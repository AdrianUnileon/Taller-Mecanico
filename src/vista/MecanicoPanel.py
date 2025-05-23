import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from src.vista.ConsultarEstado import VentanaConsultarEstado
from src.modelo.UserDao.MecanicoDAO import MecanicoDAO

class PanelMecanico(QMainWindow):
    def __init__(self, parent=None, id_mecanico=None):
        super().__init__(parent)
        self.id_mecanico = id_mecanico
        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaPanelMecanico.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Panel del Mecánico")

       

    def setup_events(self):
        self.btnConsultarOrdenesAsignadas.clicked.connect(self.abrir_ordenes)
        self.btnCerrarSesion.clicked.connect(self.cerrar_sesion)

    def abrir_ordenes(self):
        self.ordenes_window = VentanaConsultarEstado(parent=self, id_mecanico=self.id_mecanico)
        self.ordenes_window.show()
        self.hide()

    def cerrar_sesion(self):
        self.close()
        if self.parent():
            self.parent().show()
