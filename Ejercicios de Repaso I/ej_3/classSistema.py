from classEmpleado import Empleado
from classLlamada import Llamada

class Sistema(object):
    def __init__(self):
        self.lista_empleados = []
        self.lista_llamadas = []

    def agregarEmpleado(self, nombre, apellido, dni, pais, telefono):
        tmp_empleado = Empleado(nombre, apellido, dni, pais, telefono)
        self.lista_empleados.append(tmp_empleado)

        return tmp_empleado

    def realizarLlamada(self, emp_inicio, emp_destino, fecha, duracion):
        self.lista_llamadas.append(Llamada(emp_inicio, emp_destino, fecha, duracion))

    def llamadasEmpleado(self, empleado, exterior = False):
        llamadas_emp = []
        for llam in self.lista_llamadas:
            if llam.emp_inicio == empleado:
                if not exterior or not llam.emp_inicio.pais == llam.emp_destino.pais:
                    llamadas_emp.append(llam)

        return llamadas_emp

    def rankingExterior(self):
        ranking = []

        for i, emp in enumerate(self.lista_empleados):
            ranking.append(Ranking(emp, 0))
            for llam in self.llamadasEmpleado(emp, True):
                ranking[i].duracion += llam.duracion

        for i in range(len(ranking)):
            for j in range(len(ranking) - 1):
                if ranking[j].duracion < ranking[j + 1].duracion:
                    ranking[j], ranking[j + 1] = ranking[j + 1], ranking[j]

        return ranking

class Ranking(object):
    def __init__(self, empleado, duracion):
        self.empleado = empleado
        self.duracion = duracion