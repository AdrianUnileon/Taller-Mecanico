from src.modelo.Servicios.ServicioRegistrarVehiculo import ServicioRegistrarVehiculo

class ControladorRegistrarVehiculo:
    def __init__(self, usuario):
        self.usuario = usuario
        self.servicio = ServicioRegistrarVehiculo()

    def obtener_clientes(self) -> list[dict]:
        return self.servicio.obtener_clientes()

    def registrar_vehiculo(self, id_cliente: int, matricula: str, marca: str, modelo: str, anio: str) -> dict:
        return self.servicio.registrar_vehiculo(id_cliente, matricula, marca, modelo, anio)

