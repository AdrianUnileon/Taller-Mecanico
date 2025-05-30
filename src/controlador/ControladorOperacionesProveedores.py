from src.modelo.UserDao.ProveedorDAO import ProveedorDAO
from src.modelo.vo.ProveedorVO import ProveedorVO

class ControladorOperacionesProveedores:
    def __init__(self):
        self.dao = ProveedorDAO()

    def obtener_proveedores(self):
        return self.dao.obtener_todos()

    def anadir_proveedor(self, nombre, contacto, direccion):
        nuevo = ProveedorVO(Nombre=nombre, Contacto=contacto, Direccion=direccion)
        return self.dao.insertar(nuevo)

    def eliminar_proveedor(self, id_proveedor):
        self.dao.eliminar(id_proveedor)

    def modificar_proveedor(self, id_proveedor, nombre, contacto, direccion):
        self.dao.modificar_proveedor(id_proveedor, nombre, contacto, direccion)