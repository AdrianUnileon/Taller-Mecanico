from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
import os

from src.controlador.ControladorAsignarOrden import ControladorAsignarOrden

class AsignarOrden(QMainWindow):
    def __init__(self, parent=None, usuario = None):
        super().__init__(parent)
        self.usuario = usuario
        self.controller = ControladorAsignarOrden()
        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaAsignarOrden.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Asignar Orden a Mecánico")
        self.cargar_ordenes_pendientes()
        self.cargar_mecanicos()

        ruta_css = os.path.join(os.path.dirname(__file__),"qss", "estilos.qss")
        with open(ruta_css, "r") as f:
            self.setStyleSheet(f.read())

    def setup_events(self):
        self.btnAsignar.clicked.connect(self.asignar)
        self.btnVolver.clicked.connect(self.volver)

    def cargar_ordenes_pendientes(self):
        self.comboOrdenes.clear()
        ordenes = self.controller.obtener_ordenes_pendientes()
        for orden in ordenes:
            texto = f"{orden.IDOrden} - {orden.Descripcion[:30]}"
            self.comboOrdenes.addItem(texto, orden.IDOrden)

    def cargar_mecanicos(self):
        self.comboMecanicos.clear()
        mecanicos = self.controller.obtener_mecanicos_disponibles()
        for m in mecanicos:
            self.comboMecanicos.addItem(f"{m['Nombre']} {m['Apellidos']}", m['IDMecanico'])

    def asignar(self):
        id_orden = self.comboOrdenes.currentData()
        id_mecanico = self.comboMecanicos.currentData()

        if not id_orden or not id_mecanico:
            QMessageBox.warning(self, "Error", "Debes seleccionar una orden y un mecánico.")
            return

        resultado = self.controller.asignar_orden(id_orden, id_mecanico)
        if resultado:
            QMessageBox.information(self, "Éxito", "Orden asignada correctamente.")
            self.cargar_ordenes_pendientes()
        else:
            QMessageBox.critical(self, "Error", "No se pudo asignar la orden.")

    def volver(self):
        self.parent().show()
        self.close()
