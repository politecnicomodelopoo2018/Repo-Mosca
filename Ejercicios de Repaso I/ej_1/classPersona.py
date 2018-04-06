from classMedicion import Medicion

class Persona(object):
    def __init__(self, nombre, apellido, fechanac):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fechanac

        self.lista_mediciones = []

    def registrarMedicion(self, peso, altura, fecha):
        self.lista_mediciones.append(Medicion(peso, altura, fecha))

    def obtenerMedicion(self, fecha):
        for med in self.lista_mediciones:
            if fecha == med.fecha:
                return med

        return None

    def prom_anual_peso(self, year):
        if len(self.lista_mediciones) == 0:
            return 0

        total = 0
        cont = 0
        for med in self.lista_mediciones:
            if med.fecha.year == year:
                total += med.peso
                cont += 1

        return total / cont

    def prom_anual_altura(self, year):
        if len(self.lista_mediciones) == 0:
            return 0

        total = 0
        cont = 0
        for med in self.lista_mediciones:
            if med.fecha.year == year:
                total += med.altura
                cont += 1

        return total / cont

    def porc_crecimiento_peso(self, a_inicial, a_final):
        total_ini = self.prom_anual_peso(a_inicial)
        total_fin = self.prom_anual_peso(a_final)

        return 1 - total_ini / total_fin

    def porc_crecimiento_altura(self, a_inicial, a_final):
        total_ini = self.prom_anual_altura(a_inicial)
        total_fin = self.prom_anual_altura(a_final)

        return 1 - total_ini / total_fin