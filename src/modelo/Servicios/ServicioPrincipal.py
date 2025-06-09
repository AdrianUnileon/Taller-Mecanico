from src.modelo.UserDao.UserDAOJDBC import UserDaoJDBC
import bcrypt

class ServicioPrincipal:
    def __init__(self):
        self.user_dao = UserDaoJDBC()

    def autenticar(self, correo, contraseña):
        usuario = self.user_dao.buscar_por_email(correo)
        if usuario and self.verificar_contraseña(contraseña, usuario.Contraseña):
            return usuario
        return None

    def verificar_contraseña(self, pw_ingresada, pw_hash):
        return bcrypt.checkpw(pw_ingresada.encode('utf-8'), pw_hash.encode('utf-8'))
