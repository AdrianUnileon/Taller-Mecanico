class OrdenServicioVO:
    def __init__(self, IDOrden=None, FechaIngreso=None, Descripcion=None, Estado=None, IDVehiculo=None, IDMecanico=None, CostoManoObra=None):
        self.IDOrden = IDOrden
        self.FechaIngreso = FechaIngreso
        self.Descripcion = Descripcion
        self.Estado = Estado
        self.IDVehiculo = IDVehiculo
        self.IDMecanico = IDMecanico
        self.CostoManoObra = CostoManoObra

    @property
    def IDOrden(self):
        return self._IDOrden

    @IDOrden.setter
    def IDOrden(self, value):
        self._IDOrden = value

    @property
    def FechaIngreso(self):
        return self._FechaIngreso

    @FechaIngreso.setter
    def FechaIngreso(self, value):
        self._FechaIngreso = value

    @property
    def Descripcion(self):
        return self._Descripcion

    @Descripcion.setter
    def Descripcion(self, value):
        self._Descripcion = value

    @property
    def Estado(self):
        return self._Estado

    @Estado.setter
    def Estado(self, value):
        self._Estado = value

    @property
    def IDVehiculo(self):
        return self._IDVehiculo
    
    @IDVehiculo.setter
    def IDVehiculo(self, value):
        self._IDVehiculo = value

    @property
    def IDMecanico(self):
        return self._IDMecanico
    
    @IDMecanico.setter
    def IDMecanico(self, value):
        self._IDMecanico = value

    @property
    def CostoManoObra(self):
        return self._CostoManoObra
    
    @CostoManoObra.setter
    def CostoManoObra(self, value):
        self._CostoManoObra = value