import os
import re
import sys
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from PyQt5 import uic
from src.modelo.vo.UserVO import UserVO
from src.modelo.UserDao.UserDAOJDBC import UserDaoJDBC
from src.modelo.UserDao.MecanicoDAO import MecanicoDao
import bcrypt
from src.vista.VentanaCliente import VentanaCliente

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
        self.btnRegistrar.clicked.connect(self.abrir_ventana_rol)
        self.btnCancelar.clicked.connect(self.close)

    def validar_campos(self) -> tuple[bool, str]:
        if not re.match(r'^\d{8}[A-Za-z]$', self.txtDNI.text().strip()):
            return False, "DNI inválido (8 dígitos + letra)"
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', self.txtEmail.text().strip()):
            return False, "Email inválido"
        if len(self.txtPassword.text()) < 6:
            return False, "La contraseña debe tener al menos 6 caracteres"
        if not re.search(r'[A-Za-z]', self.txtPassword.text()):
            return False, "La contraseña debe contener al menos una letra"
        if self.txtPassword.text() != self.txtConfirmPassword.text():
            return False, "Las contraseñas no coinciden"
        return True, ""

    def abrir_ventana_rol(self):
        valid, mensaje = self.validar_campos()
        if not valid:
            QMessageBox.warning(self, "Error", mensaje)
            return

        dni = self.txtDNI.text().strip()
        correo = self.txtEmail.text().strip()

        if self.user_dao.buscar_por_email(correo):
            QMessageBox.warning(self, "Error", "El correo ya está registrado.")
            return

        apellidos = f"{self.txtApellido1.text().strip()} {self.txtApellido2.text().strip()}"
        tipo = self.cmbRol.currentText().strip()

        usuario = UserVO(
            DNI=dni,
            Nombre=self.txtNombre.text().strip(),
            Apellidos=apellidos,
            Correo=correo,
            Contraseña=self.txtPassword.text().strip(),
            TipoUsuario=tipo
        )

        if tipo == "Cliente":
            self.ventana_cliente = VentanaCliente(usuario, parent=self)
            self.ventana_cliente.show()
            self.hide()
        # elif tipo == "Mecánico":
        #     self.ventana_mecanico = VentanaMecanico(usuario, parent=self)
        #     self.ventana_mecanico.show()
        #     self.hide()
        # elif tipo == "Recepcionista":
        #     self.ventana_recepcionista = VentanaRecepcionista(usuario, parent=self)
        #     self.ventana_recepcionista.show()
        #     self.hide()

    def closeEvent(self, event):
        if self.parent:
            self.parent.show()
        event.accept()
