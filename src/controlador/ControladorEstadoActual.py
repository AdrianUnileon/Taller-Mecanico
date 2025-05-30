from src.modelo.UserDao.OrdenServicioDAO import OrdenServicioDAO

class ControladorEstadoActual:
    def __init__(self):
        self.dao = OrdenServicioDAO()

    def obtener_ordenes_actuales(self, id_cliente):
        """
        Retorna una lista de órdenes de servicio actuales (estado 'Asignada')
        del cliente con el ID proporcionado.
        """
        try:
            return self.dao.obtener_ordenesActuales_por_cliente(id_cliente)
        except Exception as e:
            print(f"Error en ControladorEstadoActual.obtener_ordenes_actuales: {e}")
            return []
