from src.modelo.Servicios.AsignarOrdenServicio import AsignarOrdenServicio

class ControladorAsignarOrden:
    def __init__(self):
        self.servicio = AsignarOrdenServicio()

    def obtener_ordenes_pendientes(self):
        try:
            return self.servicio.obtener_ordenes_pendientes()
        except Exception as e:
            print(f"Error al obtener órdenes pendientes: {e}")
            return []

    def obtener_mecanicos_disponibles(self):
        try:
            return self.servicio.obtener_mecanicos_disponibles()
        except Exception as e:
            print(f"Error al obtener mecánicos disponibles: {e}")
            return []

    def asignar_orden(self, id_orden, id_mecanico):
        try:
            return self.servicio.asignar_orden(id_orden, id_mecanico)
        except ValueError as e:
            print(f"Error de validación: {e}")
            return False
        except Exception as e:
            print(f"Error al asignar orden: {e}")
            return False
