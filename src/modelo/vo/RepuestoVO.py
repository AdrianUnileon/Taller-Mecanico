class RepuestoVO:
    def __init__(self, IDRepuesto=None, Nombre=None, Cantidad=None, Ubicacion=None, PrecioUnitario=None, IDProveedor=None):
        self.IDRepuesto = IDRepuesto
        self.Nombre = Nombre
        self.Cantidad = Cantidad
        self.Ubicacion = Ubicacion
        self.PrecioUnitario = PrecioUnitario
        self.IDProveedor = IDProveedor

    @property
    def IDRepuesto(self):
        return self._IDRepuesto

    @IDRepuesto.setter
    def IDRepuesto(self, value):
        self._IDRepuesto = value

    @property
    def Nombre(self):
        return self._Nombre

    @Nombre.setter
    def Nombre(self, value):
        self._Nombre = value

    @property
    def Cantidad(self):
        return self._Cantidad

    @Cantidad.setter
    def Cantidad(self, value):
        self._Cantidad = value

    @property
    def Ubicacion(self):
        return self._Ubicacion
    
    @Ubicacion.setter
    def Ubicacion(self, value):
        self._Ubicacion = value

    @property
    def PrecioUnitario(self):
        return self._PrecioUnitario

    @PrecioUnitario.setter
    def PrecioUnitario(self, value):
        self._PrecioUnitario = value

    @property
    def IDProveedor(self):
        return self._IDProveedor

    @IDProveedor.setter
    def IDProveedor(self, value):
        self._IDProveedor = value
