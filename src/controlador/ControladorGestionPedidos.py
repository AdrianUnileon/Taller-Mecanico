from src.modelo.Servicios.ServicioGestionPedidos import ServicioGestionPedidos

class ControladorPedido:
    def __init__(self):
        self.servicio = ServicioGestionPedidos()

    def obtener_proveedores(self) -> list:
        return self.servicio.obtener_proveedores()

    def crear_pedido(self, nombre_proveedor: str, repuestos: list) -> bool:
        return self.servicio.crear_pedido(nombre_proveedor, repuestos)
