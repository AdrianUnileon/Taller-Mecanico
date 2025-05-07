import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
from src.vista.OrdenesMecánicoPanel import OrdenesAsignadasWindow

class PanelMecanico(QMainWindow):
    def __init__(self, parent=None, usuario=None):
        super().__init__(parent)
        self.usuario = usuario
        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaPanelMecanico.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Panel del Mecánico")

        if self.usuario:
            self.lblTitulo.setText(f"Bienvenido/a {self.usuario.Nombre}")

    def setup_events(self):
        self.btnConsultarOrdenesAsignadas.clicked.connect(self.abrir_ordenes)
        self.btnCerrarSesion.clicked.connect(self.cerrar_sesion)

    def abrir_ordenes(self):
        self.ordenes_window = OrdenesAsignadasWindow(parent=self, usuario=self.usuario)
        self.ordenes_window.show()
        self.hide()

    def cerrar_sesion(self):
        self.close()
        if self.parent():
            self.parent().show()
