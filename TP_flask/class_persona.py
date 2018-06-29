import datetime

class Persona(object):
    def __init__(self, nombre, apellido, fechanac, dni):
        self.nombre = nombre
        self.apellido = apellido
        if type(fechanac) is str:
            self.fechaNacimiento = datetime.datetime.strptime(fechanac, "%Y-%m-%d")
        else:
            self.fechaNacimiento = fechanac
        self.dni = dni

    def get_edad(self):
        return datetime.datetime.now() - self.fechaNacimiento

class Pasajero(Persona):
    def __init__(self, nombre, apellido, fechanac, dni, vip, nec_esp):
        Persona.__init__(self, nombre, apellido, fechanac, dni)

        self.vip = vip
        self.solicitudesEspeciales = nec_esp


class Tripulante(Persona):
    def __init__(self, nombre, apellido, fechanac, dni, aviones_hab):
        Persona.__init__(self, nombre, apellido, fechanac, dni)

        self.avionesHabilitados = aviones_hab

class Servicio(Tripulante):
    def __init__(self, nombre, apellido, fechanac, dni, aviones_hab, idiomas):
        Tripulante.__init__(self, nombre, apellido, fechanac, dni, aviones_hab)

        self.idiomas = idiomas


class Piloto(Tripulante):
    pass