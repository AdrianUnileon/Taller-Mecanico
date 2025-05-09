import os
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import uic
from src.modelo.UserDao.UserDAOJDBC import UserDaoJDBC
from src.modelo.vo.UserVO import UserVO
import bcrypt
from src.vista.ClientePanel import ClientePanel
from src.vista.Registro import RegistroWindow
from src.vista.MecanicoPanel import PanelMecanico
from src.vista.RecepcionistaPanel import RecepcionistaPanel

class LoginWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.user_dao = UserDaoJDBC()
        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaLogin.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Inicio de Sesión")

        ruta_qss = os.path.join(os.path.dirname(__file__), "qss", "estilos.qss")
        if os.path.exists(ruta_qss):
            with open(ruta_qss, "r", encoding="utf-8") as f:
                self.setStyleSheet(f.read())

    def setup_events(self):
        self.btnLogin.clicked.connect(self.iniciar_sesion)
        self.btnVolver.clicked.connect(self.volver)

    def volver(self):
        self.show()
        self.close()        

    def iniciar_sesion(self):
        email = self.txtEmail.text().strip()
        password = self.txtPassword.text()

        if not email or not password:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios")
            return

        try:
            usuario = self.user_dao.buscar_por_email(email)
            if usuario and bcrypt.checkpw(password.encode('utf-8'), usuario.Contraseña.encode('utf-8')):
                QMessageBox.information(self, "Éxito", f"Bienvenido, {usuario.Nombre}!")
                self.abrir_panel_principal(usuario)
            else:
                QMessageBox.warning(self, "Error", "Credenciales incorrectas")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al iniciar sesión: {str(e)}")

    def abrir_registro(self):
        self.registro_window = RegistroWindow(self)
        self.registro_window.show()
        self.hide()

    def abrir_panel_principal(self, usuario):
        if usuario.TipoUsuario == "Cliente":
            self.panel_usuario = ClientePanel(self)
        elif usuario.TipoUsuario == "Mecánico":
            self.panel_usuario = PanelMecanico(self)
        elif usuario.TipoUsuario == "Recepcionista":
            self.panel_usuario = RecepcionistaPanel(self)

        self.panel_usuario.show()
        self.hide()  

    def closeEvent(self, event):
        if self.parent:
            self.parent.show()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = LoginWindow()
    ventana.show()
    sys.exit(app.exec_())