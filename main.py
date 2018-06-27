from class_sistema import *
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

sist = Sistema()
sist.cargar_datos("datos.json")

@app.route('/')
def main_page():
    return render_template("main_page.html")

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

# Punto 1
print("1) Pasajeros por vuelo:")
for vuelo in sist.lista_vuelos:
    print("\t" + vuelo.get_info())
    for pasaj in vuelo.pasajeros:
        tmp_vip = "no"
        if pasaj.vip:
            tmp_vip = "si"
        print("\t\tPasajero " + pasaj.dni + " - " + pasaj.apellido + " " + pasaj.nombre + ":")
        print("\t\t\tVIP: " + tmp_vip)
        if pasaj.solicitudesEspeciales:
            print("\t\t\tSolicitudes: " + pasaj.solicitudesEspeciales)

print("\n")
# Punto 2
print("2) Pasajero mas joven por vuelo:")
for vuelo in sist.lista_vuelos:
    print("\t" + vuelo.get_info())

    edad = None
    pasaj_joven = None
    for pasaj in vuelo.pasajeros:
        tmp_edad = pasaj.get_edad()
        if not edad or (edad and tmp_edad < edad):
            edad = tmp_edad
            pasaj_joven = pasaj

    if pasaj_joven:
        print("\t\tPasajero mas joven: " + pasaj_joven.apellido + " " + pasaj_joven.nombre + " (DNI " + str(pasaj_joven.dni) + ")")

print("\n")
# Punto 3
print("3) Vuelos que no llegan a la tripulacion minima:")
for vuelo in sist.lista_vuelos:
    vuelo_cant_trip = len(vuelo.tripulacion)
    vuelo_cant_nec = vuelo.avion.trip_necesaria
    if vuelo_cant_trip < vuelo_cant_nec:
        print("\t" + vuelo.get_info())
        print("\t\t" + str(vuelo_cant_trip) + " tripulantes de " + str(vuelo_cant_nec) + " necesarios.")

print("\n")
# Punto 4
print("4) Vuelos tripulados por personas no autorizadas:")
for vuelo in sist.lista_vuelos:
    trip_no_autorizada = []
    for trip in vuelo.tripulacion:
        if vuelo.avion not in trip.avionesHabilitados:
            trip_no_autorizada.append(trip)

    if len(trip_no_autorizada) > 0:
        print("\t" + vuelo.get_info())
        for trip in trip_no_autorizada:
            print("\t\tTripulante " + trip.apellido + " " + trip.nombre + " (DNI " + str(trip.dni) + ")")

print("\n")
# Punto 5
print("5) Tripulantes con mas de un viaje en determinado dia:")
tmp_trips = []
for vuelo in sist.lista_vuelos:
    for vuelo2 in sist.lista_vuelos:
        if not vuelo == vuelo2:
            if vuelo.fecha == vuelo2.fecha:
                for trip in vuelo.tripulacion:
                    if trip in vuelo2.tripulacion and trip not in [t[0] for t in tmp_trips]:
                        tmp_trips.append([trip, vuelo, vuelo2])

for trip in tmp_trips:
    print("\tTripulante " + trip[0].apellido + " " + trip[0].nombre + " (DNI " + str(trip[0].dni) + ")")
    for vuelo_extra in trip[1:]:
        print("\t\tAparece en [" + vuelo_extra.get_info() + "]")

# Punto 6 implicitamente realizado en punto 1

print("\n")
# Punto 7
print("7) Idiomas hablados por la tripulacion en cada vuelo:")
for vuelo in sist.lista_vuelos:
    print("\t" + vuelo.get_info())

    vuelo_idiomas = []
    for trip in vuelo.tripulacion:
        try:
            for i in trip.idiomas:
                if i not in vuelo_idiomas:
                    vuelo_idiomas.append(i)
        except AttributeError:
            pass

    print("\t\t" + str(vuelo_idiomas))