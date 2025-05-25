import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
from src.vista.GestionPanel import GestionPanel

class AdministradorPanel(QMainWindow):
    def __init__(self, parent = None, administrador=None):
        super().__init__(parent)
        self.administrador = administrador
        self.setup_ui()
        self.setup_events()
    
    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaAdministrador.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Panel del Administrador")
        
    def setup_events(self):
        self.btnGestionarRepuestosyProveedores.clicked.connect(self.gestionar_repuestos_proveedores)
        self.btnGestionarPedidosProveedores.clicked.connect(self.gestionar_pedidos_proveedores)
        self.btnVerReportes.clicked.connect(self.ver_reportes)
        self.btnSalirAplicacion.clicked.connect(self.salir_aplicacion)

    def gestionar_repuestos_proveedores(self):
        self.administrador_orden = GestionPanel(self, administrador = self.administrador)
        self.administrador_orden.show()
        self.hide()

    def gestionar_pedidos_proveedores(self):
        # Aquí iría la lógica real para gestionar los pedidos a los proveedores
        QMessageBox.information(self, "Historial de Servicios", "Mostrando historial de servicios...")
    
    def ver_reportes(self):
        # Aquí iría la lógica real para ver los reportes
        QMessageBox.information(self, "Ver reportes", "Mostrando los reportes...")
    
    def salir_aplicacion(self):
        self.close()

    
