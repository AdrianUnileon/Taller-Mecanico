from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
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
        self.cargar_tabla()

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

    def cargar_tabla(self):
        datos = self.controlador.obtener_ordenes_para_factura()
        self.tablaOrdenesFinalizadas.setRowCount(len(datos))
        self.tablaOrdenesFinalizadas.setColumnCount(6)
        self.tablaOrdenesFinalizadas.setHorizontalHeaderLabels([
            "ID Orden", "Descripción", "Estado", "Precio Final", "Cliente", "Vehículo"
        ])
        for fila, orden in enumerate(datos):
            precio_total = round(orden["CostoManoObra"] * Decimal("1.36"), 2)
            self.tablaOrdenesFinalizadas.setItem(fila, 0, QTableWidgetItem(str(orden["IDOrden"])))
            self.tablaOrdenesFinalizadas.setItem(fila, 1, QTableWidgetItem(orden["Descripcion"]))
            self.tablaOrdenesFinalizadas.setItem(fila, 2, QTableWidgetItem(orden["Estado"]))
            self.tablaOrdenesFinalizadas.setItem(fila, 3, QTableWidgetItem(f"{precio_total:.2f} €"))
            self.tablaOrdenesFinalizadas.setItem(fila, 4, QTableWidgetItem(orden["NombreCliente"]))
            self.tablaOrdenesFinalizadas.setItem(fila, 5, QTableWidgetItem(orden["Vehiculo"]))

    def generar_factura(self):
        fila = self.tablaOrdenesFinalizadas.currentRow()
        if fila == -1:
            QMessageBox.warning(self, "Atención", "Seleccione una orden para facturar.")
            return

        id_orden = int(self.tablaOrdenesFinalizadas.item(fila, 0).text())
        precio_str = self.tablaOrdenesFinalizadas.item(fila, 3).text().replace("€", "").strip()
        precio_sin_iva_y_beneficio = float(precio_str) / 1.36  

        exito = self.controlador.generar_factura(id_orden, precio_sin_iva_y_beneficio, self.id_recepcionista)

        if exito:
            QMessageBox.information(self, "Factura creada", "La factura fue generada correctamente.")
            self.cargar_tabla()
        else:
            QMessageBox.critical(self, "Error", "No se pudo generar la factura.")

    def volver(self):
        self.close()
        if self.parent():
            self.parent().show()
