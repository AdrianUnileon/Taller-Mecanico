import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from src.vista.OrdenesServicio import RegistrarOrdenServicio
from src.vista.RegistroCliente import RegistrarCliente
from src.vista.RegistroVehículo import RegistrarVehiculo
from src.vista.Factura import Facturas
from src.vista.DarDeBajaVehiculos import DarDeBajaVehiculos

class RecepcionistaPanel(QMainWindow):
    def __init__(self, parent = None, id_recepcionista=None):
        super().__init__(parent)
        self.id_recepcionista = id_recepcionista
        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaRecepcionista.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Panel del Recepcionista")

        
    def setup_events(self):
        self.btnRegistrarCliente.clicked.connect(self.registrar_cliente)
        self.btnCrearOrdenServicio.clicked.connect(self.crear_orden_servicio)
        self.btnRegistrarVehiculo.clicked.connect(self.registrar_vehiculo)
        self.btnEmitirFacturas.clicked.connect(self.emitir_facturas)
        self.btnBajaVehiculos.clicked.connect(self.baja_vehiculos)
        self.btnCerrarSesion.clicked.connect(self.cerrar_sesion)

    def registrar_cliente(self):
        self.ordenes_window = RegistrarCliente(parent=self, usuario = self.usuario)
        self.ordenes_window.show()
        self.hide()
    
    def crear_orden_servicio(self):
        self.ordenes_window = RegistrarOrdenServicio(parent=self, usuario=self.usuario)
        self.ordenes_window.show()
        self.hide()
    
    def registrar_vehiculo(self):
        self.ordenes_window = RegistrarVehiculo(parent=self, usuario = self.usuario)
        self.ordenes_window.show()
        self.hide()
    
    def emitir_facturas(self):
        self.ordenes_window = Facturas(id_recepcionista= self.id_recepcionista, parent=self)
        self.ordenes_window.show()
        self.hide()

    def baja_vehiculos(self):
        self.ordenes_window = DarDeBajaVehiculos(parent=self)
        self.ordenes_window.show()
        self.hide()
    
    def cerrar_sesion(self):
        self.close()
        if self.parent():
            self.parent().show()
