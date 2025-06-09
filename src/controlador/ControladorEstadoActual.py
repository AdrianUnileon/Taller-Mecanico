from src.modelo.Servicios.ConsultaEstadoService import ConsultaEstadoService

class ControladorEstadoActual:
    def __init__(self):
        self.servicio = ConsultaEstadoService()

    def obtener_ordenes_actuales(self, id_cliente: int):
        return self.servicio.obtener_ordenes_actuales_por_cliente(id_cliente)