from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def main_page():
    return render_template("main_page.html")

@app.route('/ejercicio_1')
def ejercicio_1():
    return render_template("ejercicio_1.html")