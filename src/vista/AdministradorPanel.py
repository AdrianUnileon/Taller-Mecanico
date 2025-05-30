import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from src.vista.GestionProveedores import GestionProveedores
from src.vista.GestionRepuestos import GestionRepuestos
from src.vista.GestionarPedidos import GestionPedidos
from src.vista.PedidoRecibido import ActualizarEstadoPedido

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
        self.btnGestionarProveedores.clicked.connect(self.gestionar_proveedores)
        self.btnGestionarRepuestos.clicked.connect(self.gestionar_repuestos)
        self.btnGestionarPedidosProveedores.clicked.connect(self.gestionar_pedidos_proveedores)
        self.btnPedidos.clicked.connect(self.pedidos)
        self.btnSalirAplicacion.clicked.connect(self.salir_aplicacion)

    def gestionar_proveedores(self):
        self.administrador_orden = GestionProveedores(parent = self)
        self.administrador_orden.show()
        self.hide()

    def gestionar_repuestos(self):
        self.administrador_orden = GestionRepuestos(parent = self)
        self.administrador_orden.show()
        self.hide()

    def gestionar_pedidos_proveedores(self):
        self.administrador_orden = GestionPedidos(self, administrador = self.administrador)
        self.administrador_orden.show()
        self.hide()

    def pedidos(self):
        self.administrador_orden = ActualizarEstadoPedido(self)
        self.administrador_orden.show()
        self.hide()
    
    def salir_aplicacion(self):
        self.close()

    
