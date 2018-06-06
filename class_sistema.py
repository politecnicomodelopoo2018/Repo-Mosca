from class_persona import Pasajero, Servicio, Piloto
from class_avion import *
from class_vuelo import *
import json

class Sistema(object):

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        self.lista_pasajeros = []
        self.lista_servicio = []
        self.lista_pilotos = []

        self.lista_aviones = []
        self.lista_vuelos = []

    def get_avion(self, codigo):
        for avion in self.lista_aviones:
            if avion.codigoUnico == codigo:
                return avion
        return False

    def get_persona(self, dni):
        for persona in self.lista_pasajeros + self.lista_servicio + self.lista_pilotos:
            if persona.dni == dni:
                return persona
        return False

    def cargar_datos(self, archivo):
        with open(archivo, "r") as arch:
            diccionario_datos = json.loads(arch.read())

        # Cargar aviones
        self.lista_aviones = []
        for avion in diccionario_datos["Aviones"]:
            self.crear_avion(avion["codigoUnico"], avion["cantidadDePasajerosMaxima"], avion["cantidadDeTripulaciónNecesaria"])

        # Cargar personas
        self.lista_pilotos, self.lista_servicio, self.lista_pasajeros = [], [], []
        for persona in diccionario_datos["Personas"]:
            datos_necesarios = [persona["nombre"], persona["apellido"], persona["fechaNacimiento"], persona["dni"]]
            if persona["tipo"] == "Pasajero":
                nec_esp = ""
                try:
                    nec_esp = persona["solicitudesEspeciales"]
                except KeyError:
                    pass

                self.crear_pasajero(*datos_necesarios, persona["vip"], nec_esp)

            elif persona["tipo"] == "Piloto" or persona["tipo"] == "Servicio":
                aviones_hab = []
                try:
                    for avion in persona["avionesHabilitados"]:
                        tmp_avion = self.get_avion(avion)
                        if tmp_avion:
                            aviones_hab.append(tmp_avion)
                except KeyError:
                    pass

                if persona["tipo"] == "Piloto":
                    self.crear_piloto(*datos_necesarios, aviones_hab)
                else:
                    self.crear_servicio(*datos_necesarios, aviones_hab, persona["idiomas"])

        # Cargar vuelos
        self.lista_vuelos = []
        for vuelo in diccionario_datos["Vuelos"]:
            v_avion = self.get_avion(vuelo["avion"])
            v_tripulacion = []
            v_pasajeros = []

            # Cargar tripulacion del vuelo
            for pers_trip in vuelo["tripulacion"]:
                tmp_pers = self.get_persona(pers_trip)
                if tmp_pers:
                    v_tripulacion.append(tmp_pers)

            # Cargar pasajeros del vuelo
            for pers_pasaj in vuelo["pasajeros"]:
                tmp_pasaj = self.get_persona(pers_pasaj)
                if tmp_pasaj:
                    v_tripulacion.append(tmp_pasaj)

            self.crear_vuelo(v_avion, vuelo["fecha"], vuelo["hora"], vuelo["origen"], vuelo["destino"], v_tripulacion, v_pasajeros)

    def crear_pasajero(self, nombre, apellido, fechanac, dni, vip, nec_esp):
        tmp_pasajero = Pasajero(nombre, apellido, fechanac, dni, vip, nec_esp)
        self.lista_pasajeros.append(tmp_pasajero)
        return tmp_pasajero

    def crear_servicio(self, nombre, apellido, fechanac, dni, aviones_hab, idiomas):
        tmp_servicio = Servicio(nombre, apellido, fechanac, dni, aviones_hab, idiomas)
        self.lista_servicio.append(tmp_servicio)
        return tmp_servicio

    def crear_piloto(self, nombre, apellido, fechanac, dni, aviones_hab):
        tmp_piloto = Piloto(nombre, apellido, fechanac, dni, aviones_hab)
        self.lista_pilotos.append(tmp_piloto)
        return tmp_piloto

    def crear_avion(self, codigo, max_pasajeros, trip_necesaria):
        tmp_avion = Avion(codigo, max_pasajeros, trip_necesaria)
        self.lista_aviones.append(tmp_avion)
        return tmp_avion

    def crear_vuelo(self, avion, fecha, hora, origen, destino, tripulacion, pasajeros):
        tmp_vuelo = Vuelo(avion, fecha, hora, origen, destino, tripulacion, pasajeros)
        self.lista_vuelos.append(tmp_vuelo)
        return tmp_vuelo