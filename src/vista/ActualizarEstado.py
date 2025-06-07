from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
import os
from src.controlador.ControladorActualizarEstado import ControladorActualizarEstado

class VentanaActualizarEstado(QMainWindow):
    def __init__(self, id_orden, parent=None):
        super().__init__(parent)
        self.id_orden = id_orden
        self.controlador = ControladorActualizarEstado()
        self.setup_ui()
        self.setup_events()
        self.cargar_estados()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaActualizarEstado.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Actualizar Estado de Orden")

        ruta_css = os.path.join(os.path.dirname(__file__),"qss", "estilos.qss")
        with open(ruta_css, "r") as f:
            self.setStyleSheet(f.read())

    def setup_events(self):
        self.btnActualizar.clicked.connect(self.actualizar_estado)
        self.btnVolver.clicked.connect(self.volver)

    def cargar_estados(self):
        estados = ["Asignada", "Reparada"]
        self.combo_estado.clear()
        self.combo_estado.addItems(estados)

    def actualizar_estado(self):
        nuevo_estado = self.combo_estado.currentText()
        costo_reparacion = self.CosteReparacion.text()

        if not nuevo_estado:
            QMessageBox.warning(self, "Estado vacío", "Por favor selecciona un estado.")
            return

        if nuevo_estado == "Reparada":
            if not costo_reparacion.strip():
                QMessageBox.warning(self, "Costo vacío", "Debes ingresar el coste de la reparación.")
                return
            try:
                costo_reparacion = float(costo_reparacion)
            except ValueError:
                QMessageBox.warning(self, "Formato inválido", "El coste debe ser un número válido.")
                return
        else:
            costo_reparacion = None

        exito = self.controlador.actualizar_estado_orden(self.id_orden, nuevo_estado, costo_reparacion)
        if exito:
            QMessageBox.information(self, "Éxito", "Estado actualizado correctamente.")
            self.volver()
        else:
            QMessageBox.critical(self, "Error", "No se pudo actualizar el estado.")

    def volver(self):
        self.close()
        if self.parent():
            self.parent().show()
