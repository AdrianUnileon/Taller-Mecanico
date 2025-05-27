from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5 import uic
from src.modelo.UserDao.RepuestoDAO import RepuestoDAO
import os

class ModificarRepuesto(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.dao = RepuestoDAO()
        self.setup_ui()
        self.setup_events()
        self.cargar_repuestos()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaModificarRepuesto.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Modificar Repuesto")

    def setup_events(self):
        self.tablaRepuestos.itemSelectionChanged.connect(self.cargar_datos_en_campos)
        self.btnConfirmar.clicked.connect(self.modificar_repuesto)
        self.btnVolver.clicked.connect(self.volver)

    def cargar_repuestos(self):
        self.tablaRepuestos.setColumnCount(5)
        self.tablaRepuestos.setHorizontalHeaderLabels(["IDRepuesto", "Nombre", "Cantidad", "Ubicación", "PrecioUnitario"])
        self.tablaRepuestos.setRowCount(0)
        repuestos = self.dao.obtener_todos()
        for repuesto in repuestos:
            fila = self.tablaRepuestos.rowCount()
            self.tablaRepuestos.insertRow(fila)
            self.tablaRepuestos.setItem(fila, 0, QTableWidgetItem(str(repuesto.IDRepuesto)))
            self.tablaRepuestos.setItem(fila, 1, QTableWidgetItem(repuesto.Nombre))
            self.tablaRepuestos.setItem(fila, 2, QTableWidgetItem(repuesto.Cantidad))
            self.tablaRepuestos.setItem(fila, 3, QTableWidgetItem(repuesto.Ubicacion))
            self.tablaRepuestos.setItem(fila, 4, QTableWidgetItem(str(repuesto.PrecioUnitario)))

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
        cantidad_actual = self.tablaRepuestos.item(fila, 2).text()
        ubicacion_actual = self.tablaRepuestos.item(fila, 3).text()
        precio_actual = self.tablaRepuestos.item(fila,4).text()

                           
        nuevo_cantidad = self.Cantidad.text() or cantidad_actual
        nueva_ubicacion = self.Ubicacion.text() or ubicacion_actual
        nuevo_precio = self.PrecioUnitario.text() or precio_actual

        dao = RepuestoDAO()
        dao.modificar_repuesto(id_repuesto, nombre, nuevo_cantidad, nueva_ubicacion, nuevo_precio)

        self.Cantidad.clear()
        self.Ubicacion.clear()
        self.PrecioUnitario.clear()

        self.cargar_repuestos()

        QMessageBox.information(self, "Éxito", "Repuesto modificado correctamente.")

    def volver(self):
        if self.parent:
            self.parent.show()
        self.close()
