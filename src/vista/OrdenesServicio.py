from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
import os
from src.controlador.ControladorRegistrarOrdenServicio import ControladorRegistrarOrdenServicio
from src.vista.AsignarOrden import AsignarOrden
from datetime import datetime

class RegistrarOrdenServicio(QMainWindow):
    def __init__(self, parent=None, usuario=None):
        print(f"[DEBUG] Entrando en __init__ de RegistrarOrdenServicio")
        print(f"[DEBUG] parent: {parent}, usuario: {usuario}")

        super().__init__(parent)  # o super().__init__() si no usas herencia con parent

        self.usuario = usuario

        print("[DEBUG] Llamando a setup_ui()")
        self.setup_ui()  # <-- Asegúrate de NO pasarle argumentos aquí
        print("[DEBUG] setup_ui() llamado correctamente")
        
        self.controller = ControladorRegistrarOrdenServicio(usuario)
        self.setup_events()
        self.cargar_vehiculos()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaOrdenesServicio.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Registrar Orden de Servicio")

        ruta_css = os.path.join(os.path.dirname(__file__),"qss", "estilos.qss")
        with open(ruta_css, "r") as f:
            self.setStyleSheet(f.read())

    def setup_events(self):
        self.btnRegistrar.clicked.connect(self.registrar_orden_servicio)
        self.btnAsignar.clicked.connect(self.asignar_orden)
        self.btnVolver.clicked.connect(self.volver)

    def cargar_vehiculos(self):
        self.combo_vehiculos.clear()
        vehiculos = self.controller.obtener_vehiculos()
        for v in vehiculos:
            desc = f"{v['Matricula']} - {v['Marca']}"
            self.combo_vehiculos.addItem(desc, v['IDVehiculo'])

    def registrar_orden_servicio(self):
        id_vehiculo = self.combo_vehiculos.currentData()
        descripcion = self.Descripcion.text().strip()
        fecha_ingreso = datetime.now().strftime("%Y-%m-%d")
        observaciones = self.Observaciones.text().strip()

        resultado = self.controller.registrar_orden(id_vehiculo, descripcion, fecha_ingreso, observaciones)

        if resultado:
            QMessageBox.information(self, "Éxito", "Orden registrada con exito")
        else:
            QMessageBox.warning(self, "Error", "Se ha producido un error al registrar la orden")
        
    def asignar_orden(self):
        self.ordenes_window = AsignarOrden(parent=self, usuario=self.usuario)
        self.ordenes_window.show()
        self.hide()

    def volver(self):
        if self.parent():
            self.parent().show()
        self.close()
