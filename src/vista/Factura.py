from PyQt5.QtWidgets import QMainWindow, QMessageBox, QComboBox
from PyQt5 import uic
import os
from decimal import Decimal

from src.controlador.ControladorFactura import ControladorFacturas

class Facturas(QMainWindow):
    def __init__(self, id_recepcionista, parent=None):
        super().__init__(parent)
        self.id_recepcionista = id_recepcionista
        self.controlador = ControladorFacturas()
        self.setup_ui()
        self.setup_events()
        self.cargar_facturas()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaFacturas.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Facturación")

        ruta_css = os.path.join(os.path.dirname(__file__),"qss", "estilos.qss")
        with open(ruta_css, "r") as f:
            self.setStyleSheet(f.read())

    def setup_events(self):
        self.btnGenerarfactura.clicked.connect(self.generar_factura)
        self.btnVolver.clicked.connect(self.volver)

    def cargar_facturas(self):
        self.comboFacturas.clear()
        datos = self.controlador.obtener_ordenes_para_factura()
        for orden in datos:
            precio_total = round(orden["CostoManoObra"] * Decimal("1.36"), 2)
            descripcion = (
                f"ID: {orden['IDOrden']} - {orden['Descripcion']} - "
                f"Estado: {orden['Estado']} - Precio: {precio_total:.2f} € - "
                f"Cliente: {orden['NombreCliente']} - Vehículo: {orden['Vehiculo']}"
            )
            self.comboFacturas.addItem(descripcion, orden["IDOrden"])

        if self.comboFacturas.count() == 0:
            self.comboFacturas.addItem("No hay órdenes para facturar", -1)
            self.comboFacturas.setEnabled(False)
        else:
            self.comboFacturas.setEnabled(True)

    def generar_factura(self):
        id_orden = self.comboFacturas.currentData()
        if id_orden == -1 or id_orden is None:
            QMessageBox.warning(self, "Atención", "Seleccione una orden válida para facturar.")
            return

        orden_seleccionada = next((o for o in self.controlador.obtener_ordenes_para_factura() if o["IDOrden"] == id_orden), None)
        if orden_seleccionada is None:
            QMessageBox.critical(self, "Error", "No se pudo encontrar la orden seleccionada.")
            return

        costo_mano_obra = Decimal(orden_seleccionada["CostoManoObra"])
        total_factura = round(costo_mano_obra * Decimal("1.36"), 2) 

        exito = self.controlador.generar_factura(id_orden, float(total_factura), self.id_recepcionista)

        if exito:
            QMessageBox.information(self, "Factura creada", "La factura fue generada correctamente.")
            self.cargar_facturas()
        else:
            QMessageBox.critical(self, "Error", "No se pudo generar la factura.")

    def volver(self):
        self.close()
        if self.parent():
            self.parent().show()
