import sys
from PyQt5.QtWidgets import QApplication
from src.controlador.ControladorAcceso import ControladorAcceso

def main():
    app = QApplication(sys.argv)
    controlador = ControladorAcceso()
    controlador.iniciar()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
