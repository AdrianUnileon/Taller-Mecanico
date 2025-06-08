from src.modelo.Servicios.ServicioAcceso import ServicioAcceso
from src.controlador.ControladorAdministrador import ControladorAdministrador
from src.controlador.ControladorPrincipal import ControladorPrincipal

class ControladorAcceso:
    ADMIN_PASSWORD = "admin1234"

    def __init__(self):
        self.ui_service = ServicioAcceso()

    def iniciar(self):
        if self._verificar_acceso_administrador():
            controlador = ControladorAdministrador()
        else:
            controlador = ControladorPrincipal()
        controlador.iniciar()

    def _verificar_acceso_administrador(self) -> bool:
        if self.ui_service.confirmar_administrador():
            password = self.ui_service.pedir_contraseña()
            if password == self.ADMIN_PASSWORD:
                return True
            else:
                self.ui_service.mostrar_error("Contraseña incorrecta. Acceso denegado.")
        return False

