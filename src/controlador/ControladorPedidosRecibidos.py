from src.modelo.UserDao.PedidoDAO import PedidoDAO

class ControladorActualizarPedido:
    def __init__(self):
        self.dao_pedido = PedidoDAO()

    def obtener_pedidos_en_transito(self):
        return self.dao_pedido.obtener_pedidos_por_estado("en transito")

    def marcar_pedido_como_recibido(self, id_pedido):
        return self.dao_pedido.actualizar_estado_pedido(id_pedido, "recibido")
