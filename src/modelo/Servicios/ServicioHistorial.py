from src.modelo.UserDao.OrdenServicioDAO import OrdenServicioDAO

class ServicioHistorial:
    def __init__(self, id_cliente):
        self.id_cliente = id_cliente
        self.orden_dao = OrdenServicioDAO()

    def obtener_historial(self):
        """
        Obtiene el historial completo de órdenes para el cliente.
        Retorna una lista de diccionarios con los datos de las órdenes.
        """
        return self.orden_dao.obtener_ordenes_por_cliente(self.id_cliente)