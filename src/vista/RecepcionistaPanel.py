import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
from src.vista.CrearOrdenRecepcionista import CrearOrdenRecepcionistaPanel

class RecepcionistaPanel(QMainWindow):
    def __init__(self, parent = None, usuario=None):
        super().__init__(parent)
        self.usuario = usuario
        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaRecepcionista.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Panel del Recepcionista")

        if self.usuario:
            self.lblTitulo.setText(f"Bienvenido/a {self.usuario.Nombre}")
    
    def setup_events(self):
        self.btnRegistrarCliente.clicked.connect(self.registrar_cliente)
        self.btnCrearOrdenServicio.clicked.connect(self.crear_orden_servicio)
        self.btnRegistrarVehiculo.clicked.connect(self.registrar_vehiculo)
        self.btnEmitirFacturas.clicked.connect(self.emitir_facturas)
        self.btnCerrarSesion.clicked.connect(self.cerrar_sesion)

    def registrar_cliente(self):
        # Aquí iría la lógica real para registrar clientes
        QMessageBox.information(self, "Registro de cliente", "Tu vehículo está en reparación.")
    
    def crear_orden_servicio(self):
        # Aquí iría la lógica real para crear ordenes de servicio
        self.ordenes_window = CrearOrdenRecepcionistaPanel(parent=self, usuario=self.usuario)
        self.ordenes_window.show()
        self.hide()
    
    def registrar_vehiculo(self):
        # Aquí iría la lógica real para registrar vehículos
        QMessageBox.information(self, "Registro del vehículo", "Tu vehículo está en reparación.")
    
    def emitir_facturas(self):
        # Aquí iría la lógica real para emitir facturas
        QMessageBox.information(self, "Facturas", "Tu vehículo está en reparación.")
    
    def cerrar_sesion(self):
        self.close()
        if self.parent():
            self.parent().show()
