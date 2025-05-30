from src.modelo.UserDao.VehiculoDAO import VehiculoDAO

class ControladorDarDeBajaVehiculos:
    def __init__(self):
        self.vehiculo_dao = VehiculoDAO()

    def obtener_vehiculos_con_clientes(self):
        
        return self.vehiculo_dao.obtener_vehiculos_con_clientes()

    def dar_de_baja_vehiculo(self, id_vehiculo: int) -> (bool, str):
        try:
            resultado = self.vehiculo_dao.eliminar_vehiculo(id_vehiculo)
            if resultado:
                return True, "El vehículo ha sido dado de baja correctamente."
            else:
                return False, "No se pudo dar de baja el vehículo. Verifique que no tenga órdenes activas."
        except Exception as e:
            return False, f"Error al dar de baja el vehículo: {e}"
