from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
import os
from src.controlador.ControladorRegistroCliente import ControladorRegistroCliente

class RegistrarCliente(QMainWindow):
    def __init__(self, parent=None, usuario=None):
        super().__init__(parent)
        self.controlador = ControladorRegistroCliente()
        self.usuario = usuario
        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaRegistroCliente.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Registro del Cliente")

        ruta_css = os.path.join(os.path.dirname(__file__),"qss", "estilos.qss")
        with open(ruta_css, "r") as f:
            self.setStyleSheet(f.read())

    def setup_events(self):
        self.btnRegistrar.clicked.connect(self.registrar_cliente)
        self.btnVolver.clicked.connect(self.volver)

    def registrar_cliente(self):
        nombre = self.Nombre.text().strip()
        apellido1 = self.Apellido1.text().strip()
        apellido2 = self.Apellido2.text().strip()
        dni = self.DNI.text().strip()
        contacto = self.Telefono.text().strip()
        correo = self.Correo.text().strip()
        direccion = self.Direccion.text().strip()

        exito = self.controlador.registrar_cliente(
            nombre, apellido1, apellido2, dni, correo, direccion, contacto
        )

        if exito:
            QMessageBox.information(self, "Éxito", "Cliente registrado correctamente.")
        else:
            QMessageBox.warning(self, "Error", "Se ha producido un error.")

    def volver(self):
        self.parent().show()
        self.close()
