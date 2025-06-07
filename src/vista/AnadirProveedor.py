import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
from src.controlador.ControladorOperacionesProveedores import ControladorOperacionesProveedores

class AnadirProveedor(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.controlador = ControladorOperacionesProveedores()
        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaAnadirProveedores.ui") 
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Añadir Proveedor")

        ruta_css = os.path.join(os.path.dirname(__file__),"qss", "estilos.qss")
        with open(ruta_css, "r") as f:
            self.setStyleSheet(f.read())

    def setup_events(self):
        self.bntVolver.clicked.connect(self.volver)
        self.btnConfirmar.clicked.connect(self.guardarProveedor)

    def validar_campos(self):
        if not self.Nombre.text().strip():
            QMessageBox.warning(self, "Validación", "El nombre del proveedor es obligatorio.")
            return False
        if not self.Direccion.text().strip():
            QMessageBox.warning(self, "Validación", "La dirección del proveedor es obligatoria.")
            return False
        if not self.Contacto.text().strip():
            QMessageBox.warning(self, "Validación", "El contacto del proveedor es obligatorio.")
            return False
        return True

    def guardarProveedor(self):
        if not self.validar_campos():
            return

        exito = self.controlador.anadir_proveedor(
            self.Nombre.text(),
            self.Contacto.text(),
            self.Direccion.text()
        )

        if exito:
            QMessageBox.information(self, "Éxito", "Proveedor añadido correctamente")
            self.limpiar_campos()
        else:
            QMessageBox.critical(self, "Error", "Hubo un problema al añadir el proveedor.")

    def limpiar_campos(self):
        self.Nombre.clear()
        self.Direccion.clear()
        self.Contacto.clear()

    def volver(self):
        if self.parent:
            self.parent.show()
        self.close()