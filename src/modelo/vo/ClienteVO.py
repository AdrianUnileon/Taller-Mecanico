class ClienteVO:
    def __init__(self, IDCliente=None, IDUsuario=None, Direccion=None, Contacto=None, Nombre = None, Apellidos = None):
        self.IDCliente = IDCliente
        self.IDUsuario = IDUsuario
        self.Direccion = Direccion
        self.Contacto = Contacto
        self.Nombre = Nombre
        self.Apellidos = Apellidos

    @property
    def IDUsuario(self):
        return self._IDUsuario

    @IDUsuario.setter
    def IDUsuario(self, value):
        self._IDUsuario = value

    @property
    def Direccion(self):
        return self._Direccion

    @Direccion.setter
    def Direccion(self, value):
        self._Direccion = value

    @property
    def Contacto(self):
        return self._Contacto

    @Contacto.setter
    def Contacto(self, value):
        self._Contacto = value

    @property
    def IDCliente(self):
        return self._IDCliente
    
    @IDCliente.setter
    def IDCliente(self, value):
        self._IDCliente = value

    @property
    def Nombre(self):
        return self._Nombre

    @Nombre.setter
    def Nombre(self, value):
        self._Nombre = value

    @property
    def Apellidos(self):
        return self._Apellidos

    @Apellidos.setter
    def Apellidos(self, value):
        self._Apellidos = value
