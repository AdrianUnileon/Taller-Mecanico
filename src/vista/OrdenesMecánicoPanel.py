'''import os
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5 import uic
from src.modelo.UserDao.OrdenDAOJDBC import OrdenDAOJDBC

class OrdenesAsignadasWindow(QMainWindow):
    def __init__(self, parent=None, usuario=None):
        super().__init__(parent)
        self.usuario = usuario
        self.dao = OrdenDAOJDBC()
        self.ordenes = []

        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaOrdenesAsignadas.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Órdenes Asignadas")

        self.btnActualizarEstado.clicked.connect(self.actualizar_estado)
        self.btnVolver.clicked.connect(self.volver)
        self.cargar_ordenes()

    def cargar_ordenes(self):
        self.ordenes = self.dao.obtener_ordenes_por_mecanico(self.usuario.IDUsuario)
        self.tablaOrdenes.setRowCount(len(self.ordenes))
        self.tablaOrdenes.setColumnCount(3)
        self.tablaOrdenes.setHorizontalHeaderLabels(["Fecha", "Vehículo", "Estado"])

        for i, orden in enumerate(self.ordenes):
            self.tablaOrdenes.setItem(i, 0, QTableWidgetItem(str(orden.fecha)))
            self.tablaOrdenes.setItem(i, 1, QTableWidgetItem(str(orden.id_vehiculo)))
            self.tablaOrdenes.setItem(i, 2, QTableWidgetItem(orden.estado))

    def actualizar_estado(self):
        fila = self.tablaOrdenes.currentRow()
        if fila == -1:
            QMessageBox.warning(self, "Error", "Selecciona una orden para actualizar")
            return

        orden = self.ordenes[fila]
        nuevo_estado = self.cmbNuevoEstado.currentText().strip()

        if not nuevo_estado:
            QMessageBox.warning(self, "Error", "Selecciona un nuevo estado")
            return

        if self.dao.actualizar_estado(orden.id_orden, nuevo_estado):
            QMessageBox.information(self, "Éxito", "Estado actualizado correctamente")
            self.cargar_ordenes()
        else:
            QMessageBox.critical(self, "Error", "Error al actualizar estado")'''

import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic

class OrdenesAsignadasWindow(QMainWindow):
    def __init__(self, parent = None, usuario=None):
        super().__init__(parent)
        self.usuario = usuario
        self.setup_ui()
        self.setup_events()
        
    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaOrdenesAsignadas.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Panel del Mecánico")

        if self.usuario:
            self.lblTitulo.setText(f"Bienvenido/a {self.usuario.Nombre}")
    
    def setup_events(self):
        self.btnActualizarEstado.clicked.connect(self.actualizar_estado)
        self.btnVolver.clicked.connect(self.volver)

    def actualizar_estado(self):
        # Aquí iría la lógica real para actualizar el estado de la orden
        QMessageBox.information(self, "Actualizar Estado", "Tu vehículo está en reparación.")

    def volver(self):
        self.parent().show()
        self.close()
