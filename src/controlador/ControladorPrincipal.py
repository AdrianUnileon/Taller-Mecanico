from src.modelo.Servicios.ServicioPrincipal import ServicioPrincipal
class ControladorPrincipal:
    def __init__(self, admin=None):
        self.servicio_login = ServicioPrincipal()
        self.admin = admin
        self.view = None

    def iniciar(self):
        from src.vista.Principal import PrincipalWindow  
        self.view = PrincipalWindow(self)
        self.view.show()

    def login(self, correo, contraseña):
        usuario = self.servicio_login.autenticar(correo, contraseña)
        if usuario:
            print(f"Login correcto para {usuario.Nombre}")
            return usuario
        else:
            print("Login fallido")
            return None

