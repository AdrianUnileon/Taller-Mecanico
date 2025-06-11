'''from src.modelo.vo.UserVO import UserVO
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

'''
from src.modelo.vo.UserVO import UserVO
from src.modelo.conexion.Conexion import Conexion
import bcrypt

class UserDaoJDBC(Conexion):

    def __init__(self):
        super().__init__()
        self.conn = self.createConnection()

    SQL_SELECT = "SELECT IDUsuario, DNI, Nombre, Apellidos, Correo, Contraseña, TipoUsuario FROM Usuarios"
    SQL_INSERT = """
        INSERT INTO Usuarios (IDUsuario, DNI, Nombre, Apellidos, Correo, Contraseña, TipoUsuario)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    SQL_BUSCAR_POR_EMAIL = "SELECT IDUsuario, DNI, Nombre, Apellidos, Correo, Contraseña, TipoUsuario FROM Usuarios WHERE Correo = ?"

    def select(self) -> list[UserVO]:
        cursor = None
        if self.conn is None:
            print("Error: conexión a la base de datos no inicializada.")
            return []
        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT)
            usuarios = []
            for row in cursor.fetchall():
                usuarios.append(UserVO(*row))
            return usuarios
        except Exception as e:
            print(f"Error en select: {str(e)}")
            return []
        finally:
            if cursor:
                cursor.close()
    
    def generar_nuevo_id(self) -> int:
        try:
            cursor = self.getCursor()
            cursor.execute("SELECT MAX(IDUsuario) FROM Usuarios")
            result = cursor.fetchone()
            nuevo_id = (result[0] or 0) + 1
            return nuevo_id
        except Exception as e:
            print(f"Error generando nuevo ID: {e}")
            return 1  # Fallback
        finally:
            if cursor:
                cursor.close()

    def insert(self, usuario: UserVO) -> int:
        cursor = None
        if self.conn is None:
            print("Error: conexión a la base de datos no inicializada.")
            return 0
        try:
            cursor = self.getCursor()
            hashed_pw = bcrypt.hashpw(usuario.Contraseña.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            nuevo_id = self.generar_nuevo_id()

            cursor.execute(self.SQL_INSERT, (
                nuevo_id,
                usuario.DNI,
                usuario.Nombre,
                usuario.Apellidos,
                usuario.Correo,
                hashed_pw,
                usuario.TipoUsuario
            ))

            # No hay .lastrowid en jaydebeapi, obtén ID manualmente si necesario
            self.conexion.jconn.commit()

        # Si es mecánico, insertamos también en Mecanicos
            if usuario.TipoUsuario.lower() == 'mecanico':
                query_mecanico = """
                INSERT INTO Mecanicos (IDUsuario, Especialidad, FechaContratacion)
                VALUES (?, ?, CURDATE())
                """
                cursor.execute(query_mecanico, (nuevo_id, "General"))
                self.conexion.jconn.commit()

            return nuevo_id
        
        except Exception as e:
            print(f"Error general en insert: {str(e)}")
            try:
                self.conexion.jconn.rollback()
            except Exception as rollback_error:
                print(f"Error al hacer rollback: {rollback_error}")
            return 0
        finally:
            if cursor:
                cursor.close()

    def buscar_por_email(self, email: str) -> UserVO | None:
        cursor = None
        if self.conn is None:
            print("Error: conexión a la base de datos no inicializada.")
            return None
        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_BUSCAR_POR_EMAIL, [email])
            row = cursor.fetchone()
            if row:
                return UserVO(*row)
            return None
        except Exception as e:
            print(f"Error en buscar_por_email: {str(e)}")
            return None
        finally:
            if cursor:
                cursor.close()

    def obtener_usuarios_tipo(self, tipo: str) -> list[UserVO]:
        cursor = None
        if self.conn is None:
            print("Error: conexión a la base de datos no inicializada.")
            return []
        try:
            cursor = self.getCursor()
            cursor.execute(
                "SELECT IDUsuario, DNI, Nombre, Apellidos, Correo, Contraseña, TipoUsuario FROM Usuarios WHERE TipoUsuario = ?",
                [tipo]
            )
            usuarios = [UserVO(*row) for row in cursor.fetchall()]
            return usuarios
        except Exception as e:
            print(f"Error en obtener_usuarios_tipo: {str(e)}")
            return []
        finally:
            if cursor:
                cursor.close()

    def select_por_rol(self, rol: str) -> list[UserVO]:
        cursor = None
        if self.conn is None:
            print("Error: conexión a la base de datos no inicializada.")
            return []
        try:
            cursor = self.getCursor()
            cursor.execute("SELECT * FROM Usuarios WHERE TipoUsuario = ?", [rol])
            return [UserVO(*row) for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error en select_por_rol: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
