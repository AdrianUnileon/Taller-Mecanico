from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5 import uic
import os

from src.modelo.UserDao.PedidoDAO import PedidoDAO
from src.modelo.UserDao.ProveedorDAO import ProveedorDAO

class ActualizarEstadoPedido(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.dao_pedido = PedidoDAO()
        self.dao_proveedor = ProveedorDAO()

        self.setup_ui()
        self.setup_events()
        self.cargar_pedidos()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaPedidoRecibido.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Actualizar estado de pedidos")

    def setup_events(self):
        self.btnRecibido.clicked.connect(self.marcar_recibido)
        self.btnVolver.clicked.connect(self.volver)

    def cargar_pedidos(self):
        pedidos = self.dao_pedido.obtener_pedidos_por_estado("en transito")
        self.tablPedidoTransito.setRowCount(0)
        self.tablPedidoTransito.setColumnCount(4)
        self.tablPedidoTransito.setHorizontalHeaderLabels(["Pedido", "FechaPedido", "Estado", "Proveedor"])

        for pedido in pedidos:
            fila = self.tablPedidoTransito.rowCount()
            self.tablPedidoTransito.insertRow(fila)
            self.tablPedidoTransito.setItem(fila, 0, QTableWidgetItem(str(pedido["Pedido"])))
            self.tablPedidoTransito.setItem(fila, 1, QTableWidgetItem(str(pedido["FechaPedido"])))
            self.tablPedidoTransito.setItem(fila, 2, QTableWidgetItem(pedido["Estado"]))
            self.tablPedidoTransito.setItem(fila, 3, QTableWidgetItem(pedido["Proveedor"]))

    def marcar_recibido(self):
        fila = self.tablPedidoTransito.currentRow()
        if fila == -1:
            QMessageBox.warning(self, "Error", "Por favor, selecciona un pedido primero")
            return

        item = self.tablPedidoTransito.item(fila, 0)
        if item is None:
            QMessageBox.warning(self, "Error", "La celda está vacía")
            return

        try:
            id_pedido = int(item.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "ID del pedido inválido")
            return

        nuevo_estado = "recibido"
        self.dao_pedido.actualizar_estado_pedido(id_pedido, nuevo_estado)
        QMessageBox.information(self, "Éxito", f"Pedido {id_pedido} marcado como {nuevo_estado}")
        self.cargar_pedidos()  


    def volver(self):
        if self.parent:
            self.parent.show()
        self.close()
