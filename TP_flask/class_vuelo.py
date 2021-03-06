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
        return "Vuelo de " + self.origen + " a " + self.destino + " con avion " + str(self.avion.codigo) + ", el dia "\
               + self.fecha.strftime("%d/%m/%Y") + " a las " + self.hora + " hs"