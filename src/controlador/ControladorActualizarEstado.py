from src.modelo.UserDao.OrdenServicioDAO import OrdenServicioDAO

class ControladorActualizarEstado:
    def __init__(self):
        self.orden_dao = OrdenServicioDAO()

    def actualizar_estado_orden(self, id_orden, nuevo_estado, costo_mano_obra=None):
        return self.orden_dao.actualizar_estado(id_orden, nuevo_estado, costo_mano_obra)
