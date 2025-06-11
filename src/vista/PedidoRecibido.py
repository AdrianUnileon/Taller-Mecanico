import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5 import uic

from src.controlador.ControladorPedidosRecibidos import ControladorActualizarPedido

class ActualizarEstadoPedido(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.controlador = ControladorActualizarPedido()

        self.setup_ui()
        self.setup_events()
        self.cargar_pedidos()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaPedidoRecibido.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Actualizar estado de pedidos")

        ruta_css = os.path.join(os.path.dirname(__file__),"qss", "estilos.qss")
        with open(ruta_css, "r") as f:
            self.setStyleSheet(f.read())

    def setup_events(self):
        self.btnRecibido.clicked.connect(self.marcar_recibido)
        self.btnVolver.clicked.connect(self.volver)

    def cargar_pedidos(self):
        pedidos = self.controlador.obtener_pedidos_en_transito()
        self.tablPedidoTransito.setRowCount(0)
        self.tablPedidoTransito.setColumnCount(4)
        self.tablPedidoTransito.setHorizontalHeaderLabels(["IDpedido","FechaPedido", "Estado", "Proveedor"])

        for pedido in pedidos:
            fila = self.tablPedidoTransito.rowCount()
            self.tablPedidoTransito.insertRow(fila)

            self.tablPedidoTransito.setItem(fila, 0, QTableWidgetItem(pedido.get("IDPedido", "Desconocido")))
            self.tablPedidoTransito.setItem(fila, 1, QTableWidgetItem(str(pedido["FechaPedido"])))
            self.tablPedidoTransito.setItem(fila, 2, QTableWidgetItem(pedido["Estado"]))
            self.tablPedidoTransito.setItem(fila, 3, QTableWidgetItem(pedido.get("Proveedor", "Proveedor Herramientas")))


    def marcar_recibido(self):
        fila = self.tablPedidoTransito.currentRow()
        if fila == -1:
            QMessageBox.warning(self, "Error", "Por favor, selecciona un pedido primero")
            return

        item = self.tablPedidoTransito.item(fila, 0)
        if item is None:
            QMessageBox.warning(self, "Error", "La celda está vacía")
            return

        texto_id = item.text()

        try:
            id_pedido = int(texto_id)
        except ValueError:
            QMessageBox.warning(self, "Error", f"ID del pedido inválido: {texto_id}")
            return

        self.controlador.marcar_pedido_como_recibido(id_pedido)
        QMessageBox.information(self, "Éxito", f"Pedido {id_pedido} marcado como recibido")
        self.cargar_pedidos()


    def volver(self):
        if self.parent:
            self.parent.show()
        self.close()
