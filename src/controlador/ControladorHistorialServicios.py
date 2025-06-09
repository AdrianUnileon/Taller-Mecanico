from src.modelo.Servicios.ServicioHistorial import ServicioHistorial
class ControladorHistorialServicios:
    def __init__(self, id_cliente):
        self.id_cliente = id_cliente
        self.servicios = ServicioHistorial(id_cliente)

    def obtener_historial(self):
        return self.servicios.obtener_historial()
    

