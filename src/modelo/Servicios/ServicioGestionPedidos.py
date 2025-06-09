from datetime import datetime
from src.modelo.UserDao.ProveedorDAO import ProveedorDAO
from src.modelo.UserDao.PedidoDAO import PedidoDAO
from src.modelo.UserDao.RepuestoDAO import RepuestoDAO

class ServicioGestionPedidos:
    def __init__(self):
        self.dao_proveedor = ProveedorDAO()
        self.dao_pedido = PedidoDAO()
        self.dao_repuesto = RepuestoDAO()

    def obtener_proveedores(self) -> list:
        """
        Obtiene la lista de nombres de proveedores disponibles
        :return: Lista de nombres de proveedores
        """
        return self.dao_proveedor.obtener_nombres_proveedores()

    def crear_pedido(self, nombre_proveedor: str, repuestos: list) -> bool:
        """
        Crea un nuevo pedido con sus repuestos asociados
        :param nombre_proveedor: Nombre del proveedor
        :param repuestos: Lista de tuplas (nombre_repuesto, cantidad, precio_unitario)
        :return: True si la operación fue exitosa, False en caso contrario
        """
        proveedor_id = self.dao_proveedor.obtener_id_por_nombre(nombre_proveedor)

        fecha = datetime.now().date()
        pedido_id = self.dao_pedido.insertar_pedido(proveedor_id, fecha, "en transito")

        for nombre, cantidad, precio_unitario in repuestos:
            repuesto_id = self.dao_repuesto.obtener_id_por_nombre(nombre)

            if not repuesto_id:
                repuesto_id = self.dao_repuesto.insertar_repuesto(
                    nombre=nombre,
                    cantidad=0,
                    ubicacion='Pendiente',
                    precio_unitario=precio_unitario,
                    id_proveedor=proveedor_id
                )
            
            self.dao_pedido.insertar_detalle_pedido(pedido_id, repuesto_id, cantidad, precio_unitario)
        return True

    def obtener_pedidos_pendientes(self) -> list:
        """
        Obtiene la lista de pedidos en estado 'en transito'
        :return: Lista de pedidos pendientes
        """
        # Implementar este método según sea necesario
        return self.dao_pedido.obtener_pedidos_por_estado("en transito")