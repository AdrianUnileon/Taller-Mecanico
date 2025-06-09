from src.modelo.vo.UserVO import UserVO
from src.modelo.vo.ClienteVO import ClienteVO
from src.modelo.UserDao.UserDAOJDBC import UserDaoJDBC
from src.modelo.UserDao.ClienteDAO import ClienteDao

class ServicioRegistroCliente:
    def __init__(self):
        self.dao_usuario = UserDaoJDBC()
        self.dao_cliente = ClienteDao()

    def registrar_cliente(self, nombre, apellido1, apellido2, dni, correo, direccion, contacto) -> dict:
        if not all([nombre, apellido1, apellido2, dni, correo, direccion, contacto]):
            return {"Error": "Por favor, completa todos los campos."}

        if self.dao_usuario.buscar_por_email(correo):
            return {"Error": "Ya existe un usuario con este correo."}

        contraseña_temporal = "1234"

        usuario = UserVO(
            DNI=dni,
            Nombre=nombre,
            Apellidos=f"{apellido1} {apellido2}",
            Correo=correo,
            Contraseña=contraseña_temporal,
            TipoUsuario="Cliente"
        )

        id_usuario = self.dao_usuario.insert(usuario)
        if not id_usuario or id_usuario == 0:
            return {"Error": "No se pudo registrar el usuario."}

        cliente = ClienteVO(
            IDUsuario=id_usuario,
            Direccion=direccion,
            Contacto=contacto
        )

        id_cliente = self.dao_cliente.insertar(cliente)
        if id_cliente > 0:
            return {"Exito": "Cliente registrado correctamente."}
        else:
            return {"Error": "No se pudo registrar el cliente."}
