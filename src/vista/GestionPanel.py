import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from src.vista.GestionRepuestos import GestionRepuestos
from src.vista.GestionProveedores import GestionProveedores

class GestionPanel(QMainWindow):
    def __init__(self, parent=None, administrador = None):
        super().__init__(parent)
        self.parent = parent
        self.administrador = administrador
        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaGestionPanel.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Panel de Gestion")

    def setup_events(self):
        self.btnGestionarRepuestos.clicked.connect(self.gestionarRepuestos)
        self.btnGestionarProveedores.clicked.connect(self.gestionarProveedores)
        self.btnVolver.clicked.connect(self.volver)

    def gestionarProveedores(self):
        self.administrador_orden = GestionProveedores(parent = self, administrador = self.administrador)
        self.administrador_orden.show()
        self.hide()

    def gestionarRepuestos(self):
        self.administrador_orden = GestionRepuestos(parent = self, administrador = self.administrador)
        self.administrador_orden.show()
        self.hide()

    def volver(self):
        if self.parent:
            self.parent.show()
        self.close()