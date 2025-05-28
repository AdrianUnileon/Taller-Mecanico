from src.modelo.UserDao.OrdenServicioDAO import OrdenServicioDAO
from src.modelo.UserDao.VehiculoDAO import VehiculoDAO
from src.modelo.vo.OrdenServicioVO import OrdenServicioVO

class ControladorRegistrarOrdenServicio:
    def __init__(self, usuario):
        self.usuario = usuario
        self.dao_orden = OrdenServicioDAO()
        self.dao_vehiculo = VehiculoDAO()

    def obtener_vehiculos(self):
        return self.dao_vehiculo.select()

    def registrar_orden(self, id_vehiculo: int, descripcion: str, fecha_ingreso: str, observaciones: str) -> dict:
        if not all([id_vehiculo, descripcion, fecha_ingreso, observaciones]):
            return {"Error", "Todos los campos son obligatorios."}

        orden = OrdenServicioVO(
            FechaIngreso=fecha_ingreso,
            Descripcion=descripcion,
            Estado="Pendiente de asignación",
            IDVehiculo=id_vehiculo,
            IDMecanico=None
        )

        if self.dao_orden.insertar(orden) > 0:
            return {"Exito", "Orden registrada correctamente."}
        else:
            return {"Error", "Error al registrar la orden."}
