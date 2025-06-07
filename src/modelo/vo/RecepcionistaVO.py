class RecepcionistaVO:
    def __init__(self, IDRecepcionista=None, IDUsuario=None, Nombre = None, Apellidos = None, Turno = None):
        self.IDRecepcionista = IDRecepcionista
        self.IDUsuario = IDUsuario
        self.Nombre = Nombre
        self.Apellidos = Apellidos
        self.Turno = Turno

    @property
    def IDUsuario(self):
        return self._IDUsuario

    @IDUsuario.setter
    def IDUsuario(self, value):
        self._IDUsuario = value

    @property
    def Turno(self):
        return self._Turno

    @Turno.setter
    def Turno(self, value):
        self._Turno = value

    @property
    def IDRecepcionista(self):
        return self._IDRecepcionista
    
    @IDRecepcionista.setter
    def IDRecepcionista(self, value):
        self._IDRecepcionista = value

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