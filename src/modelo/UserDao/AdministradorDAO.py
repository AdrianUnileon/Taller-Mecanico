from src.modelo.conexion.Conexion import Conexion
import mysql.connector

class AdministradorDAO:
    def __init__(self):
        self.conn = Conexion().createConnection()

    def obtener_por_usuario(self, usuario: str) -> dict:
        """Obtiene un administrador por su nombre de usuario"""
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(
                "SELECT * FROM Administradores WHERE Usuario = %s",
                (usuario,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al obtener admin: {e}")
            return None
        finally:
            cursor.close()

    def insertar_admin(self, usuario: str, contraseña_hash: str, salt: str) -> bool:
        """Inserta un nuevo administrador en la base de datos"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO Administradores (Usuario, ContraseñaHash, Salt) "
                "VALUES (%s, %s, %s)",
                (usuario, contraseña_hash, salt)
            )
            self.conn.commit()
            return cursor.rowcount > 0
        except mysql.connector.Error as err:
            print(f"Error MySQL: {err}")
            self.conn.rollback()
            return False
        finally:
            cursor.close()