class Persona(object):
    def __init__(self, nombre, fechanac):
        self.nombre = nombre
        self.fecha_nacimiento = fechanac

        self.calorias_consumidas = 0

    def consumirPlato(self, plato):
        self.calorias_consumidas += plato.calorias