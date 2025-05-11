from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
import os

from src.modelo.UserDao.ClienteDAO import ClienteDao
from src.modelo.UserDao.VehiculoDAO import VehiculoDAO
from src.modelo.vo.VehiculoVO import VehiculoVO
from src.modelo.vo.ClienteVO import ClienteVO

class RegistrarVehiculo(QMainWindow):
    def __init__(self, parent=None, usuario=None):
        super().__init__(parent)
        self.usuario = usuario
        self.dao_cliente = ClienteDao()
        self.dao_vehiculo = VehiculoDAO()
        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaRegistroVehiculo.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Registro de Vehículo")

        if self.usuario:
            self.lblTitulo.setText(f"Bienvenido/a {self.usuario.Nombre}")

        self.cargar_clientes()

    def setup_events(self):
        self.btnRegistrar.clicked.connect(self.registrar_vehiculo)
        self.btnVolver.clicked.connect(self.volver)

    def cargar_clientes(self):
        self.combo_clientes.clear()
        clientes = self.dao_cliente.select()

        for cliente in clientes:
            nombre = cliente['Nombre']
            apellidos = cliente['Apellidos']
            id_cliente = cliente['IDCliente']
            nombre_completo = f"{nombre} {apellidos}"
            self.combo_clientes.addItem(nombre_completo, id_cliente)


    def registrar_vehiculo(self):
        id_cliente = self.combo_clientes.currentData()
        matricula = self.Matricula.text().strip()
        marca = self.Marca.text().strip()
        modelo = self.Modelo.text().strip()
        anio = self.Anio.text().strip()

        if not all([matricula, marca, modelo, anio]) or id_cliente is None:
            QMessageBox.warning(self, "Campos incompletos", "Por favor, rellena todos los campos.")
            return

        if self.dao_vehiculo.buscar_por_matricula(matricula):
            QMessageBox.warning(self, "Duplicado", "Ya existe un vehículo con esa matrícula.")
            return

        vehiculo = VehiculoVO(
            Matricula=matricula,
            Marca=marca,
            Modelo=modelo,
            Anio=int(anio),
            IDCliente=id_cliente
        )

        if self.dao_vehiculo.insertar(vehiculo) > 0:
            QMessageBox.information(self, "Éxito", "Vehículo registrado correctamente.")
        else:
            QMessageBox.critical(self, "Error", "No se pudo registrar el vehículo.")
    
    def volver(self):
        self.parent().show()
        self.close()
