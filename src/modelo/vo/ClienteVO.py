'''class ClienteVO:
    def __init__(self, IDUsuario=None, DNI=None, Nombre=None, Apellido1=None, Apellido2=None, Telefono=None, Email=None, Direccion=None):
        self._IDUsuario = IDUsuario
        self._DNI = DNI
        self._Nombre = Nombre
        self._Apellido1 = Apellido1
        self._Apellido2 = Apellido2
        self._Telefono = Telefono
        self._Email = Email
        self._Direccion = Direccion

    # Getters y setters
    @property
    def IDUsuario(self):
        return self._IDUsuario

    @IDUsuario.setter
    def IDUsuario(self, value):
        self._IDUsuario = value

    @property
    def DNI(self):
        return self._DNI

    @DNI.setter
    def DNI(self, value):
        self._DNI = value

    @property
    def Nombre(self):
        return self._Nombre

    @Nombre.setter
    def Nombre(self, value):
        self._Nombre = value

    @property
    def Apellido1(self):
        return self._Apellido1

    @Apellido1.setter
    def Apellido1(self, value):
        self._Apellido1 = value

    @property
    def Apellido2(self):
        return self._Apellido2

    @Apellido2.setter
    def Apellido2(self, value):
        self._Apellido2 = value

    @property
    def Telefono(self):
        return self._Telefono

    @Telefono.setter
    def Telefono(self, value):
        self._Telefono = value

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, value):
        self._Email = value

    @property
    def Direccion(self):
        return self._Direccion

    @Direccion.setter
    def Direccion(self, value):
        self._Direccion = value

    def __str__(self):
        return f"ClienteVO(DNI={self._DNI}, Nombre='{self._Nombre}', Email='{self._Email}', Direccion='{self._Direccion}')"
'''

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
