from src.modelo.Servicios.ServicioRegistroCliente import ServicioRegistroCliente

class ControladorRegistroCliente:
    def __init__(self):
        self.servicio = ServicioRegistroCliente()

    def registrar_cliente(self, nombre, apellido1, apellido2, dni, correo, direccion, contacto) -> dict:
        return self.servicio.registrar_cliente(nombre, apellido1, apellido2, dni, correo, direccion, contacto)
