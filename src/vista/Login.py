import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
from src.controlador.ControladorLogin import ControladorLogin
from src.vista.ClientePanel import ClientePanel
from src.vista.MecanicoPanel import PanelMecanico
from src.vista.RecepcionistaPanel import RecepcionistaPanel
from src.modelo.UserDao.MecanicoDAO import MecanicoDAO
from src.modelo.UserDao.ClienteDAO import ClienteDao

class LoginWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.controlador = ControladorLogin()
        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaLogin.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Inicio de Sesión")

    def setup_events(self):
        self.btnLogin.clicked.connect(self.iniciar_sesion)
        self.btnVolver.clicked.connect(self.volver)

    def iniciar_sesion(self):
        email = self.txtEmail.text().strip()
        password = self.txtPassword.text()

        if not email or not password:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        usuario = self.controlador.autenticar_usuario(email, password)
        if usuario:
            QMessageBox.information(self, "Éxito", f"Bienvenido, {usuario.Nombre}!")
            self.abrir_panel_principal(usuario)
        else:
            QMessageBox.warning(self, "Error", "Credenciales incorrectas.")

    def abrir_panel_principal(self, usuario):

        if usuario.TipoUsuario.lower() == "cliente":
            cliente_dao = ClienteDao()
            id_cliente = cliente_dao.obtener_id_cliente_por_usuario(usuario.IDUsuario)
            self.panel_usuario = ClientePanel(self, id_cliente)
        elif usuario.TipoUsuario.lower() == "mecánico":
            mecanico_dao = MecanicoDAO()
            id_mecanico = mecanico_dao.obtener_id_por_usuario(usuario.IDUsuario)
            self.panel_usuario = PanelMecanico(self, id_mecanico)
        elif usuario.TipoUsuario.lower() == "recepcionista":
            self.panel_usuario = RecepcionistaPanel(self)

        else:
            QMessageBox.warning(self, "Error", "Tipo de usuario no reconocido.")
            return

        self.panel_usuario.show()
        self.hide()

    def volver(self):
        self.close()
        if self.parent:
            self.parent.show()

    def closeEvent(self, event):
        if self.parent:
            self.parent.show()
        event.accept()
