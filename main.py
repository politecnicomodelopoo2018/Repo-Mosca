from class_MainDB import MainDB
from flask import Flask, render_template, request, redirect

flask_app = Flask(__name__)

db = MainDB("ForoMoscaDB")


def get_table_display(table_name):
    tmp_obj = None
    table_rows = []
    if table_name.lower() in db.db_tables:
        tmp_obj = db.db_tables[table_name.lower()]()
        table_rows = db.getlist_table(tmp_obj.table_name)

    if tmp_obj:
        return render_template("table_display.html", table_name=table_name, table_cols=tmp_obj.cols, table_list=table_rows)
    return False


@flask_app.route('/')
def main_page():
    return render_template("main_page.html", db_tables=db.db_tables)

@flask_app.route('/table_display', methods=['GET', 'POST'])
def table_display():
    form_data = request.form

    for table in form_data:
        disp = get_table_display(table)
        if disp:
            return disp
    return redirect('/')

@flask_app.route('/table_edit', methods=['GET', 'POST'])
def table_edit():
    form_data = request.form

    tmp_obj = None
    for table in form_data:
        tmp_obj = db.get_table_row(table, form_data[table])

    return render_template("table_edit.html", edit_row=tmp_obj)

@flask_app.route('/table_delete', methods=['GET', 'POST'])
def table_delete():
    form_data = request.form

    for table in form_data:
        if table.lower() in db.db_tables:
            tmp_obj = db.get_table_row(table, form_data[table])
            if tmp_obj:
                db.run_query(tmp_obj.query_delete())
            return get_table_display(table)
    return redirect('/')

@flask_app.route('/table_edit', methods=['GET', 'POST'])
def table_edit():
    form_data = request.form

    for data in form_data:


if __name__ == "__main__":
    flask_app.run(debug=True)