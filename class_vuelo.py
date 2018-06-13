import datetime

class Vuelo(object):
    def __init__(self, avion, fecha, hora, origen, destino, tripulacion, pasajeros):
        self.avion = avion
        if type(fecha) is str:
            self.fecha = datetime.datetime.strptime(fecha, "%Y-%m-%d")
        else:
            self.fecha = fecha
        self.hora = hora
        self.origen = origen
        self.destino = destino
        self.tripulacion = tripulacion
        self.pasajeros = pasajeros

    def get_info(self):
        return "Vuelo de " + self.origen + " a " + self.destino + " [" + self.hora + "]"