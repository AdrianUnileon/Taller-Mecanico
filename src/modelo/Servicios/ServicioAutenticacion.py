import bcrypt
from src.modelo.UserDao.AdministradorDAO import AdministradorDAO

class ServicioAutenticacion:
    def __init__(self):
        self.admin_dao = AdministradorDAO()

    def autenticar_admin(self, usuario: str, password: str) -> bool:
        """
        Autentica un administrador contra la base de datos
        :param usuario: Nombre de usuario
        :param password: Contraseña en texto plano
        :return: True si la autenticación es exitosa
        """
        admin = self.admin_dao.obtener_por_usuario(usuario)
        if not admin:
            return False
            
        return bcrypt.checkpw(password.encode('utf-8'), admin['ContraseñaHash'].encode('utf-8'))

    def crear_admin(self, usuario: str, password: str) -> bool:
        """
        Crea un nuevo administrador en la base de datos
        :param usuario: Nombre de usuario
        :param password: Contraseña en texto plano
        :return: True si la creación fue exitosa
        """
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), salt)
        
        return self.admin_dao.insertar_admin(
            usuario=usuario,
            contraseña_hash=hashed_pw.decode('utf-8'),
            salt=salt.decode('utf-8')
        )