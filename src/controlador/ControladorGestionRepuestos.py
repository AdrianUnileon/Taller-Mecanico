from src.modelo.Servicios.ServicioGestionRepuestos import ServicioGestionRepuestos

class ControladorGestionRepuestos:
    def __init__(self):
        self.servicios = ServicioGestionRepuestos()
      
    def obtener_repuestos(self):
        return self.servicios.obtener_repuestos()

   