import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from src.vista.Registro import RegistroWindow
from src.vista.Login import LoginWindow

class PrincipalWindow(QMainWindow):
    def __init__(self, controlador, parent = None):
        super().__init__(parent)
        self.controlador = controlador
        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaPrincipal.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Panel Principal")

        ruta_css = os.path.join(os.path.dirname(__file__),"qss", "estilos.qss")
        with open(ruta_css, "r") as f:
            self.setStyleSheet(f.read())

    def setup_events(self):
        self.btnLogin.clicked.connect(self.abrir_login)
        self.btnRegistro.clicked.connect(self.abrir_registro)
        self.btnSalir.clicked.connect(self.salir_aplicacion)

    def abrir_login(self):
        self.login_window = LoginWindow(parent = self)
        self.login_window.show()
        self.hide()

    def abrir_registro(self):
        self.registro_window = RegistroWindow(parent = self)
        self.registro_window.show()
        self.hide()

    def salir_aplicacion(self):
        self.close()