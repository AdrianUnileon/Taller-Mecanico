from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
import os
from src.modelo.UserDao.ClienteDAO import ClienteDao
from src.modelo.vo.ClienteVO import ClienteVO
from src.modelo.UserDao.UserDAOJDBC import UserDaoJDBC
from src.modelo.vo.UserVO import UserVO

class VentanaCliente(QMainWindow):
    def __init__(self, usuario: UserVO, parent=None):
        super().__init__(parent)
        self.usuario = usuario
        self.parent = parent
        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaVentanaCliente.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Registro Cliente")

    def setup_events(self):
        self.btnRegistrar.clicked.connect(self.registrar_cliente)
        self.btnVolver.clicked.connect(self.volver)

    def registrar_cliente(self):
        direccion = self.Direccion.text().strip()
        contacto = self.Contacto.text().strip()

        if not direccion or not contacto:
            QMessageBox.warning(self, "Campos vacíos", "Por favor completa todos los campos.")
            return

        try:
            # Insertar el usuario en Usuarios
            user_dao = UserDaoJDBC()
            id_usuario = user_dao.insert(self.usuario)

            # Crear Cliente y registrar
            cliente = ClienteVO(IDUsuario=id_usuario, Direccion=direccion, Contacto=contacto)
            dao = ClienteDao()
            id_cliente = dao.insertar(cliente)

            if id_cliente:
                QMessageBox.information(self, "Registro exitoso", f"Cliente registrado con ID: {id_cliente}")
                self.close()
                if self.parent:
                    self.parent.show()
            else:
                QMessageBox.critical(self, "Error", "No se pudo registrar el cliente.")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error: {str(e)}")

    def volver(self):
        if self.parent:
            self.parent.show()
        self.close()
