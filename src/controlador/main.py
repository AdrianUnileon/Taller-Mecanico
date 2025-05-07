import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QInputDialog, QLineEdit
from src.vista.Principal import PrincipalWindow
from src.vista.AdministradorPanel import AdministradorPanel

# Contraseña
ADMIN_PASSWORD = "admin1234"

def main():
    app = QApplication(sys.argv)

    # Pregunta inicial
    respuesta = QMessageBox.question(
        None,
        "Acceso",
        "¿Eres el administrador?",
        QMessageBox.Yes | QMessageBox.No
    )

    if respuesta == QMessageBox.Yes:
        password, ok = QInputDialog.getText(
            None,
            "Verificación de Administrador",
            "Introduce la contraseña:",
            QLineEdit.Password
        )

        if ok and password == ADMIN_PASSWORD:
            ventana = AdministradorPanel()
            ventana.show()
        else:
            QMessageBox.critical(None, "Error", "Contraseña incorrecta. Acceso denegado.")
            sys.exit()            

    else:
        ventana = PrincipalWindow()
        ventana.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

