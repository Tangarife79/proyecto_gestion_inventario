import decimal
import datetime

class VentaDTO:
    def __init__(self):
        self.id = None
        self.id_cliente = None
        self.fecha = datetime.datetime.now()
        self.total = decimal.Decimal("0.00")

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_id_cliente(self):
        return self.id_cliente

    def set_id_cliente(self, id_cliente):
        self.id_cliente = id_cliente

    def get_fecha(self):
        return self.fecha

    def set_fecha(self, fecha):
        self.fecha = fecha

    def get_total(self):
        return self.total

    def set_total(self, total):
        self.total = decimal.Decimal(total)
