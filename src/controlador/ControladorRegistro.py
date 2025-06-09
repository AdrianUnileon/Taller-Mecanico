from src.modelo.Servicios.ServicioRegistro import ServicioRegistro

class ControladorRegistro:
    def __init__(self):
        self.servicio = ServicioRegistro()

    def registrar_usuario(self, datos):
        return self.servicio.registrar_usuario(datos)

    def registrar_cliente(self, id_usuario, direccion, contacto):
        return self.servicio.registrar_cliente(id_usuario, direccion, contacto)

    def registrar_mecanico(self, id_usuario, especialidad, fecha):
        return self.servicio.registrar_mecanico(id_usuario, especialidad, fecha)

    def registrar_recepcionista(self, id_usuario, turno):
        return self.servicio.registrar_recepcionista(id_usuario, turno)



