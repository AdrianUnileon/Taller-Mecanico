'''import os
import re
import bcrypt
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
from src.modelo.vo.UserVO import UserVO
from src.modelo.UserDao.UserDAOJDBC import UserDaoJDBC

class RegistroWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.user_dao = UserDaoJDBC()  # Conexión a la BD

    def setup_ui(self):
        # Cargar interfaz .ui
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaRegistro.ui")
        uic.loadUi(ruta_ui, self)
        
        # Configurar eventos
        self.btnRegistrar.clicked.connect(self.registrar_usuario)
        self.btnCancelar.clicked.connect(self.close)

    def validar_campos(self) -> tuple[bool, str]:
        # Validar DNI (8 dígitos + letra)
        if not re.match(r'^\d{8}[A-Za-z]$', self.txtDNI.text().strip()):
            return False, "DNI inválido (ej: 12345678A)"
            
        # Validar nombre y apellidos (solo letras y espacios)
        if not re.match(r'^[A-Za-zÁ-ú\s]+$', self.txtNombre.text().strip()):
            return False, "Nombre solo puede contener letras"
            
        # Validar email
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', self.txtEmail.text().strip()):
            return False, "Email inválido"
            
        # Validar contraseña (mínimo 6 caracteres)
        if len(self.txtPassword.text()) < 6:
            return False, "La contraseña debe tener al menos 6 caracteres"
            
        # Validar que las contraseñas coincidan
        if self.txtPassword.text() != self.txtConfirmPassword.text():
            return False, "Las contraseñas no coinciden"
            
        return True, ""

    def registrar_usuario(self):
        valid, mensaje = self.validar_campos()
        if not valid:
            self.lblMensaje.setText(f"❌ {mensaje}")
            return

        try:
            usuario = UserVO(
                iduser=self.txtDNI.text().strip(),
                nombre=self.txtNombre.text().strip(),
                apellido1=self.txtApellido1.text().strip(),
                apellido2=self.txtApellido2.text().strip(),
                email=self.txtEmail.text().strip(),
                password=self.txtPassword.text(),  # Se hashea en el DAO
                rol=self.cmbRol.currentText()
            )
            
            if self.user_dao.insert(usuario) > 0:
                QMessageBox.information(self, "Éxito", "Usuario registrado correctamente")
                self.close()
            else:
                self.lblMensaje.setText("❌ Error: DNI o email ya existen")
                
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error inesperado: {str(e)}")

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    ventana = RegistroWindow()
    ventana.show()
    app.exec_()'''

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

        # Validar nombre/apellidos
        if not all(re.match(r'^[A-Za-zÁ-ú\s]+$', field.text().strip()) 
                  for field in [self.txtNombre, self.txtApellido1]):
            return False, "Nombre/Apellido solo puede contener letras"

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