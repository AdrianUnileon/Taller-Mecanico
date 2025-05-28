class PedidoVO:
    def __init__(self, IDPedido=None, FechaPedido=None, Estado=None, IDProveedor=None):
        self.IDPedido = IDPedido
        self.FechaPedido = FechaPedido
        self.Estado = Estado
        self.IDProveedor = IDProveedor
        
    @property
    def IDPedido(self):
        return self._IDPedido

    @IDPedido.setter
    def IDPedido(self, value):
        self._IDPedido = value

    @property
    def FechaPedido(self):
        return self._FechaPedido

    @FechaPedido.setter
    def FechaPedido(self, value):
        self._FechaPedido = value

    @property
    def Estado(self):
        return self._Estado

    @Estado.setter
    def Estado(self, value):
        self._Estado = value

    @property
    def IDProveedor(self):
        return self._IDProveedor
    
    @IDProveedor.setter
    def IDProveedor(self, value):
        self._IDProveedor = value