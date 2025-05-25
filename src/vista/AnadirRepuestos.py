import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
from src.modelo.UserDao.ProveedorDAO import ProveedorDAO
from src.modelo.UserDao.RepuestoDAO import RepuestoDAO
from src.modelo.vo.RepuestoVO import RepuestoVO

class AnadirRepuesto(QMainWindow):
    def __init__(self, parent=None, administrador=None):
        super().__init__(parent)
        self.parent = parent
        self.administrador = administrador
        self.dao_repuesto = RepuestoDAO()
        self.dao_proveedor = ProveedorDAO()

        self.setup_ui()
        self.setup_events()
        self.cargar_proveedores()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaAnadirRepuestos.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Añadir Repuestos")

    def setup_events(self):
        self.btnConfirmar.clicked.connect(self.guardar_repuesto)
        self.btnVolver.clicked.connect(self.volver)

    def cargar_proveedores(self):
        proveedores = self.dao_proveedor.obtener_todos()
        self.combo_proveedor.clear()
        self.lista_proveedores = proveedores
        for proveedor in proveedores:
            self.combo_proveedor.addItem(proveedor.Nombre, proveedor.IDProveedor)

    def validar_campos(self):
        if not self.Nombre.text().strip():
            QMessageBox.warning(self, "Validación", "El nombre del repuesto es obligatorio.")
            return False
        if not self.Cantidad.text().strip().isdigit():
            QMessageBox.warning(self, "Validación", "La cantidad debe ser un número entero.")
            return False
        if not self.PrecioUnitario.text().strip().replace('.', '', 1).isdigit():
            QMessageBox.warning(self, "Validación", "El precio debe ser un número válido.")
            return False
        if not self.Ubicacion.text().strip():
            QMessageBox.warning(self, "Validación", "La ubicación es obligatoria.")
            return False
        if self.combo_proveedor.currentIndex() == -1:
            QMessageBox.warning(self, "Validación", "Debe seleccionar un proveedor.")
            return False
        return True

    def guardar_repuesto(self):
        if not self.validar_campos():
            return

        repuesto = RepuestoVO(
            Nombre=self.Nombre.text().strip(),
            Cantidad=int(self.Cantidad.text().strip()),
            PrecioUnitario=float(self.PrecioUnitario.text().strip()),
            Ubicacion=self.Ubicacion.text().strip(),
            IDProveedor=self.combo_proveedor.currentData()
        )

        id_repuesto = self.dao_repuesto.insertar(repuesto)
        if id_repuesto:
            QMessageBox.information(self, "Éxito", "Repuesto añadido correctamente.")
            self.limpiar_campos()
        else:
            QMessageBox.critical(self, "Error", "Hubo un problema al añadir el repuesto.")

    def limpiar_campos(self):
        self.Nombre.clear()
        self.Cantidad.clear()
        self.PrecioUnitario.clear()
        self.Ubicacion.clear()
        self.combo_proveedor.setCurrentIndex(0)

    def volver(self):
        if self.parent:
            self.parent.show()
        self.close()
