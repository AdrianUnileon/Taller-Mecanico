
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
import os
from src.controlador.ControladorConsultarEstado import ControladorConsultarEstado
from src.vista.ActualizarEstado import VentanaActualizarEstado

class VentanaConsultarEstado(QMainWindow):
    def __init__(self, id_mecanico, parent=None):
        super().__init__(parent)
        self.id_mecanico = id_mecanico
        self.controlador = ControladorConsultarEstado()
        self.setup_ui()
        self.setup_events()
        self.cargar_ordenes()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaConsultarEstado.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Órdenes Asignadas")

        ruta_css = os.path.join(os.path.dirname(__file__), "qss", "estilos.qss")
        with open(ruta_css, "r") as f:
            self.setStyleSheet(f.read())

    def setup_events(self):
        self.btnVolver.clicked.connect(self.volver)
        self.btnActualizarEstado.clicked.connect(self.actualizar_estado)

    def cargar_ordenes(self):
        self.comboOrdenes.clear()
        ordenes = self.controlador.obtener_ordenes_asignadas_por_mecanico(self.id_mecanico)

        for orden in ordenes:
            vehiculo = f"{orden['Marca']} {orden['Modelo']} ({orden['Matricula']})"
            descripcion = (
                f"Fecha: {orden['FechaIngreso']} - "
                f"{orden['Descripcion']} - Vehículo: {vehiculo}"
            )
            self.comboOrdenes.addItem(descripcion, orden["IDOrden"])

        if self.comboOrdenes.count() == 0:
            self.comboOrdenes.addItem("No hay órdenes asignadas", -1)
            self.comboOrdenes.setEnabled(False)
        else:
            self.comboOrdenes.setEnabled(True)

    def actualizar_estado(self):
        id_orden = self.comboOrdenes.currentData()
        if id_orden == -1 or id_orden is None:
            QMessageBox.warning(self, "Selecciona una orden", "Por favor selecciona una orden para actualizar.")
            return

        self.actualizar_estado_window = VentanaActualizarEstado(id_orden=id_orden, parent=self)
        self.actualizar_estado_window.show()
        self.hide()

    def volver(self):
        if self.parent():
            self.parent().show()
        self.close()
