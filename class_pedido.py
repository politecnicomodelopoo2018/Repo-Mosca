class Pedido(object):
    def __init__(self, fecha_creacion, plato, cliente, hora_entrega):
        self.fecha_creacion = fecha_creacion
        self.plato = plato
        self.cliente = cliente
        self.hora_entrega = hora_entrega

        self.entregado = False

    def info_string(self):
        return "Dia: " + str(self.fecha_creacion) + " - " + self.plato.info_string() + " - " + self.cliente.info_string()\
               + " - A entregarse a las " + str(self.hora_entrega[0]) + ":" + str(self.hora_entrega[1])