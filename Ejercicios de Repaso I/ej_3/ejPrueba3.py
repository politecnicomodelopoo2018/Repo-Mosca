# coding:utf-8

from classSistema import Sistema
from datetime import date
from random import randint, sample

sist = Sistema()

pedro = sist.agregarEmpleado("Pedro", "Gonzalez", "49028534", "Mexico", "6879-3945")
facundo = sist.agregarEmpleado("Facundo", "Gonzalez", "49028669", "Mexico", "6877-6598")

jorge = sist.agregarEmpleado("Jorge", "Castañeda", "67290593", "España", "5764-5463")
maria = sist.agregarEmpleado("Maria", "Castañeda", "67697057", "España", "5679-9693")

enrique = sist.agregarEmpleado("Enrique", "Aizpurua", "45650392", "Argentina", "4567-8495")
ignacio = sist.agregarEmpleado("Ignacio", "Aizpurua", "45236563", "Argentina", "4573-5676")

for i in range(15):
    tmp_emps = sample(sist.lista_empleados, 2)
    dur = randint(30, 660)

    print(tmp_emps[0].nombre + " (" + tmp_emps[0].pais + ") llama a " +
          tmp_emps[1].nombre + " (" + tmp_emps[1].pais +
          ") por " + str(dur / 60) + " minutos, " + str(dur % 60) + " segundos.")

    sist.realizarLlamada(tmp_emps[0], tmp_emps[1], date(randint(1990, 2010), randint(1, 12), randint(1, 28)), dur)

print("\n")
print("Ranking de llamadas al exterior:")

for i, rank in enumerate(sist.rankingExterior()):
    print("#" + str(i + 1) + ": " + rank.empleado.nombre + " " + rank.empleado.apellido + ", con " + str(rank.duracion / 60) + " minutos, " + str(rank.duracion % 60) + " segundos de llamada al exterior.")