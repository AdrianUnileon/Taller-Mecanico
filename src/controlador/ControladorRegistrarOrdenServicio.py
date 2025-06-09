from src.modelo.Servicios.ServicioRegistrarOrdenServicio import ServicioRegistrarOrdenServicio

class ControladorRegistrarOrdenServicio:
    def __init__(self, usuario):
        self.usuario = usuario
        self.servicio = ServicioRegistrarOrdenServicio()

    def obtener_vehiculos(self):
        return self.servicio.obtener_vehiculos()

    def registrar_orden(self, id_vehiculo: int, descripcion: str, fecha_ingreso: str, observaciones: str) -> dict:
        return self.servicio.registrar_orden(id_vehiculo, descripcion, fecha_ingreso, observaciones)
