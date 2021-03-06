from class_sistema import *
from flask import Flask, render_template, request, redirect

app = Flask(__name__, static_url_path='/static')

sist = Sistema()
sist.cargar_datos("datos.json")

@app.route('/')
def main_page():
    return render_template("table_display.html", base=sist.base_cargada)

@app.route('/ejercicio_1')
def ejercicio_1():
    return render_template("ejercicio_1.html", data=sist.ejercicio_1())

@app.route('/ejercicio_2')
def ejercicio_2():
    return render_template("ejercicio_2.html", data=sist.ejercicio_2())

@app.route('/ejercicio_3')
def ejercicio_3():
    return render_template("ejercicio_3.html", data=sist.ejercicio_3())

@app.route('/ejercicio_4')
def ejercicio_4():
    return render_template("ejercicio_4.html", data=sist.ejercicio_4())

@app.route('/ejercicio_5')
def ejercicio_5():
    return render_template("ejercicio_5.html", data=sist.ejercicio_5())

@app.route('/ejercicio_7')
def ejercicio_7():
    return render_template("ejercicio_7.html", data=sist.ejercicio_7())

@app.route('/cargar_base')
def cargar_base():
    return render_template("cargar_base.html", system=sist)

@app.route('/cargar_base_eleccion')
def cargar_base_eleccion():
    base = request.args.get('base_select')
    sist.cargar_datos(base)
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)