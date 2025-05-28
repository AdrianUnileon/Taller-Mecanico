from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
import os
from src.controlador.ControladorRegistrarOrdenServicio import ControladorRegistrarOrdenServicio

class RegistrarOrdenServicio(QMainWindow):
    def __init__(self, parent=None, usuario=None):
        super().__init__(parent)
        self.usuario = usuario
        self.controller = ControladorRegistrarOrdenServicio(usuario)
        self.setup_ui()
        self.setup_events()
        self.cargar_vehiculos()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaOrdenesServicio.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Registrar Orden de Servicio")

        if self.usuario:
            self.lblTitulo.setText(f"Bienvenido/a {self.usuario.Nombre}")

    def setup_events(self):
        self.btnRegistrar.clicked.connect(self.registrar_orden_servicio)
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
        fecha_ingreso = self.FechaIngreso.date().toString("yyyy-MM-dd")
        observaciones = self.Observaciones.text().strip()

        resultado = self.controller.registrar_orden(id_vehiculo, descripcion, fecha_ingreso, observaciones)

        if resultado:
            QMessageBox.information(self, "Éxito", "Orden registrada con exito")
        else:
            QMessageBox.warning(self, "Error", "Se ha producido un error al registrar la orden")

    def volver(self):
        self.parent().show()
        self.close()
