import datetime

class EntradaDTO:
    def __init__(self):
        self.id = None
        self.id_producto = None
        self.cantidad = 0
        self.fecha = datetime.datetime.now()

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_id_producto(self):
        return self.id_producto

    def set_id_producto(self, id_producto):
        self.id_producto = id_producto

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_fecha(self):
        return self.fecha

    def set_fecha(self, fecha):
        self.fecha = fecha
