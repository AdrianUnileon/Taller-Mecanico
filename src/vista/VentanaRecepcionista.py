from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
import os
from src.modelo.UserDao.UserDAOJDBC import UserDaoJDBC
from src.modelo.vo.UserVO import UserVO
from src.modelo.vo.RecepcionistaVO import RecepcionistaVO
from src.modelo.UserDao.RecepcionistaDAO import RecepcionistaDAO

class VentanaRecepcionista(QMainWindow):
    def __init__(self, usuario: UserVO, parent=None):
        super().__init__(parent)
        self.usuario = usuario
        self.parent = parent
        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaVentanaRecepcionista.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Registro Recepcionista")

    def setup_events(self):
        self.btnRegistrar.clicked.connect(self.registrar_cliente)
        self.btnVolver.clicked.connect(self.volver)

    def registrar_cliente(self):
        turno = self.Turno.text().strip()
        if not turno:
            QMessageBox.warning(self, "Campos vacíos", "Por favor completa todos los campos.")
            return
        try:
            
            id_usuario = self.usuario.IDUsuario

            recepcionista = RecepcionistaVO(IDUsuario=id_usuario, Turno=turno)
            dao = RecepcionistaDAO()
            id_recepcionista = dao.insertar(recepcionista)

            if id_recepcionista:
                QMessageBox.information(self, "Registro exitoso", "Recepcionista registrado correctamente.")
                self.close()
                if self.parent:
                    self.parent.show()
            else:
                QMessageBox.critical(self, "Error", "No se pudo registrar el recepcionista.")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error: {str(e)}")

    def volver(self):
        if self.parent:
            self.parent.show()
        self.close()