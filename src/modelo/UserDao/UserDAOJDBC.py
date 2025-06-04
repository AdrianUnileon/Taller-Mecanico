from src.modelo.vo.UserVO import UserVO
from src.modelo.conexion.Conexion import Conexion
import bcrypt
import mysql.connector

class UserDaoJDBC(Conexion):

    def __init__(self):
        self.conn = Conexion().createConnection()

    SQL_SELECT = "SELECT IDUsuario, DNI, Nombre, Apellidos, Correo, Contraseña, TipoUsuario FROM Usuarios"
    SQL_INSERT = """
        INSERT INTO Usuarios (DNI, Nombre, Apellidos, Correo, Contraseña, TipoUsuario)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    SQL_BUSCAR_POR_EMAIL = "SELECT IDUsuario, DNI, Nombre, Apellidos, Correo, Contraseña, TipoUsuario FROM Usuarios WHERE Correo = %s"

    def select(self) -> list[UserVO]:
        cursor = None
        try:
           
            
            cursor = self.conn.cursor(dictionary=True)  
            cursor.execute(self.SQL_SELECT)
            
            usuarios = []
            for row in cursor.fetchall():
                usuarios.append(
                    UserVO(
                        IDUsuario=row['IDUsuario'],
                        DNI=row['DNI'],
                        Nombre=row['Nombre'],
                        Apellidos=row['Apellidos'],
                        Correo=row['Correo'],
                        Contraseña=row['Contraseña'],
                        TipoUsuario=row['TipoUsuario']
                    )
                )
            return usuarios
            
        except Exception as e:
            print(f"Error en select: {str(e)}")
            return []
        finally:
            if cursor: cursor.close()
            if self.conn: self.closeConnection()

    def insert(self, usuario: UserVO) -> int:
        cursor = None
        try:
        
            cursor = self.conn.cursor()
            password = usuario.Contraseña
           

            hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            query = """
            INSERT INTO Usuarios 
            (DNI, Nombre, Apellidos, Correo, Contraseña, TipoUsuario)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
        
            cursor.execute(query, (
                usuario.DNI,
                usuario.Nombre,
                usuario.Apellidos,
                usuario.Correo,
                hashed_pw,
                usuario.TipoUsuario
            ))
        
            self.conn.commit()
            id_usuario = cursor.lastrowid
            
            if usuario.TipoUsuario.lower() == 'mecanico':
                query_mecanico = """
                INSERT INTO Mecanicos (IDUsuario, Especialidad, FechaContratacion)
                VALUES (%s, %s, CURDATE())
                """
                cursor.execute(query_mecanico, (id_usuario, "General", "24/02/2025"))
                self.conn.commit()

            return id_usuario
            
            
        except mysql.connector.Error as err:
            print(f"Error MySQL en insert: {err}")
            if self.conn: self.conn.rollback()
            return 0
        except Exception as e:
            print(f"Error general en insert: {str(e)}")
            if self.conn: self.conn.rollback()
            return 0
        finally:
            if cursor: cursor.close()
            if self.conn: self.closeConnection()

    def buscar_por_email(self, email: str) -> UserVO | None:
        cursor = None
        try:
            
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(self.SQL_BUSCAR_POR_EMAIL, (email,))
            row = cursor.fetchone()
            
            if row:
                return UserVO(
                    IDUsuario=row['IDUsuario'],
                    DNI=row['DNI'],
                    Nombre=row['Nombre'],
                    Apellidos=row['Apellidos'],
                    Correo=row['Correo'],
                    Contraseña=row['Contraseña'],
                    TipoUsuario=row['TipoUsuario']
                )
            return None
            
        except Exception as e:
            print(f"Error en buscar_por_email: {str(e)}")
            return None
        finally:
            if cursor: cursor.close()
            if self.conn: self.closeConnection()
    
    def obtener_usuarios_tipo(self, tipo: str) -> list[UserVO]:
        cursor = None
        try:

            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(
                "SELECT IDUsuario, DNI, Nombre, Apellidos, Correo, Contraseña, TipoUsuario FROM Usuarios WHERE TipoUsuario = %s",
                (tipo,)
                )
            usuarios = []
            for row in cursor.fetchall():
                usuarios.append(
                    UserVO(
                        IDUsuario=row['IDUsuario'],
                        DNI=row['DNI'],
                        Nombre=row['Nombre'],
                        Apellidos=row['Apellidos'],
                        Correo=row['Correo'],
                        Contraseña=row['Contraseña'],
                        TipoUsuario=row['TipoUsuario']
                    )
                )
            return usuarios

        except Exception as e:
            print(f"Error en obtener_usuarios_tipo: {str(e)}")
            return []
        finally:
            if cursor: cursor.close()
            if self.conn: self.closeConnection()
    
    def select_por_rol(self, rol: str):
        cursor = self.conn.cursor(dictionary=True)
        try:
            query = "SELECT * FROM Usuarios WHERE TipoUsuario = %s"
            cursor.execute(query, (rol,))
            rows = cursor.fetchall()
            return [UserVO(**row) for row in rows]
        finally:
            cursor.close()
            self.closeConnection()


    