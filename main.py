from class_sistema import *

sist = Sistema()

sist.cargar_datos("datos.json")

print("PILOTOS:\n", sist.lista_pilotos, "\n")
print("SERVICIO:\n", sist.lista_servicio, "\n")
print("PASAJEROS:\n", sist.lista_pasajeros, "\n")
print("AVIONES:\n", sist.lista_aviones, "\n")
print("VUELOS:\n", sist.lista_vuelos, "\n")