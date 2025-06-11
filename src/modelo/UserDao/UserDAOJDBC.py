from src.modelo.vo.UserVO import UserVO
from src.modelo.conexion.Conexion import Conexion
import bcrypt

class UserDaoJDBC(Conexion):

    SQL_SELECT = "SELECT IDUsuario, DNI, Nombre, Apellidos, Correo, Contraseña, TipoUsuario FROM Usuarios"
    SQL_INSERT = """
        INSERT INTO Usuarios (IDUsuario, DNI, Nombre, Apellidos, Correo, Contraseña, TipoUsuario)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    SQL_BUSCAR_POR_EMAIL = "SELECT IDUsuario, DNI, Nombre, Apellidos, Correo, Contraseña, TipoUsuario FROM Usuarios WHERE Correo = ?"

    def select(self) -> list[UserVO]:
        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT)
            return [UserVO(*row) for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error en select: {e}")
            return []
        finally:
            if cursor:
                cursor.close()

    def generar_nuevo_id(self) -> int:
        try:
            cursor = self.getCursor()
            cursor.execute("SELECT MAX(IDUsuario) FROM Usuarios")
            result = cursor.fetchone()
            return (result[0] or 0) + 1
        except Exception as e:
            print(f"Error generando nuevo ID: {e}")
            return 1
        finally:
            if cursor:
                cursor.close()

    def insert(self, usuario: UserVO) -> int:
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
            self.conexion.jconn.commit()

            if usuario.TipoUsuario.lower() == 'mecanico':
                query_mecanico = """
                INSERT INTO Mecanicos (IDUsuario, Especialidad, FechaContratacion)
                VALUES (?, ?, CURDATE())
                """
                cursor.execute(query_mecanico, (nuevo_id, "General"))
                self.conexion.jconn.commit()

            return nuevo_id
        except Exception as e:
            print(f"Error en insert: {e}")
            try:
                self.conexion.jconn.rollback()
            except Exception as rollback_error:
                print(f"Error al hacer rollback: {rollback_error}")
            return 0
        finally:
            if cursor:
                cursor.close()

    def buscar_por_email(self, email: str) -> UserVO | None:
        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_BUSCAR_POR_EMAIL, [email])
            row = cursor.fetchone()
            return UserVO(*row) if row else None
        except Exception as e:
            print(f"Error en buscar_por_email: {e}")
            return None
        finally:
            if cursor:
                cursor.close()

    def obtener_usuarios_tipo(self, tipo: str) -> list[UserVO]:
        try:
            cursor = self.getCursor()
            cursor.execute(
                "SELECT IDUsuario, DNI, Nombre, Apellidos, Correo, Contraseña, TipoUsuario FROM Usuarios WHERE TipoUsuario = ?",
                [tipo]
            )
            return [UserVO(*row) for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error en obtener_usuarios_tipo: {e}")
            return []
        finally:
            if cursor:
                cursor.close()

    def select_por_rol(self, rol: str) -> list[UserVO]:
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

