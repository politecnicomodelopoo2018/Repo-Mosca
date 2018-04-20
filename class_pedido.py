class Pedido(object):
    def __init__(self, fecha_creacion, plato, cliente, hora_entrega):
        self.fecha_creacion = fecha_creacion
        self.plato = plato
        self.cliente = cliente
        self.hora_entrega = hora_entrega

        self.entregado = False