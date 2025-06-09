from src.modelo.Servicios.DarDeBajaServicio import DarDeBajaVehiculoServicio

class ControladorDarDeBajaVehiculos:
    def __init__(self):
        self.servicio = DarDeBajaVehiculoServicio()

    def obtener_vehiculos_sin_ordenes(self):
        try:
            return self.servicio.obtener_vehiculos_sin_ordenes()
        except Exception as e:
            print(f"Error al obtener vehículos sin órdenes: {e}")
            return []

    def dar_de_baja_vehiculo(self, id_vehiculo: int) -> (bool, str):
        try:
            return self.servicio.dar_de_baja_vehiculo(id_vehiculo)
        except ValueError as e:
            return False, f"Error de validación: {e}"
        except Exception as e:
            return False, f"Error inesperado: {e}"
