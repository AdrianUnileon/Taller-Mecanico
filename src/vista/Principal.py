import os
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from src.vista.Login import LoginWindow
from src.vista.Registro import RegistroWindow

class PrincipalWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        ruta_ui = os.path.join(os.path.dirname(__file__), "Ui", "VistaPrincipal.ui")
        uic.loadUi(ruta_ui, self)
        self.setWindowTitle("Panel Principal")

    def setup_events(self):
        # Conectar botones a las ventanas
        self.btnLogin.clicked.connect(self.abrir_login)
        self.btnRegistro.clicked.connect(self.abrir_registro)
        self.btnSalir.clicked.connect(self.salir_aplicacion)

    def abrir_login(self):
        self.login_window = LoginWindow(self)  
        self.login_window.show()
        self.hide()  

    def abrir_registro(self):
        self.registro_window = RegistroWindow(self)  
        self.registro_window.show()
        self.hide()  
    
    def salir_aplicacion(self):
        self.close()

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    ventana = PrincipalWindow()
    ventana.show()
    app.exec_()