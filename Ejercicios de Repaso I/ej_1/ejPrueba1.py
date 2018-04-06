from classPersona import Persona
from datetime import date
from math import floor
from random import randint

# it - iteraciones a realizar
def generador_peso(inicial, alt, it):
    peso_base = inicial
    peso_base_min = floor(inicial * 0.5)
    peso_base_max = floor(inicial * 1.5)

    i = 0
    rand = float(randint(-1, 1))
    while i < it:
        yield max(peso_base_min, min(peso_base_max, peso_base + rand))
        i += 1
        rand += float(randint(-alt, alt))

pers = Persona("Chris", "Wilson", date(1978, 12, 8))

# Mediciones 1990 - 1992
for y in range(3):
    for peso in generador_peso(40, 1, 10):
        pers.registrarMedicion(peso * 2, peso, date(1990 + y, randint(1, 12), randint(1, 28)))

print("Promedio peso 1990: " + str(pers.prom_anual_peso(1990))) # Promedio 1990
print("Promedio peso 1991: " + str(pers.prom_anual_peso(1991))) # Promedio 1991
print("Promedio peso 1992: " + str(pers.prom_anual_peso(1992))) # Promedio 1992

print("Progresion peso 1990 - 1992: " + str(pers.porc_crecimiento_peso(1990, 1992) * 100) + "%")

print('\n')
print("Promedio altura 1990: " + str(pers.prom_anual_altura(1990))) # Promedio 1990
print("Promedio altura 1991: " + str(pers.prom_anual_altura(1991))) # Promedio 1991
print("Promedio altura 1992: " + str(pers.prom_anual_altura(1992))) # Promedio 1992

print("Progresion altura 1990 - 1992: " + str(pers.porc_crecimiento_altura(1990, 1992) * 100) + "%")