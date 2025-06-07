class ProveedorVO:
    def __init__(self, IDProveedor=None, Nombre=None, Contacto=None, Direccion=None):
        self.IDProveedor = IDProveedor
        self.Nombre = Nombre
        self.Contacto = Contacto
        self.Direccion = Direccion
    @property
    def IDProveedor(self):
        return self._IDProveedor

    @IDProveedor.setter
    def IDProveedor(self, value):
        self._IDProveedor = value

    @property
    def Nombre(self):
        return self._Nombre

    @Nombre.setter
    def Nombre(self, value):
        self._Nombre = value

    @property
    def Contacto(self):
        return self._Contacto

    @Contacto.setter
    def Contacto(self, value):
        self._Contacto = value

    @property
    def Direccion(self):
        return self._Direccion
    
    @Direccion.setter
    def Direccion(self, value):
        self._Direccion = value