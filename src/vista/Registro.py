import os
import re
import sys
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from PyQt5 import uic
from src.modelo.vo.UserVO import UserVO
from src.modelo.UserDao.UserDAOJDBC import UserDaoJDBC
import bcrypt

class RegistroWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.user_dao = UserDaoJDBC()
        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaRegistro.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Registro de Usuario")

    def setup_events(self):
        self.btnRegistrar.clicked.connect(self.registrar_usuario)
        self.btnCancelar.clicked.connect(self.close)

    def validar_campos(self) -> tuple[bool, str]:
        # Validar DNI
        if not re.match(r'^\d{8}[A-Za-z]$', self.txtDNI.text().strip()):
            return False, "DNI inválido (8 dígitos + letra)"

        # Validar email
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', self.txtEmail.text().strip()):
            return False, "Email inválido"

        # Validar contraseña
        if len(self.txtPassword.text()) < 6:
            return False, "La contraseña debe tener al menos 8 caracteres"
        if not re.search(r'[A-Za-z]', self.txtPassword.text()):
            return False, "La contraseña debe contener al menos una letra"
            
        if self.txtPassword.text() != self.txtConfirmPassword.text():
            return False, "Las contraseñas no coinciden"

        return True, ""

    def registrar_usuario(self):
        valid, mensaje = self.validar_campos()
        if not valid:
            QMessageBox.warning(self, "Error", mensaje)
            return

        try:
            dni = self.txtDNI.text().strip()
            correo = self.txtEmail.text().strip()

            # Comprobar si el usuario ya existe por DNI o Email
            if self.user_dao.buscar_por_email(dni):
                QMessageBox.warning(self, "Error", "El DNI ya está registrado.")
                return
            if self.user_dao.buscar_por_email(correo):
                QMessageBox.warning(self, "Error", "El correo electrónico ya está registrado.")
                return
            # Concatenar apellidos
            apellidos = f"{self.txtApellido1.text().strip()} {self.txtApellido2.text().strip()}".strip()
            
            usuario = UserVO(
                DNI=self.txtDNI.text().strip(),
                Nombre=self.txtNombre.text().strip(),
                Apellidos=apellidos,
                Correo=self.txtEmail.text().strip(),
                Contraseña=self.txtPassword.text(),
                TipoUsuario=self.cmbRol.currentText()
            )

            if self.user_dao.insert(usuario) > 0:
                QMessageBox.information(self, "Éxito", "Registro exitoso!")
                self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error: {str(e)}")


    def closeEvent(self, event):
        if self.parent:
            self.parent.show()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = RegistroWindow()
    ventana.show()
    sys.exit(app.exec_())