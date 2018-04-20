class Persona(object):
    def __init__(self, nombre, apellido, fechanac):
        self.nombre = nombre
        self.apellido = apellido
        self.fechanac = fechanac

class Artista(Persona):
    pass

class Autor(Persona):
    def __init__(self, nombre, apellido, fechanac, nacion):
        Persona.__init__(self, nombre, apellido, fechanac)
        self.nacionalidad = nacion