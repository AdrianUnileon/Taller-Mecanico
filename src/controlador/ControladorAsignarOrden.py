from src.modelo.UserDao.OrdenServicioDAO import OrdenServicioDAO
from src.modelo.UserDao.MecanicoDAO import MecanicoDAO

class ControladorAsignarOrden:
    def __init__(self):
        self.dao_orden = OrdenServicioDAO()
        self.dao_mecanico = MecanicoDAO()

    def obtener_ordenes_pendientes(self):
        return self.dao_orden.select_pendientes()

    def obtener_mecanicos_disponibles(self):
        return self.dao_mecanico.obtener_mecanicos_disponibles()

    def asignar_orden(self, id_orden, id_mecanico):
        return self.dao_orden.asignar_orden(id_orden, id_mecanico)
