from src.modelo.UserDao.OrdenServicioDAO import OrdenServicioDAO

class ConsultaEstadoService:
    def __init__(self):
        self.orden_dao = OrdenServicioDAO()

    def obtener_ordenes_asignadas_por_mecanico(self, id_mecanico: int):
        if not isinstance(id_mecanico, int):
            raise ValueError("ID de mecánico inválido")
        return self.orden_dao.obtener_ordenes_por_mecanico(id_mecanico)

    def obtener_ordenes_por_cliente(self, id_cliente: int):
        if not isinstance(id_cliente, int):
            raise ValueError("ID de cliente inválido")
        return self.orden_dao.obtener_ordenes_por_cliente(id_cliente)

    def obtener_ordenes_actuales_por_cliente(self, id_cliente: int):
        if not isinstance(id_cliente, int):
            raise ValueError("ID de cliente inválido")
        return self.orden_dao.obtener_ordenesActuales_por_cliente(id_cliente)
