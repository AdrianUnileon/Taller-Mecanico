import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from src.controlador.ControladorEstadoActual import ControladorEstadoActual

class EstadoActual(QMainWindow):
    def __init__(self, parent=None, id_cliente=None):
        super().__init__(parent)
        self.parent = parent
        self.id_cliente = id_cliente
        self.controlador = ControladorEstadoActual()
        self.setup_ui()
        self.setup_events()
        self.cargar_servicios()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaEstadoActual.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Estado Actual del Vehículo")

        ruta_css = os.path.join(os.path.dirname(__file__), "qss", "estilos.qss")
        with open(ruta_css, "r") as f:
            self.setStyleSheet(f.read())

    def setup_events(self):
        self.btnVolver.clicked.connect(self.volver)

    def cargar_servicios(self):
        servicios = self.controlador.obtener_ordenes_actuales(self.id_cliente)
        self.comboEstadoActual.clear()

        for orden in servicios:
            vehiculo = f"{orden['Marca']} {orden['Modelo']} ({orden['Matricula']})"
            descripcion = (
                f"Fecha: {orden['FechaIngreso']} - "
                f"{orden['Descripcion']} - Estado: {orden['Estado']} - Vehículo: {vehiculo}"
            )
            self.comboEstadoActual.addItem(descripcion, orden["IDOrden"])

        if self.comboEstadoActual.count() == 0:
            self.comboEstadoActual.addItem("No hay órdenes actuales", -1)
            self.comboEstadoActual.setEnabled(False)
        else:
            self.comboEstadoActual.setEnabled(True)

    def volver(self):
        if self.parent:
            self.parent.show()
        self.close()
