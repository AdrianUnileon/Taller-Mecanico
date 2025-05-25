import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5 import uic
from src.modelo.UserDao.RepuestoDAO import RepuestoDAO

class EliminarRepuesto(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setup_ui()
        self.setup_events()
        self.dao = RepuestoDAO()
        self.cargar_repuestos()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaEliminarRepuesto.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Eliminar Repuesto")

    def setup_events(self):
        self.btnEliminar.clicked.connect(self.eliminar_repuesto)
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

    def eliminar_repuesto(self):
        fila = self.tablaRepuestos.currentRow()
        if fila == -1:
            QMessageBox.warning(self, "Advertencia", "Debes seleccionar un repuesto.")
            return

        id_repuesto = int(self.tablaRepuestos.item(fila, 0).text())

        confirmacion = QMessageBox.question(
            self,
            "Confirmar eliminación",
            f"¿Estás seguro de que deseas eliminar al repuesto con ID {id_repuesto}?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if confirmacion == QMessageBox.Yes:
            self.dao.eliminar(id_repuesto)
            QMessageBox.information(self, "Éxito", "Repuesto eliminado correctamente.")
            self.cargar_repuestos()

    def volver(self):
        if self.parent:
            self.parent.show()
        self.close()
