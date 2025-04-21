import decimal

class ProductoDTO:
    def __init__(self):
        self.id = None
        self.nombre = None
        self.id_categoria = None
        self.id_marca = None
        self.id_proveedor = None
        self.precio = decimal.Decimal("0.00")

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_id_categoria(self):
        return self.id_categoria

    def set_id_categoria(self, id_categoria):
        self.id_categoria = id_categoria

    def get_id_marca(self):
        return self.id_marca

    def set_id_marca(self, id_marca):
        self.id_marca = id_marca

    def get_id_proveedor(self):
        return self.id_proveedor

    def set_id_proveedor(self, id_proveedor):
        self.id_proveedor = id_proveedor

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = decimal.Decimal(precio)
