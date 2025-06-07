import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5 import uic
from src.controlador.ControladorOperacionesRepuestos import ControladorOperacionesRepuestos

class ModificarRepuesto(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.controlador = ControladorOperacionesRepuestos()
        self.setup_ui()
        self.setup_events()
        self.cargar_repuestos()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaModificarRepuesto.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Modificar Repuesto")

        ruta_css = os.path.join(os.path.dirname(__file__),"qss", "estilos.qss")
        with open(ruta_css, "r") as f:
            self.setStyleSheet(f.read())

    def setup_events(self):
        self.tablaRepuestos.itemSelectionChanged.connect(self.cargar_datos_en_campos)
        self.btnConfirmar.clicked.connect(self.modificar_repuesto)
        self.btnVolver.clicked.connect(self.volver)

    def cargar_repuestos(self):
        self.tablaRepuestos.setRowCount(0)
        self.tablaRepuestos.setColumnCount(6)
        self.tablaRepuestos.setHorizontalHeaderLabels([
            "IDRepuesto", "Nombre", "Cantidad", "Ubicación", "Precio Unitario", "IDProveedor"
        ])

        repuestos = self.controlador.obtener_repuestos()
        for repuesto in repuestos:
            fila = self.tablaRepuestos.rowCount()
            self.tablaRepuestos.insertRow(fila)
            self.tablaRepuestos.setItem(fila, 0, QTableWidgetItem(str(repuesto.IDRepuesto)))
            self.tablaRepuestos.setItem(fila, 1, QTableWidgetItem(repuesto.Nombre))
            self.tablaRepuestos.setItem(fila, 2, QTableWidgetItem(str(repuesto.Cantidad)))
            self.tablaRepuestos.setItem(fila, 3, QTableWidgetItem(repuesto.Ubicacion))
            self.tablaRepuestos.setItem(fila, 4, QTableWidgetItem(str(repuesto.PrecioUnitario)))
            self.tablaRepuestos.setItem(fila, 5, QTableWidgetItem(str(repuesto.IDProveedor)))

    def cargar_datos_en_campos(self):
        fila = self.tablaRepuestos.currentRow()
        if fila != -1:
            self.Cantidad.setText(self.tablaRepuestos.item(fila, 2).text())
            self.Ubicacion.setText(self.tablaRepuestos.item(fila, 3).text())
            self.PrecioUnitario.setText(self.tablaRepuestos.item(fila, 4).text())

    def modificar_repuesto(self):
        fila = self.tablaRepuestos.currentRow()
        if fila == -1:
            QMessageBox.warning(self, "Advertencia", "Selecciona un repuesto.")
            return

        id_repuesto = int(self.tablaRepuestos.item(fila, 0).text())
        nombre = self.tablaRepuestos.item(fila, 1).text()
        try:
            nueva_cantidad = int(self.Cantidad.text())
            nueva_ubicacion = self.Ubicacion.text()
            nuevo_precio = float(self.PrecioUnitario.text())

            self.controlador.modificar_repuesto(id_repuesto, nombre, nueva_cantidad, nueva_ubicacion, nuevo_precio)

            QMessageBox.information(self, "Éxito", "Repuesto modificado correctamente.")
            self.cargar_repuestos()
            self.limpiar_campos()
        except ValueError:
            QMessageBox.warning(self, "Error", "Cantidad debe ser entero y Precio unitario un número válido.")

    def limpiar_campos(self):
        self.Cantidad.clear()
        self.Ubicacion.clear()
        self.PrecioUnitario.clear()

    def volver(self):
        if self.parent:
            self.parent.show()
        self.close()
