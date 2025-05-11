from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
from src.modelo.UserDao.ClienteDAO import ClienteDao
from src.modelo.UserDao.UserDAOJDBC import UserDaoJDBC
from src.modelo.vo.ClienteVO import ClienteVO
import os

class RegistrarCliente(QMainWindow):
    def __init__(self, parent=None, usuario = None):
        super().__init__(parent)
        self.dao_cliente = ClienteDao()
        self.dao_usuario = UserDaoJDBC()
        self.usuario = usuario
        self.setup_ui()
        self.setup_events()
        self.cargar_usuarios()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaRegistroCliente.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Registro del Cliente")

        if self.usuario:
            self.lblTitulo.setText(f"Bienvenido/a {self.usuario.Nombre}")

    def setup_events(self):
        self.btnRegistrar.clicked.connect(self.registrar_cliente)
        self.btnVolver.clicked.connect(self.volver)

    def cargar_usuarios(self):
        usuarios = self.dao_usuario.obtener_usuarios_tipo("Cliente")
        self.cmbUsuarios.clear()
        for usuario in usuarios:
            self.cmbUsuarios.addItem(f"{usuario.Nombre} ({usuario.IDUsuario})", usuario.IDUsuario)

    def registrar_cliente(self):
        id_usuario = self.cmbUsuarios.currentData()
        direccion = self.txtDireccion.text().strip()
        contacto = self.txtContacto.text().strip()

        if self.dao_cliente.buscar_por_usuario(id_usuario):
            QMessageBox.warning(self, "Duplicado", "Este usuario ya es un cliente.")
            return

        cliente = ClienteVO(IDUsuario=id_usuario, Direccion=direccion, Contacto=contacto)
        if self.dao_cliente.insertar(cliente) > 0:
            QMessageBox.information(self, "Éxito", "Cliente registrado correctamente.")
            self.close()
        else:
            QMessageBox.critical(self, "Error", "No se pudo registrar el cliente.")
  
    
    def volver(self):
        self.parent().show()
        self.close()