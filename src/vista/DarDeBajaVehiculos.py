from PyQt5.QtWidgets import QMainWindow, QMessageBox, QComboBox
from PyQt5 import uic
import os

from src.controlador.ControladorDarDeBajaVehiculos import ControladorDarDeBajaVehiculos

class DarDeBajaVehiculos(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controlador = ControladorDarDeBajaVehiculos()

        self.setup_ui()
        self.setup_events()
        self.cargar_vehiculos()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaDarDeBajaVehiculos.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Dar de baja vehículos")

        ruta_css = os.path.join(os.path.dirname(__file__), "qss", "estilos.qss")
        with open(ruta_css, "r") as f:
            self.setStyleSheet(f.read())

    def setup_events(self):
        self.btnDardeBaja.clicked.connect(self.dar_de_baja)
        self.btnVolver.clicked.connect(self.volver)

    def cargar_vehiculos(self):
        self.comboVehiculos.clear()
        self.vehiculos_list = self.controlador.obtener_vehiculos_sin_ordenes()
        for vehiculo in self.vehiculos_list:
            descripcion = (f"ID: {vehiculo['IDVehiculo']} - "
                           f"{vehiculo['Marca']} {vehiculo['Modelo']} "
                           f"({vehiculo['Matricula']}) - Cliente: {vehiculo['NombreCliente']}")
            self.comboVehiculos.addItem(descripcion, vehiculo['IDVehiculo'])

        if self.comboVehiculos.count() == 0:
            self.comboVehiculos.addItem("No hay vehículos disponibles", -1)
            self.comboVehiculos.setEnabled(False)
        else:
            self.comboVehiculos.setEnabled(True)

    def dar_de_baja(self):
        id_vehiculo = self.comboVehiculos.currentData()
        if id_vehiculo == -1 or id_vehiculo is None:
            QMessageBox.warning(self, "Atención", "Seleccione un vehículo válido para dar de baja.")
            return

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
        if self.parent():
            self.parent().show()
        self.close()