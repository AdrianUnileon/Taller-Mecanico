import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
from src.controlador.ControladorOperacionesProveedores import ControladorOperacionesProveedores
from src.controlador.ControladorOperacionesRepuestos import ControladorOperacionesRepuestos

class AnadirRepuesto(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.controlador_proveedores = ControladorOperacionesProveedores()
        self.controlador_repuestos = ControladorOperacionesRepuestos()
        self.setup_ui()
        self.setup_events()
        self.cargar_proveedores_en_combo()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaAnadirRepuestos.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Añadir Repuesto")

        ruta_css = os.path.join(os.path.dirname(__file__),"qss", "estilos.qss")
        with open(ruta_css, "r") as f:
            self.setStyleSheet(f.read())

    def setup_events(self):
        self.btnConfirmar.clicked.connect(self.anadir_repuesto)
        self.btnVolver.clicked.connect(self.volver)

    def cargar_proveedores_en_combo(self):
        self.combo_proveedor.clear()
        proveedores = self.controlador_proveedores.obtener_proveedores()
        for proveedor in proveedores:
            self.combo_proveedor.addItem(proveedor.Nombre, proveedor.IDProveedor)

    def anadir_repuesto(self):
        nombre = self.Nombre.text().strip()
        cantidad_text = self.Cantidad.text().strip()
        ubicacion = self.Ubicacion.text().strip()
        precio_text = self.PrecioUnitario.text().strip()
        proveedor_index = self.combo_proveedor.currentIndex()

        if not nombre or not cantidad_text or not ubicacion or not precio_text or proveedor_index == -1:
            QMessageBox.warning(self, "Error", "Completa todos los campos.")
            return

        try:
            cantidad = int(cantidad_text)
            precio = float(precio_text)
        except ValueError:
            QMessageBox.warning(self, "Error", "Cantidad debe ser entero y Precio numérico.")
            return

        id_proveedor = self.combo_proveedor.itemData(proveedor_index)

        exito = self.controlador_repuestos.insertar_repuesto(
            nombre, cantidad, ubicacion, precio, id_proveedor
        )

        if exito:
            QMessageBox.information(self, "Éxito", "Repuesto añadido correctamente.")
            self.limpiar_campos()
        else:
            QMessageBox.critical(self, "Error", "No se pudo añadir el repuesto.")

    def limpiar_campos(self):
        self.Nombre.clear()
        self.Cantidad.clear()
        self.Ubicacion.clear()
        self.PrecioUnitario.clear()
        self.combo_proveedor.setCurrentIndex(0)

    def volver(self):
        if self.parent:
            self.parent.show()
        self.close()
