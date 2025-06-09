from src.modelo.Servicios.ServicioOrden import ServicioOrden

class ControladorActualizarEstado:
    def __init__(self):
        self.servicio = ServicioOrden()

    def actualizar_estado_orden(self, id_orden, nuevo_estado, costo_mano_obra=None):
        return self.servicio.actualizar_estado(id_orden, nuevo_estado, costo_mano_obra)

