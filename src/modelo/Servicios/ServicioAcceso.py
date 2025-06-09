import os

class ServicioAcceso:
    def __init__(self, password_admin=None):
        self.password_admin = password_admin or os.getenv("ADMIN_PASSWORD", "admin1234")

    def verificar_password(self, password: str) -> bool:
        return password == self.password_admin
