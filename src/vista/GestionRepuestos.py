import os
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5 import uic
from src.controlador.ControladorGestionRepuestos import ControladorGestionRepuestos
from src.vista.AnadirRepuestos import AnadirRepuesto
from src.vista.EliminarRepuesto import EliminarRepuesto
from src.vista.ModificarRepuesto import ModificarRepuesto

class GestionRepuestos(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.controlador = ControladorGestionRepuestos()
        self.setup_ui()
        self.setup_events()
        self.cargar_repuestos()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaRepuestos.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Panel de Repuestos")

        ruta_css = os.path.join(os.path.dirname(__file__),"qss", "estilos.qss")
        with open(ruta_css, "r") as f:
            self.setStyleSheet(f.read())

    def setup_events(self):
        self.btnAnadirRepuestos.clicked.connect(self.AnadirRepuestos)
        self.btnModificarRepuestos.clicked.connect(self.ModificarRepuestos)
        self.btnEliminarRepuestos.clicked.connect(self.EliminarRepuestos)
        self.btnVolver.clicked.connect(self.volver)
    
    def cargar_repuestos(self):
        repuestos = self.controlador.obtener_repuestos()

        self.tablaRepuestos.setRowCount(0)
        self.tablaRepuestos.setColumnCount(4)
        self.tablaRepuestos.setHorizontalHeaderLabels(["Nombre", "Cantidad", "Ubicación", "Precio Unitario"])

        for repuesto in repuestos:
            fila = self.tablaRepuestos.rowCount()
            self.tablaRepuestos.insertRow(fila)
            self.tablaRepuestos.setItem(fila, 0, QTableWidgetItem(repuesto.Nombre))
            self.tablaRepuestos.setItem(fila, 1, QTableWidgetItem(str(repuesto.Cantidad)))
            self.tablaRepuestos.setItem(fila, 2, QTableWidgetItem(repuesto.Ubicacion))
            self.tablaRepuestos.setItem(fila, 3, QTableWidgetItem(f"{repuesto.PrecioUnitario:.2f} €"))
        
        

    def AnadirRepuestos(self):
        self.ventana_anadir = AnadirRepuesto(parent=self)
        self.ventana_anadir.show()
        self.hide()

    def ModificarRepuestos(self):
        self.ventana_anadir = ModificarRepuesto(parent=self)
        self.ventana_anadir.show()
        self.hide()

    def EliminarRepuestos(self):
        self.ventana_anadir = EliminarRepuesto(parent=self)
        self.ventana_anadir.show()
        self.hide()

    def volver(self):
        if self.parent:
            self.parent.show()
        self.close()