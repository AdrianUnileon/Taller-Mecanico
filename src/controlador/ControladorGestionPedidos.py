from datetime import datetime
from src.modelo.UserDao.ProveedorDAO import ProveedorDAO
from src.modelo.UserDao.PedidoDAO import PedidoDAO
from src.modelo.UserDao.RepuestoDAO import RepuestoDAO

class ControladorPedido:
    def __init__(self):
        self.dao_proveedor = ProveedorDAO()
        self.dao_pedido = PedidoDAO()
        self.dao_repuesto = RepuestoDAO()

    def obtener_proveedores(self):
        return self.dao_proveedor.obtener_nombres_proveedores()

    def crear_pedido(self, nombre_proveedor, repuestos):
        proveedor_id = self.dao_proveedor.obtener_id_por_nombre(nombre_proveedor)
        if not proveedor_id:
            print("Proveedor no encontrado.")
            return False

        fecha = datetime.now().date()
        pedido_id = self.dao_pedido.insertar_pedido(proveedor_id, fecha, "en transito")
        if not pedido_id:
            print("No se pudo crear el pedido.")
            return False

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

            if not repuesto_id:
                print(f"No se pudo obtener/crear el repuesto: {nombre}")
                return False
            
            self.dao_pedido.insertar_detalle_pedido(pedido_id, repuesto_id, cantidad, precio_unitario)

        return True


