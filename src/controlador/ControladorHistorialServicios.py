from src.modelo.UserDao.OrdenServicioDAO import OrdenServicioDAO

class ControladorHistorialServicios:
    def __init__(self, id_cliente):
        self.id_cliente = id_cliente
        self.orden_dao = OrdenServicioDAO()

    def obtener_historial(self):
        """
        Obtiene el historial completo de órdenes para el cliente.
        Retorna una lista de diccionarios con los datos de las órdenes.
        """
        try:
            return self.orden_dao.obtener_ordenes_por_cliente(self.id_cliente)
        except Exception as e:
            print(f"Error obteniendo historial de servicios: {e}")
            return []

