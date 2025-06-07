from src.modelo.UserDao.UserDAOJDBC import UserDaoJDBC
import bcrypt

class ControladorPrincipal:
    def __init__(self, admin = None):
        self.user_dao = UserDaoJDBC()
        self.admin = admin
        self.view = None

    def iniciar(self):
        from src.vista.Principal import PrincipalWindow  
        self.view = PrincipalWindow(self)
        self.view.show()

    def login(self, correo, contraseña):
        usuario = self.user_dao.buscar_por_email(correo)
        if usuario and self.verificar_contraseña(contraseña, usuario.Contraseña):
            print(f"Login correcto para {usuario.Nombre}")
            return usuario
        else:
            print("Login fallido")
            return None

    def verificar_contraseña(self, pw_ingresada, pw_hash):
        return bcrypt.checkpw(pw_ingresada.encode('utf-8'), pw_hash.encode('utf-8'))
