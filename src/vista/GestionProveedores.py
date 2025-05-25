import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5 import uic
from src.modelo.UserDao.ProveedorDAO import ProveedorDAO
from src.vista.AnadirProveedor import AnadirProveedor 
from src.vista.EliminarProveedor import EliminarProveedor 
from src.vista.ModificarProveedor import ModificarProveedor

class GestionProveedores(QMainWindow):
    def __init__(self, parent=None, administrador=None):
        super().__init__(parent)
        self.parent = parent
        self.administrador = administrador
        self.setup_ui()
        self.setup_events()
        self.cargar_proveedores()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaProveedores.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Panel de Proveedores")

    def setup_events(self):
        self.btnAnadirProveedor.clicked.connect(self.anadir_proveedor)
        self.btnModificarProveedor.clicked.connect(self.ModificarProveedores)
        self.btnEliminarProveedor.clicked.connect(self.EliminarProveedores)
        self.btnVolver.clicked.connect(self.volver)

    def cargar_proveedores(self):
        dao = ProveedorDAO()
        proveedores = dao.obtener_todos()
        self.tablaProveedores.setColumnCount(4)
        self.tablaProveedores.setHorizontalHeaderLabels(["IDProveedor","Nombre", "Contacto", "Direccion"])
        self.tablaProveedores.setRowCount(0)

        for proveedor in proveedores:
            fila = self.tablaProveedores.rowCount()
            self.tablaProveedores.insertRow(fila)
            self.tablaProveedores.setItem(fila, 0, QTableWidgetItem(proveedor.IDProveedor))
            self.tablaProveedores.setItem(fila, 1, QTableWidgetItem(proveedor.Nombre))
            self.tablaProveedores.setItem(fila, 2, QTableWidgetItem(proveedor.Contacto))
            self.tablaProveedores.setItem(fila, 3, QTableWidgetItem(proveedor.Direccion))



    def anadir_proveedor(self):
        self.ventana_anadir = AnadirProveedor(parent=self, administrador=self.administrador)
        self.ventana_anadir.show()
        self.hide()

    def ModificarProveedores(self):
        self.ventana_anadir = ModificarProveedor(parent=self)
        self.ventana_anadir.show()
        self.hide()

    def EliminarProveedores(self):
        self.ventana_anadir = EliminarProveedor(parent=self)
        self.ventana_anadir.show()
        self.hide()

    def volver(self):
        if self.parent:
            self.parent.show()
        self.close()
