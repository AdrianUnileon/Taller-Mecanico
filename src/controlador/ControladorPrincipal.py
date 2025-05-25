'''class ControladorPrincipal():
    def __init__(self, vista, modelo):
        self._vista = vista
        self._modelo = modelo
    
    def login(self, nombre):
        if len (nombre) >3:
            loginVO = loginVO(nombre)
            respuestaLogin = self._modelo.comprobarLogin(loginVO)
            print(respuestaLogin)
        else:
            print("Nombre invalido")

    def mostrarLogin(self):
        self._vista.show()

    def ocultarLogin(self):
        self._vista.hide()

'''
from src.modelo.UserDao.UserDAOJDBC import UserDaoJDBC
from src.vista.Principal import PrincipalWindow
from src.vista.AdministradorPanel import AdministradorPanel

class ControladorPrincipal:
    def __init__(self, admin=False):
        self.user_dao = UserDaoJDBC()
        self.admin = admin
        self.ventana_principal = PrincipalWindow()
        self.ventana_administrador = AdministradorPanel()


    def mostrar_principal(self):
        self.ventana_principal.show()

    def mostrar_administrador(self):
        self.ventana_administrador.show()

    def login(self, correo, contraseña):
        usuario = self.user_dao.buscar_por_email(correo)
        if usuario and self.verificar_contraseña(contraseña, usuario.Contraseña):
            print(f"Login correcto para {usuario.Nombre}")
            return True
        else:
            print("Login fallido")
            return False

    def verificar_contraseña(self, pw_ingresada, pw_hash):
        import bcrypt
        return bcrypt.checkpw(pw_ingresada.encode('utf-8'), pw_hash.encode('utf-8'))
