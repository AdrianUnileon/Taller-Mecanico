from src.modelo.UserDao.UserDAOJDBC import UserDaoJDBC
from src.vista.Principal import PrincipalWindow
from src.vista.AdministradorPanel import AdministradorPanel
from src.vista.Login import LoginWindow
import bcrypt

class ControladorPrincipal:
    def __init__(self, admin=False):
        self.user_dao = UserDaoJDBC()
        self.admin = admin
        self.ventana_login = None
        self.ventana_principal = None
        self.ventana_administrador = None

    def mostrar_administrador(self):
        self.ventana_administrador = AdministradorPanel()
        self.ventana_administrador.show()

    def mostrar_principal(self):
        self.ventana_principal = PrincipalWindow()
        self.ventana_principal.show()

    def mostrar_login(self):
        self.ventana_login = LoginWindow()
        self.ventana_login.show()

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

