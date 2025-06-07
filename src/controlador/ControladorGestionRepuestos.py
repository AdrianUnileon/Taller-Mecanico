from src.modelo.UserDao.RepuestoDAO import RepuestoDAO

class ControladorGestionRepuestos:
    def __init__(self):
        self.dao = RepuestoDAO()
      
    def obtener_repuestos(self):
        return self.dao.obtener_todos()

   