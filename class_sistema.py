from class_persona import Alumno, Profesor
from class_plato import Plato
from class_pedido import Pedido

class Sistema(object):
    def __init__(self):
        self.lista_alumnos = []
        self.lista_profesores = []

        self.lista_platos = []
        self.lista_pedidos = []

    # Creacion de objetos
    def crearAlumno(self, nombre, apellido, division):
        tmp_alumno = Alumno(nombre, apellido, division)
        self.lista_alumnos.append(tmp_alumno)
        return tmp_alumno

    def crearProfesor(self, nombre, apellido, descuento):
        tmp_profesor = Profesor(nombre, apellido, descuento)
        self.lista_profesores.append(tmp_profesor)
        return tmp_profesor

    def crearPlato(self, nombre, precio):
        tmp_plato = Plato(nombre, precio)
        self.lista_platos.append(tmp_plato)
        return tmp_plato

    def crearPedido(self, fecha, plato, cliente, hora_entrega):
        tmp_pedido = Pedido(fecha, plato, cliente, hora_entrega)
        self.lista_pedidos.append(tmp_pedido)
        return tmp_pedido

    # Metodos
