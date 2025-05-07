import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
from src.vista.AsignarOrden import AsignarOrdenes

class CrearOrdenRecepcionistaPanel(QMainWindow):
    def __init__(self, parent = None, usuario=None):
        super().__init__(parent)
        self.usuario = usuario
        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaCrearOrden.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Panel del Recepcionista")

        if self.usuario:
            self.lblTitulo.setText(f"Bienvenido/a {self.usuario.Nombre}")
    
    def setup_events(self):
        self.btnAsignarOrden.clicked.connect(self.asignar_orden)
        self.btnVolver.clicked.connect(self.volver)

    def asignar_orden(self):
        self.ordenes_window = AsignarOrdenes(parent=self, usuario=self.usuario)
        self.ordenes_window.show()
        self.hide()
    
    def volver(self):
        self.parent().show()
        self.close()