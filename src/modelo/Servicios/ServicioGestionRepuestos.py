from src.modelo.UserDao.RepuestoDAO import RepuestoDAO

class ServicioGestionRepuestos:

    def __init__(self):
        self.dao = RepuestoDAO()
      
    def obtener_repuestos(self):
        return self.dao.obtener_todos()