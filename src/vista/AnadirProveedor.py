import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
from src.modelo.UserDao.ProveedorDAO import ProveedorDAO
from src.modelo.vo.ProveedorVO import ProveedorVO

class AnadirProveedor(QMainWindow):
    def __init__(self, parent=None, administrador=None):
        super().__init__(parent)
        self.parent = parent
        self.administrador = administrador
        self.setup_ui()
        self.setup_events()
        self.dao = ProveedorDAO()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaAnadirProveedores.ui") 
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Añadir Proveedor")

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

        nuevo_proveedor = ProveedorVO(
            Nombre=self.Nombre.text().strip(),
            Direccion=self.Direccion.text().strip(),
            Contacto=self.Contacto.text().strip()
        )

        nuevo_id = self.dao.insertar(nuevo_proveedor)
        if nuevo_id:
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