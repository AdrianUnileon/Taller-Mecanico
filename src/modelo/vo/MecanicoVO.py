class MecanicoVO:
    def __init__(self, IDMecanico=None, IDUsuario=None, Especialidad=None, FechaContratacion=None, Nombre = None, Apellidos = None):
        self.IDMecanico = IDMecanico
        self.IDUsuario = IDUsuario
        self.Especialidad = Especialidad
        self.FechaContratacion = FechaContratacion
        self.Nombre = Nombre
        self.Apellidos = Apellidos

    @property
    def IDUsuario(self):
        return self._IDUsuario

    @IDUsuario.setter
    def IDUsuario(self, value):
        self._IDUsuario = value

    @property
    def Especialidad(self):
        return self._Especialidad

    @Especialidad.setter
    def Especialidad(self, value):
        self._Especialidad = value

    @property
    def FechaContratacion(self):
        return self._FechaContratacion

    @FechaContratacion.setter
    def FechaContratacion(self, value):
        self._FechaContratacion = value

    @property
    def IDMecanico(self):
        return self._IDMecanico
    
    @IDMecanico.setter
    def IDMecanico(self, value):
        self._IDMecanico = value

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
