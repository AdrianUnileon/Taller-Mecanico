from src.modelo.Servicios.ServicioOperacionesProveedores import ServicioOperacionesProveedores

class ControladorOperacionesProveedores:
    def __init__(self):
        self.servicio = ServicioOperacionesProveedores()

    def obtener_proveedores(self) -> list:
        return self.servicio.obtener_proveedores()

    def anadir_proveedor(self, nombre: str, contacto: str, direccion: str) -> bool:
        return self.servicio.anadir_proveedor(nombre, contacto, direccion)

    def eliminar_proveedor(self, id_proveedor: int) -> bool:
        return self.servicio.eliminar_proveedor(id_proveedor)

    def modificar_proveedor(self, id_proveedor: int, nombre: str, contacto: str, direccion: str) -> bool:
        return self.servicio.modificar_proveedor(id_proveedor, nombre, contacto, direccion)