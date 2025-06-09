from src.modelo.UserDao.ProveedorDAO import ProveedorDAO

class ServicioGestionProveedores:

    def __init__(self):
        self.dao = ProveedorDAO()

    def obtener_proveedores(self):
        return self.dao.obtener_todos()