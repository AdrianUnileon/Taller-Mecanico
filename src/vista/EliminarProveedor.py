import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5 import uic
from src.controlador.ControladorOperacionesProveedores import ControladorOperacionesProveedores

class EliminarProveedor(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.controlador = ControladorOperacionesProveedores()
        self.setup_ui()
        self.setup_events()
        self.cargar_proveedores()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaEliminarProveedores.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Eliminar Proveedores")

        ruta_css = os.path.join(os.path.dirname(__file__),"qss", "estilos.qss")
        with open(ruta_css, "r") as f:
            self.setStyleSheet(f.read())

    def setup_events(self):
        self.btnEliminar.clicked.connect(self.eliminar_proveedor)
        self.btnVolver.clicked.connect(self.volver)

    def cargar_proveedores(self):
        self.tablaProveedores.setColumnCount(4)
        self.tablaProveedores.setHorizontalHeaderLabels(["IDProveedor", "Nombre", "Contacto", "Dirección"])
        self.tablaProveedores.setRowCount(0)
        proveedores = self.controlador.obtener_proveedores()
        for proveedor in proveedores:
            fila = self.tablaProveedores.rowCount()
            self.tablaProveedores.insertRow(fila)
            self.tablaProveedores.setItem(fila, 0, QTableWidgetItem(str(proveedor.IDProveedor)))
            self.tablaProveedores.setItem(fila, 1, QTableWidgetItem(proveedor.Nombre))
            self.tablaProveedores.setItem(fila, 2, QTableWidgetItem(proveedor.Contacto))
            self.tablaProveedores.setItem(fila, 3, QTableWidgetItem(proveedor.Direccion))

    def eliminar_proveedor(self):
        fila = self.tablaProveedores.currentRow()
        if fila == -1:
            QMessageBox.warning(self, "Advertencia", "Debes seleccionar un proveedor.")
            return

        id_proveedor = int(self.tablaProveedores.item(fila, 0).text())

        confirmacion = QMessageBox.question(
            self,
            "Confirmar eliminación",
            f"¿Estás seguro de que deseas eliminar al proveedor con ID {id_proveedor}?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if confirmacion == QMessageBox.Yes:
            self.controlador.eliminar_proveedor(id_proveedor)
            QMessageBox.information(self, "Éxito", "Proveedor eliminado correctamente.")
            self.cargar_proveedores()

    def volver(self):
        if self.parent:
            self.parent.show()
        self.close()