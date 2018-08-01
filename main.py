from class_MainDB import MainDB
from flask import Flask, render_template

flask_app = Flask(__name__)

db = MainDB();

@flask_app.route('/')
def main_page():
    return render_template("main_page.html", database=db)


if __name__ == "__main__":
    flask_app.run(debug=True)