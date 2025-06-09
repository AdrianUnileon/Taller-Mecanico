from src.modelo.Servicios.ServicioAcceso import ServicioAcceso
from src.vista.VistaAcceso import VistaAcceso
from src.controlador.ControladorAdministrador import ControladorAdministrador
from src.controlador.ControladorPrincipal import ControladorPrincipal

class ControladorAcceso:
    def __init__(self):
        self.servicio = ServicioAcceso()
        self.vista = VistaAcceso()

    def iniciar(self):
        if self._verificar_acceso_administrador():
            controlador = ControladorAdministrador  ()
        else:
            controlador = ControladorPrincipal()
        controlador.iniciar()

    def _verificar_acceso_administrador(self) -> bool:
        if self.vista.confirmar_administrador():
            password = self.vista.pedir_contraseña()
            if self.servicio.verificar_password(password):
                return True
            else:
                self.vista.mostrar_error("Contraseña incorrecta. Acceso denegado.")
        return False
