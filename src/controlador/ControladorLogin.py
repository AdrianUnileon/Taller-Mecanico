from src.modelo.UserDao.UserDAOJDBC import UserDaoJDBC
import bcrypt

class ControladorLogin:
    def __init__(self):
        self.user_dao = UserDaoJDBC()

    def autenticar_usuario(self, email: str, password: str):
        usuario = self.user_dao.buscar_por_email(email)
        if usuario and bcrypt.checkpw(password.encode('utf-8'), usuario.Contraseña.encode('utf-8')):
            return usuario
        return None
