class UsuarioDTO:
    def __init__(self):
        self.id = None
        self.nombre = None
        self.usuario = None
        self.contrasena = None
        self.id_rol = None

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_usuario(self):
        return self.usuario

    def set_usuario(self, usuario):
        self.usuario = usuario

    def get_contrasena(self):
        return self.contrasena

    def set_contrasena(self, contrasena):
        self.contrasena = contrasena

    def get_id_rol(self):
        return self.id_rol

    def set_id_rol(self, id_rol):
        self.id_rol = id_rol
