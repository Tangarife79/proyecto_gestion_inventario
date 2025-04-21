class InventarioDTO:
    def __init__(self):
        self.id = None
        self.id_producto = None
        self.id_ubicacion = None
        self.cantidad = 0

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_id_producto(self):
        return self.id_producto

    def set_id_producto(self, id_producto):
        self.id_producto = id_producto

    def get_id_ubicacion(self): 
        return self.id_ubicacion

    def set_id_ubicacion(self, id_ubicacion): 
        self.id_ubicacion = id_ubicacion

    def get_cantidad(self): 
        return self.cantidad
    def set_cantidad(self, cantidad): 
        self.cantidad = cantidad
