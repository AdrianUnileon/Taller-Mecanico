from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
from src.modelo.UserDao.ClienteDAO import ClienteDao
from src.modelo.UserDao.UserDAOJDBC import UserDaoJDBC
from src.modelo.vo.ClienteVO import ClienteVO
from src.modelo.vo.UserVO import UserVO
import os

class RegistrarCliente(QMainWindow):
    def __init__(self, parent=None, usuario = None):
        super().__init__(parent)
        self.dao_cliente = ClienteDao()
        self.dao_usuario = UserDaoJDBC()
        self.usuario = usuario
        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaRegistroCliente.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Registro del Cliente")

        if self.usuario:
            self.lblTitulo.setText(f"Bienvenido/a {self.usuario.Nombre}")

    def setup_events(self):
        self.btnRegistrar.clicked.connect(self.registrar_cliente)
        self.btnVolver.clicked.connect(self.volver)
    
    def registrar_cliente(self):
        nombre = self.Nombre.text().strip()
        apellido1 = self.Apellido1.text().strip()
        apellido2 = self.Apellido2.text().strip()
        dni = self.DNI.text().strip()
        contacto = self.Telefono.text().strip()
        correo = self.Correo.text().strip()
        direccion = self.Direccion.text().strip()

        if not all([nombre, apellido1, apellido2, dni, correo, direccion, contacto]):
            QMessageBox.warning(self, "Campos incompletos", "Por favor, completa todos los campos.")
            return

        if self.dao_usuario.buscar_por_email(correo):
            QMessageBox.warning(self, "Duplicado", "Ya existe un usuario con este correo.")
            return
        
        contraseña_temporal = "1234"

        nuevo_usuario = UserVO(
            DNI=dni,
            Nombre=nombre,
            Apellidos=f"{apellido1} {apellido2}",
            Correo=correo,
            Contraseña=contraseña_temporal,
            TipoUsuario="Cliente"
        )
        
        if self.dao_usuario.buscar_por_email(correo):
            QMessageBox.warning(self, "Duplicado", "Ya existe un usuario con este correo.")
            return

        id_usuario = self.dao_usuario.insert(nuevo_usuario)

        if not id_usuario or id_usuario == 0:
            QMessageBox.critical(self, "Error", "No se pudo registrar el usuario.")
            return

        cliente = ClienteVO(IDUsuario=id_usuario, Direccion=direccion, Contacto=contacto)
        if self.dao_cliente.insertar(cliente) > 0:
            QMessageBox.information(self, "Éxito", "Cliente registrado correctamente.")
        else:
            QMessageBox.critical(self, "Error", "No se pudo registrar el cliente.")

    def volver(self):
        self.parent().show()
        self.close()