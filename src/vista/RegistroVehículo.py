from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
import os

from src.controlador.ControladorRegistrarVehiculo import ControladorRegistrarVehiculo


class RegistrarVehiculo(QMainWindow):
    def __init__(self, parent=None, usuario=None):
        super().__init__(parent)
        self.usuario = usuario
        self.controller = ControladorRegistrarVehiculo(usuario)
        self.setup_ui()
        self.setup_events()
        self.cargar_clientes()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaRegistroVehiculo.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Registro de Vehículo")

        ruta_css = os.path.join(os.path.dirname(__file__),"qss", "estilos.qss")
        with open(ruta_css, "r") as f:
            self.setStyleSheet(f.read())

    def setup_events(self):
        self.btnRegistrar.clicked.connect(self.on_registrar_clicked)
        self.btnVolver.clicked.connect(self.volver)

    def cargar_clientes(self):
        self.combo_clientes.clear()
        clientes = self.controller.obtener_clientes()
        for cliente in clientes:
            nombre = f"{cliente['Nombre']} {cliente['Apellidos']}"
            self.combo_clientes.addItem(nombre, cliente['IDCliente'])

    def on_registrar_clicked(self):
        id_cliente = self.combo_clientes.currentData()
        matricula = self.Matricula.text().strip()
        marca = self.Marca.text().strip()
        modelo = self.Modelo.text().strip()
        anio = self.Anio.text().strip()

        resultado = self.controller.registrar_vehiculo(id_cliente, matricula, marca, modelo, anio)

        if resultado:
            QMessageBox.information(self, "Éxito", "Se ha registrado con exito el vehículo.")
        else:
            QMessageBox.warning(self, "Error", "Se ha producido un fallo al registrar el vehículo.")

    def volver(self):
        if self.parent():
            self.parent().show()
        self.close()
