from src.modelo.UserDao.UserDAOJDBC import UserDaoJDBC
from src.modelo.UserDao.MecanicoDAO import MecanicoDAO
from src.modelo.UserDao.ClienteDAO import ClienteDao
from src.modelo.UserDao.RecepcionistaDAO import RecepcionistaDAO
import bcrypt

class ServicioLogin:
    def __init__(self):
        self.user_dao = UserDaoJDBC()
        self.cliente_dao = ClienteDao()
        self.mecanico_dao = MecanicoDAO()
        self.recepcionista_dao = RecepcionistaDAO()

    def autenticar_usuario(self, email: str, password: str):
        try:
            usuario = self.user_dao.buscar_por_email(email)
            if usuario and self._verificar_password(password, usuario.Contraseña):
                return usuario
            return None
        except Exception as e:
            print(f"Error en autenticar_usuario: {e}")
            return None

    def obtener_id_rol(self, usuario) -> int:
        try:
            tipo = usuario.TipoUsuario.lower()
            if tipo == "cliente":
                return self.cliente_dao.obtener_id_cliente_por_usuario(usuario.IDUsuario)
            elif tipo == "mecánico":
                return self.mecanico_dao.obtener_id_por_usuario(usuario.IDUsuario)
            elif tipo == "recepcionista":
                return self.recepcionista_dao.obtener_id_por_usuario(usuario.IDUsuario)
            return None
        except Exception as e:
            print(f"Error en obtener_id_rol: {e}")
            return None

    def _verificar_password(self, password_plano: str, password_hash: str) -> bool:
        try:
            if isinstance(password_hash, str):
                password_hash = password_hash.encode('utf-8')
            return bcrypt.checkpw(password_plano.encode('utf-8'), password_hash)
        except Exception as e:
            print(f"Error en _verificar_password: {e}")
            return False