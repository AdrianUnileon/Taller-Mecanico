from src.modelo.Servicios.ServicioGestionProveedores import ServicioGestionProveedores

class ControladorGestionProveedores:
    def __init__(self):
        self.servicio = ServicioGestionProveedores()

    def obtener_proveedores(self):
        return self.servicio.obtener_proveedores()
