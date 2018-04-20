class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Alumno(Persona):
    def __init__(self, nombre, apellido, division):
        Persona.__init__(self, nombre, apellido)
        self.division = division

    def info_string(self):
        return self.nombre + " " + self.apellido + ", division " + self.division

class Profesor(Persona):
    def __init__(self, nombre, apellido, descuento):
        Persona.__init__(self, nombre, apellido)
        self.descuento = descuento

    def info_string(self):
        return self.nombre + " " + self.apellido + ", " + str(self.descuento) + "% de descuento"