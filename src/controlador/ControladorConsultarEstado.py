from src.modelo.Servicios.ConsultaEstadoService import ConsultaEstadoService

class ControladorConsultarEstado:
    def __init__(self):
        self.servicio = ConsultaEstadoService()

    def obtener_ordenes_asignadas_por_mecanico(self, id_mecanico: int):
        try:
            return self.servicio.obtener_ordenes_asignadas_por_mecanico(id_mecanico)
        except ValueError as e:
            print(f"Error de validación: {e}")
            return []
        except Exception as e:
            print(f"Error inesperado: {e}")
            return []

    def obtener_ordenes_por_cliente(self, id_cliente: int):
        try:
            return self.servicio.obtener_ordenes_por_cliente(id_cliente)
        except ValueError as e:
            print(f"Error de validación: {e}")
            return []
        except Exception as e:
            print(f"Error al obtener órdenes del cliente: {e}")
            return []

    def obtener_ordenes_actuales_por_cliente(self, id_cliente: int):
        try:
            return self.servicio.obtener_ordenes_actuales_por_cliente(id_cliente)
        except ValueError as e:
            print(f"Error de validación: {e}")
            return []
        except Exception as e:
            print(f"Error al obtener órdenes actuales: {e}")
            return []
