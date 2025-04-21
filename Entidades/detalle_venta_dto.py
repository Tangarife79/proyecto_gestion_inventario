import decimal

class DetalleVentaDTO:
    def __init__(self):
        self.id = None
        self.id_venta = None
        self.id_producto = None
        self.cantidad = 0
        self.precio_unitario = decimal.Decimal("0.00")

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_id_venta(self):
        return self.id_venta

    def set_id_venta(self, id_venta):
        self.id_venta = id_venta

    def get_id_producto(self):
        return self.id_producto

    def set_id_producto(self, id_producto):
        self.id_producto = id_producto

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio_unitario(self):
        return self.precio_unitario

    def set_precio_unitario(self, precio_unitario):
        self.precio_unitario = decimal.Decimal(precio_unitario)
