class ClienteDTO:
    def __init__(self):
        self.id = None
        self.nombre = None
        self.correo = None
        self.telefono = None

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_correo(self):
        return self.correo

    def set_correo(self, correo):
        self.correo = correo

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, telefono):
        self.telefono = telefono
