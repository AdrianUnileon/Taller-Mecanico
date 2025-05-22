from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
import os
from src.modelo.UserDao.OrdenServicioDAO import OrdenServicioDAO
from PyQt5 import uic
from src.modelo.UserDao.OrdenServicioDAO import OrdenServicioDAO

class VentanaActualizarEstado(QMainWindow):
    def __init__(self, id_orden, parent=None):
        super().__init__(parent)
        self.id_orden = id_orden
        self.orden_dao = OrdenServicioDAO()
        self.setup_ui()
        self.setup_events()
        self.cargar_estados()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaActualizarEstado.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Actualizar Estado de Orden")

    def setup_events(self):
        self.btnActualizar.clicked.connect(self.actualizar_estado)
        self.btnVolver.clicked.connect(self.volver)

    def cargar_estados(self):
        estados = ["En reparación", "Reparada"]
        self.combo_estado.clear()
        self.combo_estado.addItems(estados)

    def actualizar_estado(self):
        nuevo_estado = self.combo_estado.currentText()
        if not nuevo_estado:
            QMessageBox.warning(self, "Estado vacío", "Por favor selecciona un estado.")
            return

        try:
            cursor = self.orden_dao.conn.cursor()
            query = "UPDATE OrdenesServicio SET Estado = %s WHERE IDOrden = %s"
            cursor.execute(query, (nuevo_estado, self.id_orden))
            self.orden_dao.conn.commit()
            cursor.close()

            QMessageBox.information(self, "Éxito", "Estado actualizado correctamente.")
            self.volver()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo actualizar el estado: {e}")

    def volver(self):
        self.close()
        if self.parent():
            self.parent().show()
