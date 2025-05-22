from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5 import uic
import os
from src.modelo.UserDao.OrdenServicioDAO import OrdenServicioDAO
from src.vista.ActualizarEstado import VentanaActualizarEstado

class VentanaConsultarEstado(QMainWindow):
    def __init__(self, id_mecanico, parent=None):
        super().__init__(parent)
        self.id_mecanico = id_mecanico
        self.orden_dao = OrdenServicioDAO()
        self.setup_ui()
        self.setup_events()
        self.cargar_ordenes()


    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaConsultarEstado.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Órdenes Asignadas")

    def setup_events(self):
        self.btnVolver.clicked.connect(self.volver)
        self.btnActualizarEstado.clicked.connect(self.actualizar_estado)

    def cargar_ordenes(self):
        ordenes = self.orden_dao.obtener_ordenes_por_mecanico(self.id_mecanico)
        self.tableWidget.setRowCount(len(ordenes))
        self.tableWidget.setHorizontalHeaderLabels(["IDOrden", "FechaIngreso", "Descripcion", "Estado", "Vehiculo"])

        for i, orden in enumerate(ordenes):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(orden["IDOrden"])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(orden["FechaIngreso"])))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(orden["Descripcion"]))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(orden["Estado"]))
            vehiculo = f"{orden['Marca']} {orden['Modelo']} ({orden['Matricula']})"
            self.tableWidget.setItem(i, 4, QTableWidgetItem(vehiculo))
            
            

    def actualizar_estado(self):
        fila_seleccionada = self.tableWidget.currentRow()

        if fila_seleccionada == -1:
            QMessageBox.warning(self, "Selecciona una orden", "Por favor selecciona una orden para actualizar.")
            return
        id_orden = int(self.tableWidget.item(fila_seleccionada, 0).text())

        self.actualizar_estado_window = VentanaActualizarEstado(id_orden=id_orden, parent=self)
        self.actualizar_estado_window.show()
        self.hide()

    def volver(self):
        if self.parent():
            self.parent().show()
        self.close()
