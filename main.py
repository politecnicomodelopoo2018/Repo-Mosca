from class_MainDB import MainDB
from flask import Flask, render_template, request

flask_app = Flask(__name__)

db = MainDB()

@flask_app.route('/')
def main_page():
    return render_template("main_page.html")

@flask_app.route('/table_display', methods=['GET', 'POST'])
def table_display():
    # Categorias
    tmp_obj = db.db_tables["category"]()
    table_rows = db.getlist_table("ForoMoscaDB", tmp_obj.table_name)
    return render_template("table_display.html", table_name=tmp_obj.table_name, table_cols=tmp_obj.cols, table_list=table_rows)


if __name__ == "__main__":
    flask_app.run(debug=True)