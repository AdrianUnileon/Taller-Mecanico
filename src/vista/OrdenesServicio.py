from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
import os
from src.modelo.UserDao.OrdenServicioDAO import OrdenServicioDAO
from src.modelo.vo.OrdenServicioVO import OrdenServicioVO
from src.modelo.vo.VehiculoVO import VehiculoVO
from src.modelo.UserDao.VehiculoDAO import VehiculoDAO

class RegistrarOrdenServicio(QMainWindow):
    def __init__(self, parent=None, usuario=None):
        super().__init__(parent)
        self.usuario = usuario
        self.dao_orden_servicio = OrdenServicioDAO()
        self.dao_vehiculo = VehiculoDAO()
        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaOrdenesServicio.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Registrar Orden de Servicio")

        if self.usuario:
            self.lblTitulo.setText(f"Bienvenido/a {self.usuario.Nombre}")

        self.cargar_vehiculos()

    def setup_events(self):
        self.btnRegistrar.clicked.connect(self.registrar_orden_servicio)
        self.btnVolver.clicked.connect(self.volver)

    def cargar_vehiculos(self):
        self.combo_vehiculos.clear()
        vehiculos = self.dao_vehiculo.select()  # Método `select` en VehiculoDAO

        for vehiculo in vehiculos:
            matricula = vehiculo['Matricula']
            marca = vehiculo['Marca']
            id_vehiculo = vehiculo['IDVehiculo']
            vehiculo_info = f"{matricula} - {marca}"
            self.combo_vehiculos.addItem(vehiculo_info, id_vehiculo)

    def registrar_orden_servicio(self):
        id_vehiculo = self.combo_vehiculos.currentData()
        descripcion = self.Descripcion.text().strip()
        fecha_ingreso = self.FechaIngreso.date().toString("yyyy-MM-dd")  # Formato de fecha
        observaciones = self.Observaciones.text().strip()

        if not all([descripcion, fecha_ingreso, observaciones]) or id_vehiculo is None:
            QMessageBox.warning(self, "Campos incompletos", "Por favor, rellena todos los campos.")
            return

        orden_servicio = OrdenServicioVO(
            FechaIngreso=fecha_ingreso,
            Descripcion=descripcion,
            Estado="Pendiente de asignación",
            IDVehiculo=id_vehiculo,
            IDMecanico=None  # Se asignará más adelante
        )

        if self.dao_orden_servicio.insertar(orden_servicio) > 0:
            QMessageBox.information(self, "Éxito", "Orden de servicio registrada correctamente.")
            
        else:
            QMessageBox.critical(self, "Error", "No se pudo registrar la orden de servicio.")

    def volver(self):
        self.parent().show()
        self.close()
