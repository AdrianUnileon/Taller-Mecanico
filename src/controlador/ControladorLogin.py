from src.modelo.UserDao.UserDAOJDBC import UserDaoJDBC
from src.modelo.UserDao.MecanicoDAO import MecanicoDAO
from src.modelo.UserDao.ClienteDAO import ClienteDao
from src.modelo.UserDao.RecepcionistaDAO import RecepcionistaDAO
import bcrypt

class ControladorLogin:
    def __init__(self):
        self.user_dao = UserDaoJDBC()
        self.cliente_dao = ClienteDao()
        self.mecanico_dao = MecanicoDAO()
        self.recepcionista_dao = RecepcionistaDAO()

    def autenticar_usuario(self, email: str, password: str):
        usuario = self.user_dao.buscar_por_email(email)
        if usuario and bcrypt.checkpw(password.encode('utf-8'), usuario.Contraseña.encode('utf-8')):
            return usuario
        return None
    
    def obtener_id_rol(self, usuario):
        if usuario.TipoUsuario.lower() == "cliente":
            return self.cliente_dao.obtener_id_cliente_por_usuario(usuario.IDUsuario)
        elif usuario.TipoUsuario.lower() == "mecánico":
            return self.mecanico_dao.obtener_id_por_usuario(usuario.IDUsuario)
        elif usuario.TipoUsuario.lower() == "recepcionista":
            return self.recepcionista_dao.obtener_id_por_usuario(usuario.IDUsuario)
        return None
