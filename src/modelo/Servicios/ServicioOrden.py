from src.modelo.UserDao.OrdenServicioDAO import OrdenServicioDAO

class ServicioOrden:
    def __init__(self):
        self.orden_dao = OrdenServicioDAO()

    def actualizar_estado(self, id_orden: int, nuevo_estado: str, costo_mano_obra: float = None) -> bool:
        return self.orden_dao.actualizar_estado(id_orden, nuevo_estado, costo_mano_obra)
    
    def obtener_ordenes_actuales_por_cliente(self, id_cliente: int):
        return self.orden_dao.obtener_ordenesActuales_por_cliente(id_cliente)

