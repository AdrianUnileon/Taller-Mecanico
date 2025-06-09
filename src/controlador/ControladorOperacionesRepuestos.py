from src.modelo.Servicios.ServiciosOperacionesRepuestos import ServicioOperacionesRepuestos

class ControladorOperacionesRepuestos:
    def __init__(self):
        self.servicio = ServicioOperacionesRepuestos()

    def obtener_repuestos(self):
        return self.servicio.obtener_repuestos()

    def insertar_repuesto(self, nombre, cantidad, ubicacion, precio_unitario, id_proveedor):
        return self.servicio.insertar_repuesto(nombre, cantidad, ubicacion, precio_unitario, id_proveedor)

    def modificar_repuesto(self, id_repuesto, nombre, cantidad, ubicacion, precio_unitario):
        return self.servicio.modificar_repuesto(id_repuesto, nombre, cantidad, ubicacion, precio_unitario)

    def eliminar_repuesto(self, id_repuesto):
        return self.servicio.eliminar_repuesto(id_repuesto)
