from src.modelo.vo.UserVO import UserVO
from src.modelo.conexion.Conexion import Conexion
import bcrypt
import mysql.connector

class UserDaoJDBC(Conexion):
    SQL_SELECT = "SELECT IDUsuario, DNI, Nombre, Apellidos, Correo, Contraseña, TipoUsuario FROM Usuarios"
    SQL_INSERT = """
        INSERT INTO Usuarios (DNI, Nombre, Apellidos, Correo, Contraseña, TipoUsuario)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    SQL_BUSCAR_POR_EMAIL = "SELECT IDUsuario, DNI, Nombre, Apellidos, Correo, Contraseña, TipoUsuario FROM Usuarios WHERE Correo = %s"

    def select(self) -> list[UserVO]:
        conn = None
        cursor = None
        try:
            conn = self.createConnection()
            if not conn or not conn.is_connected():
                raise Exception("Error de conexión a MySQL")
            
            cursor = conn.cursor(dictionary=True)  # Usar diccionarios para acceso por nombre
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
            if conn: self.closeConnection()

    def insert(self, usuario: UserVO) -> int:
        conn = None
        cursor = None
        try:
            conn = self.createConnection()
            if not conn or not conn.is_connected():
                raise Exception("Error de conexión a MySQL")
        
            cursor = conn.cursor()
        
        # Hashear contraseña
            hashed_pw = bcrypt.hashpw(usuario.Contraseña.encode('utf-8'), bcrypt.gensalt())
        
        # Consulta modificada explícitamente omitiendo IDUsuario
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
        
            conn.commit()
            return cursor.lastrowid  
            
        except mysql.connector.Error as err:
            print(f"Error MySQL en insert: {err}")
            if conn: conn.rollback()
            return 0
        except Exception as e:
            print(f"Error general en insert: {str(e)}")
            if conn: conn.rollback()
            return 0
        finally:
            if cursor: cursor.close()
            if conn: self.closeConnection()

    def buscar_por_email(self, email: str) -> UserVO | None:
        conn = None
        cursor = None
        try:
            conn = self.createConnection()
            if not conn or not conn.is_connected():
                raise Exception("Error de conexión a MySQL")
            
            cursor = conn.cursor(dictionary=True)
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
            if conn: self.closeConnection()