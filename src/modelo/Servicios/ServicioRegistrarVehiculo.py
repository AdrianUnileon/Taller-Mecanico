from src.modelo.UserDao.ClienteDAO import ClienteDao
from src.modelo.UserDao.VehiculoDAO import VehiculoDAO
from src.modelo.vo.VehiculoVO import VehiculoVO

class ServicioRegistrarVehiculo:
    def __init__(self):
        self.dao_cliente = ClienteDao()
        self.dao_vehiculo = VehiculoDAO()

    def obtener_clientes(self) -> list[dict]:
        return self.dao_cliente.select()

    def registrar_vehiculo(self, id_cliente: int, matricula: str, marca: str, modelo: str, anio: str) -> dict:
        if not all([id_cliente, matricula, marca, modelo, anio]):
            return {"Error": "Por favor, rellena todos los campos."}

        if self.dao_vehiculo.buscar_por_matricula(matricula):
            return {"Error": "Ya existe un vehículo con esa matrícula."}

        try:
            anio = int(anio)
        except ValueError:
            return {"Error": "El año debe ser un número."}

        vehiculo = VehiculoVO(
            Matricula=matricula,
            Marca=marca,
            Modelo=modelo,
            Anio=anio,
            IDCliente=id_cliente
        )

        id_vehiculo = self.dao_vehiculo.insertar(vehiculo)
        if id_vehiculo > 0:
            return {"Exito": "Vehículo registrado correctamente."}
        else:
            return {"Error": "No se pudo registrar el vehículo."}
