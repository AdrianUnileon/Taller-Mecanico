from src.modelo.Servicios.ServicioGestionPedidos import ServicioGestionPedidos

class ControladorPedido:
    def __init__(self):
        self.servicio = ServicioGestionPedidos()

    def obtener_proveedores(self) -> list:
        """
        Obtiene la lista de proveedores disponibles
        :return: Lista de nombres de proveedores
        """
        return self.servicio.obtener_proveedores()

    def crear_pedido(self, nombre_proveedor: str, repuestos: list) -> bool:
        """
        Crea un nuevo pedido con los repuestos especificados
        :param nombre_proveedor: Nombre del proveedor seleccionado
        :param repuestos: Lista de repuestos con formato (nombre, cantidad, precio)
        :return: True si el pedido se creó correctamente
        """
        return self.servicio.crear_pedido(nombre_proveedor, repuestos)

