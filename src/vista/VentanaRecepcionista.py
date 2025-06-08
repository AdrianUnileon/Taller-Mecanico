from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
import os
from src.controlador.ControladorRegistro import ControladorRegistro

class VentanaRecepcionista(QMainWindow):
    def __init__(self, usuario: None, parent=None):
        super().__init__(parent)
        self.usuario = usuario
        self.parent = parent
        self.controlador = ControladorRegistro()
        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaVentanaRecepcionista.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Registro Recepcionista")

        ruta_css = os.path.join(os.path.dirname(__file__),"qss", "estilos.qss")
        with open(ruta_css, "r") as f:
            self.setStyleSheet(f.read())

    def setup_events(self):
        self.btnRegistrar.clicked.connect(self.registrar_cliente)
        self.btnVolver.clicked.connect(self.volver)

    def registrar_cliente(self):
        turno = self.Turno.text().strip()
        if not turno:
            QMessageBox.warning(self, "Campos vacíos", "Por favor completa todos los campos.")
            return
        try:
            exito = self.controlador.registrar_recepcionista(
                self.usuario.IDUsuario, 
                turno
            )

            if exito:
                QMessageBox.information(self, "Éxito", "Registro completado")
                self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

        self.limpiar()

    def limpiar(self):
        self.Turno.clear()

    def volver(self):
        if self.parent:
            self.parent.show()
        self.close()