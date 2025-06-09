from src.modelo.Servicios.ServicioLogin import ServicioLogin

class ControladorLogin:
    def __init__(self):
        self.servicio = ServicioLogin()

    def autenticar_usuario(self, email: str, password: str):
        return self.servicio.autenticar_usuario(email, password)

    def obtener_id_rol(self, usuario):
        return self.servicio.obtener_id_rol(usuario)