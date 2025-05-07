class UserVO:
    def __init__(self, IDUsuario=None, DNI=None, Nombre=None, Apellidos=None, Correo=None, Contraseña=None, TipoUsuario=None):
        self._IDUsuario = IDUsuario
        self._DNI = DNI
        self._Nombre = Nombre
        self._Apellidos = Apellidos
        self._Correo = Correo
        self._Contraseña = Contraseña
        self._TipoUsuario = TipoUsuario

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
    def Apellidos(self):
        return self._Apellidos

    @Apellidos.setter
    def Apellidos(self, value):
        self._Apellidos = value

    @property
    def Correo(self):
        return self._Correo

    @Correo.setter
    def Correo(self, value):
        self._Correo = value

    @property
    def Contraseña(self):
        return self._Contraseña

    @Contraseña.setter
    def Contraseña(self, value):
        self._Contraseña = value

    @property
    def TipoUsuario(self):
        return self._TipoUsuario

    @TipoUsuario.setter
    def TipoUsuario(self, value):
        self._TipoUsuario = value

    def __str__(self):
        return f"UserVO(DNI={self._DNI}, Nombre='{self._Nombre}', Correo='{self._Correo}')"