from class_MainDB import MainDB
from flask import Flask, render_template, request, redirect
import pymysql

flask_app = Flask(__name__)

db = MainDB("ForoMoscaDB")


@flask_app.route('/')
def main_page():
    return render_template("main_page.html", db_tables=db.db_tables)

@flask_app.route('/table_display/<string:table_name>')
def table_display(table_name):
    tmp_obj = None
    table_rows = []
    if table_name.lower() in db.db_tables:
        tmp_obj = db.db_tables[table_name.lower()]()
        table_rows = db.getlist_table(tmp_obj.table_name)

    if tmp_obj:
        return render_template("table_display.html", table_name=table_name, table_cols=tmp_obj.cols, table_list=table_rows)
    return redirect('/')

@flask_app.route('/table_edit', methods=['GET', 'POST'])
def table_edit():
    form_data = request.form

    tmp_obj = None
    tmp_mode = "edit"
    for data in form_data:
        if data == "mode_add":
            tmp_mode = "add"
            tmp_obj = db.db_tables[form_data[data].lower()]()
        else:
            tmp_obj = db.get_table_row(data, form_data[data])

    fkey_cols = {}
    fkey_constraint = 1
    for col in tmp_obj.fkey_cols:
        fkey_cols[col] = db.getlist_table(tmp_obj.fkey_cols[col].foreign_table)
        if len(fkey_cols[col]) == 0:
            fkey_constraint = 0

    return render_template("table_edit.html", mode=tmp_mode, edit_row=tmp_obj, fkey_cols=fkey_cols, fkey_constraint=fkey_constraint)

@flask_app.route('/table_edit_complete', methods=['GET', 'POST'])
def table_edit_complete():
    form_data = request.form

    table_name = ""
    table_cols = {}
    tmp_mode = "edit"
    for data in form_data:
        if data == "tablename":
            table_name = form_data[data]
        elif data == "mode":
            tmp_mode = form_data[data]
        else:
            data_split = data.split('.')
            if len(data_split) > 1:
                if data_split[0] == "column":
                    table_cols[data_split[1]] = form_data[data]

    if table_name.lower() in db.db_tables:
        tmp_obj = db.db_tables[table_name.lower()]()
        tmp_obj.load_from_dict(table_cols)
        try:
            if tmp_mode == "edit":
                db.run_query(tmp_obj.query_update())
            elif tmp_mode == "add":
                db.run_query(tmp_obj.query_insert())
        except pymysql.err.DataError as err:
            print(err)

        return redirect('/table_display/' + table_name)
    return redirect('/')

@flask_app.route('/table_delete', methods=['GET', 'POST'])
def table_delete():
    form_data = request.form

    for table in form_data:
        if table.lower() in db.db_tables:
            tmp_obj = db.get_table_row(table, form_data[table])
            if tmp_obj:
                db.run_query([tmp_obj.query_delete(), ()])
            return redirect('/table_display/' + table)
    return redirect('/')


if __name__ == "__main__":
    flask_app.run(debug=True)