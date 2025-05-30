import os
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
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

    def setup_events(self):
        self.btnVolver.clicked.connect(self.volver)

    def cargar_servicios(self):
        servicios = self.controlador.obtener_ordenes_actuales(self.id_cliente)

        self.tablaEstadoActual.setRowCount(len(servicios))
        self.tablaEstadoActual.setHorizontalHeaderLabels([
            "IDOrden", "FechaIngreso", "Descripción", "Estado", "Vehículo"
        ])

        for i, orden in enumerate(servicios):
            self.tablaEstadoActual.setItem(i, 0, QTableWidgetItem(str(orden["IDOrden"])))
            self.tablaEstadoActual.setItem(i, 1, QTableWidgetItem(str(orden["FechaIngreso"])))
            self.tablaEstadoActual.setItem(i, 2, QTableWidgetItem(orden["Descripcion"]))
            self.tablaEstadoActual.setItem(i, 3, QTableWidgetItem(orden["Estado"]))

            vehiculo = f"{orden['Marca']} {orden['Modelo']} ({orden['Matricula']})"
            self.tablaEstadoActual.setItem(i, 4, QTableWidgetItem(vehiculo))

    def volver(self):
        if self.parent:
            self.parent.show()
        self.close()
