from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5 import uic
import os
from src.controlador.ControladorGestionPedidos import ControladorPedido

class GestionPedidos(QMainWindow):
    def __init__(self, parent=None, administrador=None):
        super().__init__(parent)
        self.parent = parent
        self.administrador = administrador

        self.controlador = ControladorPedido()

        self.setup_ui()
        self.setup_events()
        self.cargar_proveedores()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaPedido.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Panel de Pedidos")

        ruta_css = os.path.join(os.path.dirname(__file__),"qss", "estilos.qss")
        with open(ruta_css, "r") as f:
            self.setStyleSheet(f.read())

    def setup_events(self):
        self.btnAnadirAlPedido.clicked.connect(self.anadir_al_pedido)
        self.btnRealizarPedido.clicked.connect(self.realizar_pedido)
        self.btnEliminarDelPedido.clicked.connect(self.eliminar)
        self.btnVolver.clicked.connect(self.volver)

    def cargar_proveedores(self):
        proveedores = self.controlador.obtener_proveedores()
        self.combo_proveedores.clear()
        self.combo_proveedores.addItems(proveedores)

    def anadir_al_pedido(self):
        nombre = self.Nombre.text().strip()
        cantidad_text = self.Cantidad.text().strip()
        precioUnitario_text = self.PrecioUnitario.text().strip()

        if not nombre or not cantidad_text or not precioUnitario_text:
            QMessageBox.warning(self, "Error", "Por favor, rellena todos los campos")
            return

        try:
            cantidad = int(cantidad_text)
            precioUnitario = int(precioUnitario_text)
        except ValueError:
            QMessageBox.warning(self, "Error", "Cantidad debe ser un número entero")
            return

        row = self.tablaRepuestosPedidos.rowCount()
        self.tablaRepuestosPedidos.insertRow(row)
        self.tablaRepuestosPedidos.setItem(row, 0, QTableWidgetItem(nombre))
        self.tablaRepuestosPedidos.setItem(row, 1, QTableWidgetItem(str(cantidad)))
        self.tablaRepuestosPedidos.setItem(row, 2, QTableWidgetItem(str(precioUnitario)))

        self.Nombre.clear()
        self.Cantidad.clear()
        self.PrecioUnitario.clear()

    def realizar_pedido(self):
        proveedor = self.combo_proveedores.currentText()
        if not proveedor:
            QMessageBox.warning(self, "Error", "Selecciona un proveedor")
            return

        if self.tablaRepuestosPedidos.rowCount() == 0:
            QMessageBox.warning(self, "Error", "Añade al menos un repuesto al pedido")
            return

        repuestos = []
        for row in range(self.tablaRepuestosPedidos.rowCount()):
            nombre = self.tablaRepuestosPedidos.item(row, 0).text()
            cantidad = int(self.tablaRepuestosPedidos.item(row, 1).text())
            PrecioUnitario = int(self.tablaRepuestosPedidos.item(row, 2).text())
            repuestos.append((nombre, cantidad, PrecioUnitario))

        exito = self.controlador.crear_pedido(proveedor, repuestos)

        if exito:
            QMessageBox.information(self, "Éxito", "Pedido realizado con exito")
            self.tablaRepuestosPedidos.setRowCount(0)
        else:
            QMessageBox.warning(self, "Error","Se ha producido un error al realizar el pedido")

    def eliminar(self):
        fila_seleccionada = self.tablaRepuestosPedidos.currentRow()
        if fila_seleccionada >= 0:
            self.tablaRepuestosPedidos.removeRow(fila_seleccionada)
        else:
            QMessageBox.warning(self, "Error", "Selecciona una fila para eliminar")

    def volver(self):
        if self.parent:
            self.parent.show()
        self.close()

