from src.modelo.UserDao.OrdenServicioDAO import OrdenServicioDAO

class ControladorConsultarEstado:
    def __init__(self):
        self.orden_dao = OrdenServicioDAO()

    def obtener_ordenes_asignadas_por_mecanico(self, id_mecanico):
        """
        Devuelve las órdenes asignadas a un mecánico específico.
        """
        return self.orden_dao.obtener_ordenes_por_mecanico(id_mecanico)
