import os
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5 import uic
from src.controlador.ControladorHistorialServicios import ControladorHistorialServicios

class HistorialCliente(QMainWindow):
    def __init__(self, id_cliente, parent=None):
        super().__init__(parent)
        self.id_cliente = id_cliente
        self.controlador = ControladorHistorialServicios(self.id_cliente)
        self.parent = parent
        self.setup_ui()
        self.setup_events()
        self.cargar_historial()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaHistorialServicios.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Historial de Servicios")

        ruta_css = os.path.join(os.path.dirname(__file__),"qss", "estilos.qss")
        with open(ruta_css, "r") as f:
            self.setStyleSheet(f.read())

    def setup_events(self):
        self.btnVolver.clicked.connect(self.volver)

    def cargar_historial(self):
        historial = self.controlador.obtener_historial()
        self.mostrar_servicios(historial)

    def mostrar_servicios(self, lista_servicios):
        self.tablaServicios.setRowCount(len(lista_servicios))
        self.tablaServicios.setHorizontalHeaderLabels(["IDOrden", "FechaIngreso", "Descripcion", "Estado", "Vehículo"])
        for i, orden in enumerate(lista_servicios):
            self.tablaServicios.setItem(i, 0, QTableWidgetItem(str(orden["IDOrden"])))
            self.tablaServicios.setItem(i, 1, QTableWidgetItem(str(orden["FechaIngreso"])))
            self.tablaServicios.setItem(i, 2, QTableWidgetItem(orden["Descripcion"]))
            self.tablaServicios.setItem(i, 3, QTableWidgetItem(orden["Estado"]))
            vehiculo = f"{orden['Marca']} {orden['Modelo']} ({orden['Matricula']})"
            self.tablaServicios.setItem(i, 4, QTableWidgetItem(vehiculo))

    def volver(self):
        if self.parent:
            self.parent.show()
        self.close()
