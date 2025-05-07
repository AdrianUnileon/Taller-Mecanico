import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic

class AsignarOrdenes(QMainWindow):
    def __init__(self, parent = None, usuario=None):
        super().__init__(parent)
        self.usuario = usuario
        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaAsignarOrden.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Panel del Recepcionista")

        if self.usuario:
            self.lblTitulo.setText(f"Bienvenido/a {self.usuario.Nombre}")

    def setup_events(self):
        self.btnVolver.clicked.connect(self.volver)
        self.btnAsignar.clicked.connect(self.asignar)
    
    def cargar_datos(self):
        # Cargar órdenes pendientes
        self.cmbOrdenes.clear()
        self.ordenes = self.dao_ordenes.obtener_ordenes_pendientes()
        for orden in self.ordenes:
            texto = f"{orden['IDOrden']} - {orden['NombreCliente']} ({orden['Matricula']})"
            self.cmbOrdenes.addItem(texto, orden['IDOrden'])
        # Cargar mecánicos disponibles
        self.cmbMecanicos.clear()
        self.mecanicos = self.dao_mecanicos.obtener_mecanicos_disponibles()
        for mecanico in self.mecanicos:
            self.cmbMecanicos.addItem(mecanico['Nombre'], mecanico['IDMecanico'])
    
    def asignar(self):
        id_orden = self.cmbOrdenes.currentData()
        id_mecanico = self.cmbMecanicos.currentData()
        if not id_orden or not id_mecanico:
            QMessageBox.warning(self, "Error", "Debe seleccionar una orden y un mecánico.")
            return

        try:
            conn = self.dao_ordenes.createConnection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE OrdenesServicio SET IDMecanico = ?, Estado = 'Asignada' WHERE IDOrden = ?",
                (id_mecanico, id_orden)
            )
            conn.commit()
            QMessageBox.information(self, "Éxito", "Orden asignada correctamente.")
            self.cargar_datos()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo asignar la orden: {e}")
        finally:
            if cursor: cursor.close()
            self.dao_ordenes.closeConnection()
    
    def volver(self):
        self.parent().show()
        self.close()