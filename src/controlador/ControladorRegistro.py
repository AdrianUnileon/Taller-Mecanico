from src.modelo.vo.UserVO import UserVO
from src.modelo.UserDao.UserDAOJDBC import UserDaoJDBC
from src.modelo.UserDao.ClienteDAO import ClienteDao
from src.modelo.vo.ClienteVO import ClienteVO
from src.modelo.UserDao.RecepcionistaDAO import RecepcionistaDAO
from src.modelo.vo.RecepcionistaVO import RecepcionistaVO
from src.modelo.UserDao.MecanicoDAO import MecanicoDAO
from src.modelo.vo.MecanicoVO import MecanicoVO

class ControladorRegistro:
    def __init__(self):
        self.user_dao = UserDaoJDBC()

    def registrar_usuario(self, datos):
        if self.user_dao.buscar_por_email(datos["correo"]):
            return False, "El correo ya está registrado."

        nuevo_usuario = UserVO(
            DNI=datos["dni"],
            Nombre=datos["nombre"],
            Apellidos=datos["apellidos"],
            Correo=datos["correo"],
            Contraseña=datos["password"],
            TipoUsuario=datos["tipo"]
        )

        id_generado = self.user_dao.insert(nuevo_usuario)

        if id_generado:
            nuevo_usuario.IDUsuario = id_generado
            return True, nuevo_usuario
        return False, "Error al registrar el usuario en la base de datos."

    def registrar_cliente(self, id_usuario, direccion, contacto):
        cliente = ClienteVO(IDUsuario=id_usuario, Direccion=direccion, Contacto=contacto)
        return ClienteDao().insertar(cliente)

    def registrar_mecanico(self, id_usuario, especialidad, fecha):
        mecanico = MecanicoVO(IDUsuario=id_usuario, Especialidad=especialidad, FechaContratacion=fecha)
        return MecanicoDAO().insertar(mecanico)

    def registrar_recepcionista(self, id_usuario, turno):
        recepcionista = RecepcionistaVO(IDUsuario=id_usuario, Turno=turno)
        return RecepcionistaDAO().insertar(recepcionista)

