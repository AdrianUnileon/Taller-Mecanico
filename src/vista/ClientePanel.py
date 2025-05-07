import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic

class ClientePanel(QMainWindow):
    def __init__(self, parent = None, usuario=None):
        super().__init__(parent)
        self.usuario = usuario
        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaCliente.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Panel del Cliente")

        if self.usuario:
            self.lblTitulo.setText(f"Bienvenido/a {self.usuario.Nombre}")

    def setup_events(self):
        self.btnEstadoVehiculo.clicked.connect(self.consultar_estado_vehiculo)
        self.btnHistorial.clicked.connect(self.consultar_historial_servicios)
        self.btnCerrarSesion.clicked.connect(self.cerrar_sesion)

    def consultar_estado_vehiculo(self):
        # Aquí iría la lógica real para consultar el estado del vehículo
        QMessageBox.information(self, "Estado del Vehículo", "Tu vehículo está en reparación.")

    def consultar_historial_servicios(self):
        # Aquí iría la lógica real para mostrar el historial de servicios
        QMessageBox.information(self, "Historial de Servicios", "Mostrando historial de servicios...")

    def cerrar_sesion(self):
        self.close()
        if self.parent():
            self.parent().show()
