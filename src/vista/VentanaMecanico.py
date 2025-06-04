from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
import os
from src.controlador.ControladorRegistro import ControladorRegistro
from datetime import datetime

class VentanaMecanico(QMainWindow):
    def __init__(self, usuario: None, parent=None):
        super().__init__(parent)
        self.usuario = usuario
        self.parent = parent
        self.controlador = ControladorRegistro()
        self.setup_ui()
        self.setup_events()
    
    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaVentanaMecanico.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Registro Mecanico")

    def setup_events(self):
        self.btnRegistrar.clicked.connect(self.registrar_cliente)
        self.btnVolver.clicked.connect(self.volver)

    def registrar_cliente(self):
        especialidad = self.Especialidad.text().strip()
        fechacontratacion = self.FechaContratacion.text().strip()

        if not especialidad or not fechacontratacion:
            QMessageBox.warning(self, "Campos vacíos", "Por favor completa todos los campos.")
            return

        try:
            Fecha = datetime.strptime(fechacontratacion, "%d/%m/%Y").date()
            
            exito = self.controlador.registrar_mecanico(
                self.usuario.IDUsuario, 
                especialidad, 
                Fecha
            )

            if exito:
                QMessageBox.information(self, "Éxito", "Registro completado")
                self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def volver(self):
        if self.parent:
            self.parent.show()
        self.close()

