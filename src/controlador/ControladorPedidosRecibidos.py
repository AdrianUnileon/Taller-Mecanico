from src.modelo.Servicios.ServiciosPedidosRecibidos import ServicioActualizarPedido

class ControladorActualizarPedido:
    def __init__(self):
        self.servicios = ServicioActualizarPedido()

    def obtener_pedidos_en_transito(self):
        return self.servicios.obtener_pedidos_en_transito()

    def marcar_pedido_como_recibido(self, id_pedido):
        return self.servicios.marcar_pedido_como_recibido(id_pedido)
