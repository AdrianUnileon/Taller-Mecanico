from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
import os
from src.modelo.UserDao.MecanicoDAO import MecanicoDAO
from src.modelo.vo.MecanicoVO import MecanicoVO
from src.modelo.UserDao.UserDAOJDBC import UserDaoJDBC
from src.modelo.vo.UserVO import UserVO
from datetime import datetime

class VentanaMecanico(QMainWindow):
    def __init__(self, usuario: UserVO, parent=None):
        super().__init__(parent)
        self.usuario = usuario
        self.parent = parent
        self.setup_ui()
        self.setup_events()
    
    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaVentanaMecanico.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Registro Mecanico")

    def setup_events(self):
        self.btnRegistrar.clicked.connect(self.registrar_cliente)
        self.btnVolver.clicked.connect(self.volver)

    def registrar_cliente(self):
        especialidad = self.Especialidad.text().strip()
        fechacontratacion = self.FechaContratacion.text().strip()

        if not especialidad or not fechacontratacion:
            QMessageBox.warning(self, "Campos vacíos", "Por favor completa todos los campos.")
            return

        try:
            Fecha = datetime.strptime(fechacontratacion, "%d/%m/%Y").date()
            # Insertar el usuario en Usuarios
            user_dao = UserDaoJDBC()
            id_usuario = user_dao.insert(self.usuario)

            # Crear Cliente y registrar
            mecanico = MecanicoVO(IDUsuario=id_usuario, Especialidad=especialidad, FechaContratacion=Fecha)
            dao = MecanicoDAO()
            id_mecanico = dao.insertar(mecanico)

            if id_mecanico:
                QMessageBox.information(self, "Registro exitoso", "Mecanico registrado correctamente")
                self.close()
                if self.parent:
                    self.parent.show()
            else:
                QMessageBox.critical(self, "Error", "No se pudo registrar el mecanico.")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error: {str(e)}")

    def volver(self):
        if self.parent:
            self.parent.show()
        self.close()

