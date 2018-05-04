class Plato(object):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def info_string(self):
        return self.nombre + ": $" + str(self.precio)