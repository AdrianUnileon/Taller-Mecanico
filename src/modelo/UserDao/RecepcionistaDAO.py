from src.modelo.conexion.Conexion import Conexion
import mysql.connector
from src.modelo.vo.RecepcionistaVO import RecepcionistaVO
class RecepcionistaDAO:
    def __init__(self):
        self.conexion = Conexion()
        self.conn = self.conexion.createConnection()

    def _obtener_siguiente_id_recepcionista(self) -> int:
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT MAX(IDRecepcionista) FROM Recepcionistas")
            resultado = cursor.fetchone()
            cursor.close()
            return (resultado[0] or 0) + 1
        except mysql.connector.Error as e:
            print("Error al obtener el siguiente ID del recepcionista:", e)
            return 1  
        except Exception as e:
            print("Error general al obtener el siguiente ID del recepcionista:", e)
            return 1

    def insertar(self, recepcionista: RecepcionistaVO) -> int:
        cursor = None
        try:
            nuevo_id_recepcionista = self._obtener_siguiente_id_recepcionista()

            cursor = self.conn.cursor()
            query = """
                INSERT INTO Recepcionistas (IDRecepcionista, IDUsuario, Turno)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (
                nuevo_id_recepcionista,
                recepcionista.IDUsuario,
                recepcionista.Turno,
            ))
            self.conn.commit()
            return nuevo_id_recepcionista

        except mysql.connector.Error as e:
            print("Error MySQL al insertar recepcionista:", e)
            if self.conn: self.conn.rollback()
            return 0
        except Exception as e:
            print("Error general al insertar recepcionista:", e)
            if self.conn: self.conn.rollback()
            return 0
        finally:
            if cursor: cursor.close()

    def obtener_id_por_usuario(self, id_usuario):
        cursor = self.conn.cursor()
        query = "SELECT IDRecepcionista FROM recepcionistas WHERE IDUsuario = %s"
        cursor.execute(query, (id_usuario,))
        resultado = cursor.fetchone()
        return resultado[0] if resultado else None
