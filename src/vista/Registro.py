import os
import re
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
from src.controlador.ControladorRegistro import ControladorRegistro
from src.vista.VentanaCliente import VentanaCliente
from src.vista.VentanaMecanico import VentanaMecanico
from src.vista.VentanaRecepcionista import VentanaRecepcionista
from src.vista.AdministradorPanel import AdministradorPanel

class RegistroWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.controlador = ControladorRegistro()
        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaRegistro.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Registro de Usuario")

        ruta_css = os.path.join(os.path.dirname(__file__), "qss", "estilos.qss")
        with open(ruta_css, "r") as f:
            self.setStyleSheet(f.read())

    def setup_events(self):
        self.btnRegistrar.clicked.connect(self.registrar_usuario)
        self.btnCancelar.clicked.connect(self.close)

    def validar_campos(self, datos):
        if not re.match(r'^\d{8}[A-Za-z]$', datos['dni']):
            return False, "DNI inválido. Debe tener 8 dígitos seguidos de una letra."
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', datos['correo']):
            return False, "Correo electrónico inválido."
        if len(datos['password']) < 6:
            return False, "La contraseña debe tener al menos 6 caracteres."
        if not re.search(r'[A-Za-z]', datos['password']):
            return False, "La contraseña debe contener letras."
        if datos['password'] != datos['confirm_password']:
            return False, "Las contraseñas no coinciden."
        return True, ""

    def registrar_usuario(self):
        datos = {
            "dni": self.txtDNI.text().strip(),
            "nombre": self.txtNombre.text().strip(),
            "apellidos": f"{self.txtApellido1.text().strip()} {self.txtApellido2.text().strip()}",
            "correo": self.txtEmail.text().strip(),
            "password": self.txtPassword.text(),
            "confirm_password": self.txtConfirmPassword.text(),
            "tipo": self.cmbRol.currentText()
        }

        valido, mensaje = self.validar_campos(datos)
        if not valido:
            QMessageBox.warning(self, "Validación", mensaje)
            return

        exito, resultado = self.controlador.registrar_usuario(datos)
        if not exito:
            QMessageBox.warning(self, "Error", resultado)
            return

        usuario = resultado
        QMessageBox.information(self, "Registro Exitoso", f"{usuario.Nombre}, tu cuenta fue creada.")

        tipo_usuario = usuario.TipoUsuario.lower()
        if tipo_usuario == "cliente":
            self.ventana = VentanaCliente(usuario, parent=self)
        elif tipo_usuario == "mecánico":
            self.ventana = VentanaMecanico(usuario, parent=self)
        elif tipo_usuario == "recepcionista":
            self.ventana = VentanaRecepcionista(usuario, parent=self)
        elif tipo_usuario == "administrador": 
            self.ventana = AdministradorPanel(usuario, parent=self)
        else:
            QMessageBox.warning(self, "Error", "Tipo de usuario desconocido.")
            return

        self.ventana.show()
        self.limpiar_campos()
        self.hide()

    def limpiar_campos(self):
        self.txtDNI.clear()
        self.txtNombre.clear()
        self.txtApellido1.clear()
        self.txtApellido2.clear()
        self.txtEmail.clear()
        self.txtPassword.clear()
        self.txtConfirmPassword.clear()
        self.cmbRol.clear()

    def closeEvent(self, event):
        if self.parent:
            self.parent.show()
        event.accept()
