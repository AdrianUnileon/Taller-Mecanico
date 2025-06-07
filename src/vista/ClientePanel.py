import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from src.vista.HistorialServicios import HistorialCliente
from src.vista.EstadoActual import EstadoActual

class ClientePanel(QMainWindow):
    def __init__(self, parent = None, id_cliente = None):
        super().__init__(parent)
        self.id_cliente = id_cliente
        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaCliente.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Panel del Cliente")

        ruta_css = os.path.join(os.path.dirname(__file__),"qss", "estilos.qss")
        with open(ruta_css, "r") as f:
            self.setStyleSheet(f.read())


    def setup_events(self):
        self.btnEstadoVehiculo.clicked.connect(self.consultar_estado_vehiculo)
        self.btnHistorial.clicked.connect(self.consultar_historial_servicios)
        self.btnCerrarSesion.clicked.connect(self.cerrar_sesion)

    def consultar_estado_vehiculo(self):
        self.historial_window = EstadoActual(parent=self, id_cliente=self.id_cliente)
        self.historial_window.show()
        self.hide()

    def consultar_historial_servicios(self):
        self.historial_window = HistorialCliente(parent=self, id_cliente=self.id_cliente)
        self.historial_window.show()
        self.hide()

    def cerrar_sesion(self):
        self.close()
        if self.parent():
            self.parent().show()
