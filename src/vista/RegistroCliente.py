import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic

class RegistroCliente(QMainWindow):
    def __init__(self, parent = None, usuario=None):
        super().__init__(parent)
        self.usuario = usuario
        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaRegistroCliente.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Registro del Cliente")

        if self.usuario:
            self.lblTitulo.setText(f"Bienvenido/a {self.usuario.Nombre}")

    def setup_events(self):
        self.btnRegistrar.clicked.connect(self.registrar_cliente)
        self.btnVolver.clicked.connect(self.volver)

    
    def registrar_cliente(self):
        QMessageBox.information(self, "Éxito", "Registro exitoso!")
        #Incompleto. Falta la logica para el registro del cliente
    
    def volver(self):
        self.parent().show()
        self.close()