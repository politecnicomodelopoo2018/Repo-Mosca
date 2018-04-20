# -*- coding: utf-8 -*-

class Vehiculo(object):
    def __init__(self, patente, cant_ruedas, año_fab):
        self.patente = patente
        self.cant_ruedas = cant_ruedas
        self.año_fab = año_fab

class Camioneta(Vehiculo):
    def __init__(self, patente, cant_ruedas, año_fab, carga):
        Vehiculo.__init__(self, patente, cant_ruedas, año_fab)
        self.carga = carga

class Auto(Vehiculo):
    def __init__(self, patente, cant_ruedas, año_fab, descapotable):
        Vehiculo.__init__(self, patente, cant_ruedas, año_fab)
        self.descapotable = descapotable