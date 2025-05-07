from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.UserVO import UserVO
from typing import List

class UserDao(Conexion):
    
    def __init__(self):
        super().__init__()

    def select(self) -> List[UserVO]:
        cursor = self.getCursor()
        usuario = []

        #try:

        
        #except Exception as e:
            #print('e')

        """
        Recupera todos los usuarios de la base de datos.
        
        Returns:
            list[UserVO]: Una lista de objetos UserVO.
        
        Raises:
            SQLException: Si hay un error al ejecutar la consulta.
            Exception: Para otros errores inesperados.
        """
        raise NotImplementedError("Método select() no implementado")

    def insert(self, usuarios: UserVO) -> int:
        """
        Inserta un nuevo usuario en la base de datos.

        Args:
            user (UserVO): El objeto UserVO a insertar.

        Returns:
            int: El ID del usuario insertado.

        Raises:
            SQLException: Si hay un error al ejecutar la inserción.
        """
        raise NotImplementedError("Método insert() no implementado")