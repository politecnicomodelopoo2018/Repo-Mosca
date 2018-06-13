from class_sistema import *

sist = Sistema()
sist.cargar_datos("datos.json")

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

# Punto 5
print("5) Tripulantes con mas de un viaje en determinado dia:")
for vuelo in sist.lista_vuelos:
