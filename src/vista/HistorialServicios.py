import os
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5 import uic
from src.modelo.UserDao.OrdenServicioDAO import OrdenServicioDAO

class HistorialCliente(QMainWindow):
    def __init__(self, parent=None, id_cliente=None):
        super().__init__(parent)
        self.parent = parent
        self.id_cliente = id_cliente
        self.dao = OrdenServicioDAO()
        self.setup_ui()
        self.setup_events()
        self.cargar_servicios()
    
    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaHistorialServicios.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Historial de Servicios")

    def setup_events(self):
        self.btnDescargar.clicked.connect(self.descargar)
        self.btnVolver.clicked.connect(self.volver)

    def cargar_servicios(self):
        servicios = self.dao.obtener_ordenes_por_cliente(self.id_cliente)
        self.tablaServicios.setRowCount(len(servicios))
        self.tablaServicios.setHorizontalHeaderLabels(["IDOrden", "FechaIngreso", "Descripcion", "Estado", "Vehiculo"])
        for i, orden in enumerate(servicios):
            self.tablaServicios.setItem(i, 0, QTableWidgetItem(str(orden["IDOrden"])))
            self.tablaServicios.setItem(i, 1, QTableWidgetItem(str(orden["FechaIngreso"])))
            self.tablaServicios.setItem(i, 2, QTableWidgetItem(orden["Descripcion"]))
            self.tablaServicios.setItem(i, 3, QTableWidgetItem(orden["Estado"]))
            vehiculo = f"{orden['Marca']} {orden['Modelo']} ({orden['Matricula']})"
            self.tablaServicios.setItem(i, 4, QTableWidgetItem(vehiculo))

    def descargar(self):
        #Logica para descargar (DUDA)
        QMessageBox.information(self, "Ver reportes", "Mostrando los reportes...")

    def volver(self):
        if self.parent:
            self.parent.show()
        self.close()
            
    