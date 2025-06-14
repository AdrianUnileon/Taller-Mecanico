import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5 import uic
from src.controlador.ControladorOperacionesProveedores import ControladorOperacionesProveedores

class ModificarProveedor(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.controlador = ControladorOperacionesProveedores()
        self.setup_ui()
        self.setup_events()
        self.cargar_proveedores()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaModificarProveedor.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Modificar Proveedor")

        ruta_css = os.path.join(os.path.dirname(__file__),"qss", "estilos.qss")
        with open(ruta_css, "r") as f:
            self.setStyleSheet(f.read())

    def setup_events(self):
        self.tablaProveedores.itemSelectionChanged.connect(self.cargar_datos_en_campos)
        self.btnConfirmar.clicked.connect(self.modificar_proveedor)
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

    def cargar_datos_en_campos(self):
        fila = self.tablaProveedores.currentRow()
        if fila != -1:
            self.Contacto.setText(self.tablaProveedores.item(fila, 2).text())
            self.Direccion.setText(self.tablaProveedores.item(fila, 3).text())

    def modificar_proveedor(self):
        fila = self.tablaProveedores.currentRow()
        if fila == -1:
            QMessageBox.warning(self, "Advertencia", "Selecciona un proveedor.")
            return

        id_proveedor = int(self.tablaProveedores.item(fila, 0).text())
        nombre = self.tablaProveedores.item(fila, 1).text()
        nuevo_contacto = self.Contacto.text()
        nueva_direccion = self.Direccion.text()

        self.controlador.modificar_proveedor(id_proveedor, nombre, nuevo_contacto, nueva_direccion)

        self.Contacto.clear()
        self.Direccion.clear()

        self.cargar_proveedores()

        QMessageBox.information(self, "Éxito", "Proveedor modificado correctamente.")

    def volver(self):
        if self.parent:
            self.parent.show()
        self.close()

