import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
from src.controlador.ControladorRegistro import ControladorRegistro
from src.vista.VentanaCliente import VentanaCliente
from src.vista.VentanaMecanico import VentanaMecanico
from src.vista.VentanaRecepcionista import VentanaRecepcionista

class RegistroWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.parent = parent
        self.controlador = ControladorRegistro()
        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaRegistro.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Registro de Usuario")

    def setup_events(self):
        self.btnRegistrar.clicked.connect(self.registrar_usuario)
        self.btnCancelar.clicked.connect(self.close)

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

        valido, mensaje = self.controlador.validar_campos(datos)
        if not valido:
            QMessageBox.warning(self, "Error", mensaje)
            return

        exito, resultado = self.controlador.registrar_usuario(datos)
        if not exito:
            QMessageBox.warning(self, "Error", resultado)
            return

        usuario = resultado
        QMessageBox.information(self, "Registro Exitoso", f"{usuario.Nombre}, tu cuenta fue creada.")

        if usuario.TipoUsuario.lower() == "cliente":
            self.ventana = VentanaCliente(usuario, parent=self)
        elif usuario.TipoUsuario.lower() == "mecánico":
            self.ventana = VentanaMecanico(usuario, parent=self)
        elif usuario.TipoUsuario.lower() == "recepcionista":
            self.ventana = VentanaRecepcionista(usuario, parent=self)
        else:
            QMessageBox.warning(self, "Error", "Tipo de usuario desconocido.")
            return

        self.ventana.show()
        self.hide()

    def closeEvent(self, event):
        if self.parent:
            self.parent.show()
        event.accept()
