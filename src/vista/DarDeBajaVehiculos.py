from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5 import uic
import os

from src.controlador.ControladorDarDeBajaVehiculos import ControladorDarDeBajaVehiculos

class DarDeBajaVehiculos(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaDarDeBajaVehiculos.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Dar de baja vehículos")

        self.controlador = ControladorDarDeBajaVehiculos()

        self.configurar_tabla()
        self.cargar_vehiculos()

        self.btnDardeBaja.clicked.connect(self.dar_de_baja)
        self.btnVolver.clicked.connect(self.volver)

    def configurar_tabla(self):
        self.tablVehiculos.setColumnCount(3)
        self.tablVehiculos.setHorizontalHeaderLabels(["ID Vehículo", "Vehículo", "Cliente"])
        self.tablVehiculos.setColumnHidden(0, False)  
        self.tablVehiculos.setEditTriggers(self.tablVehiculos.NoEditTriggers)

    def cargar_vehiculos(self):
        self.tablVehiculos.setRowCount(0)
        vehiculos = self.controlador.obtener_vehiculos_con_clientes()
        for fila, vehiculo in enumerate(vehiculos):
            self.tablVehiculos.insertRow(fila)
            self.tablVehiculos.setItem(fila, 0, QTableWidgetItem(str(vehiculo["IDVehiculo"])))
            descripcion = f"{vehiculo['Marca']} {vehiculo['Modelo']} ({vehiculo['Matricula']})"
            self.tablVehiculos.setItem(fila, 1, QTableWidgetItem(descripcion))
            self.tablVehiculos.setItem(fila, 2, QTableWidgetItem(vehiculo["NombreCliente"]))

    def dar_de_baja(self):
        fila = self.tablVehiculos.currentRow()
        if fila == -1:
            QMessageBox.warning(self, "Atención", "Seleccione un vehículo para dar de baja.")
            return

        id_vehiculo = int(self.tablVehiculos.item(fila, 0).text())
        respuesta = QMessageBox.question(
            self,
            "Confirmar baja",
            "¿Está seguro que desea dar de baja este vehículo?",
            QMessageBox.Yes | QMessageBox.No
        )
        if respuesta == QMessageBox.Yes:
            exito, mensaje = self.controlador.dar_de_baja_vehiculo(id_vehiculo)
            if exito:
                QMessageBox.information(self, "Vehículo dado de baja", mensaje)
                self.cargar_vehiculos()
            else:
                QMessageBox.critical(self, "Error", mensaje)

    def volver(self):
        self.close()
        if self.parent():
            self.parent().show()
