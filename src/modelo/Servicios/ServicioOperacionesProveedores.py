from src.modelo.UserDao.ProveedorDAO import ProveedorDAO
from src.modelo.vo.ProveedorVO import ProveedorVO

class ServicioOperacionesProveedores:
    def __init__(self):
        self.dao = ProveedorDAO()

    def obtener_proveedores(self) -> list:
        try:
            return self.dao.obtener_todos()
        except Exception as e:
            print(f"Error al obtener proveedores: {e}")
            return []

    def anadir_proveedor(self, nombre: str, contacto: str, direccion: str) -> bool:
        try:
            if not nombre or not contacto:
                raise ValueError("Nombre y contacto son campos obligatorios")
                
            nuevo_proveedor = ProveedorVO(Nombre=nombre, Contacto=contacto, Direccion=direccion)
            return self.dao.insertar(nuevo_proveedor) > 0
        except Exception as e:
            print(f"Error al añadir proveedor: {e}")
            return False

    def eliminar_proveedor(self, id_proveedor: int) -> bool:
        try:
            if not id_proveedor or id_proveedor <= 0:
                raise ValueError("ID de proveedor inválido")
                
            self.dao.eliminar(id_proveedor)
            return True
        except Exception as e:
            print(f"Error al eliminar proveedor: {e}")
            return False

    def modificar_proveedor(self, id_proveedor: int, nombre: str, contacto: str, direccion: str) -> bool:
        try:
            if not id_proveedor or id_proveedor <= 0:
                raise ValueError("ID de proveedor inválido")
            if not nombre or not contacto:
                raise ValueError("Nombre y contacto son campos obligatorios")
                
            return self.dao.modificar_proveedor(id_proveedor, nombre, contacto, direccion)
        except Exception as e:
            print(f"Error al modificar proveedor: {e}")
            return False