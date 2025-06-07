from PyQt5.QtWidgets import QMessageBox, QInputDialog, QLineEdit

class ServicioAcceso:
    def confirmar_administrador(self) -> bool:
        respuesta = QMessageBox.question(
            None,
            "Acceso",
            "¿Eres el administrador?",
            QMessageBox.Yes | QMessageBox.No
        )
        return respuesta == QMessageBox.Yes

    def pedir_contraseña(self) -> str:
        password, ok = QInputDialog.getText(
            None,
            "Verificación de Administrador",
            "Introduce la contraseña:",
            QLineEdit.Password
        )
        return password if ok else None

    def mostrar_error(self, mensaje: str):
        QMessageBox.critical(None, "Error", mensaje)