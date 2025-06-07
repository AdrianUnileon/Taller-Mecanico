from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5 import uic
import os
from src.controlador.ControladorGestionProveedores import ControladorGestionProveedores
from src.vista.AnadirProveedor import AnadirProveedor
from src.vista.EliminarProveedor import EliminarProveedor
from src.vista.ModificarProveedor import ModificarProveedor

class GestionProveedores(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.controlador = ControladorGestionProveedores()
        self.setup_ui()
        self.setup_events()
        self.cargar_proveedores()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaProveedores.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Gestión de Proveedores")

        ruta_css = os.path.join(os.path.dirname(__file__),"qss", "estilos.qss")
        with open(ruta_css, "r") as f:
            self.setStyleSheet(f.read())

    def setup_events(self):
        self.btnAnadirProveedor.clicked.connect(self.abrir_anadir_proveedor)
        self.btnEliminarProveedor.clicked.connect(self.abrir_eliminar_proveedor)
        self.btnModificarProveedor.clicked.connect(self.abrir_modificar_proveedor)
        self.btnVolver.clicked.connect(self.volver)
    
    def cargar_proveedores(self):
        proveedores = self.controlador.obtener_proveedores()
        self.tablaProveedores.setRowCount(0)
        self.tablaProveedores.setColumnCount(4)
        self.tablaProveedores.setHorizontalHeaderLabels(["IDProveedor", "Nombre", "Contacto", "Direccion"])

        for proveedor in proveedores:
            fila = self.tablaProveedores.rowCount()
            self.tablaProveedores.insertRow(fila)
            self.tablaProveedores.setItem(fila, 0, QTableWidgetItem(str(proveedor.IDProveedor)))
            self.tablaProveedores.setItem(fila, 1, QTableWidgetItem(proveedor.Nombre))
            self.tablaProveedores.setItem(fila, 2, QTableWidgetItem(proveedor.Contacto))
            self.tablaProveedores.setItem(fila, 3, QTableWidgetItem(proveedor.Direccion))


    def abrir_anadir_proveedor(self):
        self.anadir = AnadirProveedor(self)
        self.anadir.show()
        self.hide()

    def abrir_eliminar_proveedor(self):
        self.eliminar = EliminarProveedor(self)
        self.eliminar.show()
        self.hide()

    def abrir_modificar_proveedor(self):
        self.modificar = ModificarProveedor(self)
        self.modificar.show()
        self.hide()

    def volver(self):
        if self.parent:
            self.parent.show()
        self.close()
