class FacturaVO:
    def __init__(self, IDFactura=None, Fecha=None, Total=None, IDOrden=None, IDRecepcionista=None):
        self.IDFactura = IDFactura
        self.Fecha = Fecha
        self.Total = Total
        self.IDOrden = IDOrden
        self.IDRecepcionista = IDRecepcionista

    @property
    def IDFactura(self):
        return self._IDFactura

    @IDFactura.setter
    def IDFactura(self, value):
        self._IDFactura = value

    @property
    def Fecha(self):
        return self._Fecha

    @Fecha.setter
    def Fecha(self, value):
        self._Fecha = value

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, value):
        self._Total = value

    @property
    def IDOrden(self):
        return self._IDOrden
    
    @IDOrden.setter
    def IDOrden(self, value):
        self._IDOrden = value

    @property
    def IDRecepcionista(self):
        return self._IDRecepcionista

    @IDRecepcionista.setter
    def IDRecepcionista(self, value):
        self._IDRecepcionista = value

