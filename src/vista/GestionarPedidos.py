from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5 import uic
import os
from datetime import date
from src.modelo.UserDao.PedidoDAO import PedidoDAO
from src.modelo.UserDao.RepuestoDAO import RepuestoDAO

class GestionPedidos(QMainWindow):
    def __init__(self, parent=None, administrador=None):
        super().__init__(parent)
        self.parent = parent
        self.administrador = administrador

        self.dao_pedido = PedidoDAO()
        self.dao_repuesto = RepuestoDAO()

        self.setup_ui()
        self.setup_events()
        self.cargar_repuestos()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaPedido.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Panel de Pedidos")

    def setup_events(self):
        self.btnAnadirAlPedido.clicked.connect(self.anadir_al_pedido)
        self.btnRealizarPedido.clicked.connect(self.realizar_pedido)
        self.btnEliminarDelPedido.clicked.connect(self.eliminar)
        self.btnVolver.clicked.connect(self.volver)

    def cargar_repuestos(self):
        conn = self.dao_pedido.conexion_singleton.createConnection()
        cursor = conn.cursor()
        cursor.execute("SELECT Nombre FROM Proveedores")
        proveedores = cursor.fetchall()
        self.combo_proveedores.clear()
        for prov in proveedores:
            self.combo_proveedores.addItem(prov[0])
        cursor.close()

    def anadir_al_pedido(self):
        nombre = self.Nombre.text().strip()
        cantidad_text = self.Cantidad.text().strip()

        if not nombre or not cantidad_text:
            QMessageBox.warning(self, "Error", "Por favor, rellena todos los campos")
            return

        try:
            cantidad = int(cantidad_text)
        except ValueError:
            QMessageBox.warning(self, "Error", "Cantidad debe ser un número entero")
            return

        row = self.tablaRepuestosPedidos.rowCount()
        self.tablaRepuestosPedidos.insertRow(row)
        self.tablaRepuestosPedidos.setItem(row, 0, QTableWidgetItem(nombre))
        self.tablaRepuestosPedidos.setItem(row, 1, QTableWidgetItem(str(cantidad)))

        self.Nombre.clear()
        self.Cantidad.clear()
    
    def realizar_pedido(self):
        proveedor_nombre = self.combo_proveedores.currentText()

        if not proveedor_nombre:
            QMessageBox.warning(self, "Error", "Selecciona un proveedor")
            return

        if self.tablaRepuestosPedidos.rowCount() == 0:
            QMessageBox.warning(self, "Error", "Añade al menos un repuesto al pedido")
            return

        proveedor_id = self.dao_pedido.obtener_id_proveedor(proveedor_nombre)
        if not proveedor_id:
            QMessageBox.warning(self, "Error", "Proveedor no encontrado en base de datos")
            return

        from datetime import date
        fecha = date.today()
        estado = "en tránsito"

        pedido_id = self.dao_pedido.insertar_pedido(proveedor_id, fecha, estado)
        if pedido_id == 0:
            QMessageBox.warning(self, "Error", "No se pudo registrar el pedido")
            return

        for row in range(self.tablaRepuestosPedidos.rowCount()):
            nombre = self.tablaRepuestosPedidos.item(row, 0).text()
            cantidad = int(self.tablaRepuestosPedidos.item(row, 1).text())

            repuesto_id = self.dao_repuesto.obtener_id_por_nombre(nombre)
            if repuesto_id is None:
            # Insertar nuevo repuesto porque no existe
                repuesto_id = self.dao_repuesto.insertar_repuesto(nombre)
                if repuesto_id is None:
                    continue

        # Insertar detalle con precio_unitario 0 (o lo que desees)
            self.dao_pedido.insertar_detalle(pedido_id, repuesto_id, cantidad, precio_unitario=0)

        QMessageBox.information(self, "Éxito", "Pedido registrado correctamente")
        self.tablaRepuestosPedidos.setRowCount(0)

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
