from src.modelo.UserDao.VehiculoDAO import VehiculoDAO

class DarDeBajaVehiculoServicio:
    def __init__(self):
        self.vehiculo_dao = VehiculoDAO()

    def obtener_vehiculos_sin_ordenes(self):
        return self.vehiculo_dao.obtener_vehiculos_sin_ordenes()

    def dar_de_baja_vehiculo(self, id_vehiculo: int) -> (bool, str):
        if not isinstance(id_vehiculo, int) or id_vehiculo <= 0:
            raise ValueError("ID de vehículo inválido")

        resultado = self.vehiculo_dao.eliminar_vehiculo(id_vehiculo)
        if resultado:
            return True, "El vehículo ha sido dado de baja correctamente."
        else:
            return False, "No se pudo dar de baja el vehículo."
