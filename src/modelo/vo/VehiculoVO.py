class VehiculoVO:
    def __init__(self, IDVehiculo=None, Matricula=None, Marca=None, Modelo=None, Anio=None, IDCliente=None):
        self.IDVehiculo = IDVehiculo
        self.Matricula = Matricula
        self.Marca = Marca
        self.Modelo = Modelo
        self.Anio = Anio
        self.IDCliente = IDCliente

    @property
    def IDVehiculo(self):
        return self._IDVehiculo

    @IDVehiculo.setter
    def IDVehiculo(self, value):
        self._IDVehiculo = value

    @property
    def Matricula(self):
        return self._Matricula

    @Matricula.setter
    def Matricula(self, value):
        self._Matricula = value

    @property
    def Marca(self):
        return self._Marca

    @Marca.setter
    def Marca(self, value):
        self._Marca = value

    @property
    def Modelo(self):
        return self._Modelo
    
    @Modelo.setter
    def Modelo(self, value):
        self._Modelo = value

    @property
    def Anio(self):
        return self._Anio

    @Anio.setter
    def Anio(self, value):
        self._Anio = value

    @property
    def IDCliente(self):
        return self._IDCliente

    @IDCliente.setter
    def IDCliente(self, value):
        self._IDCliente = value