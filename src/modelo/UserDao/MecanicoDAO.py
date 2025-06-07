from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.MecanicoVO import MecanicoVO
import mysql.connector

class MecanicoDAO:
    def __init__(self):
        self.conexion_singleton = Conexion()  
        self.conn = self.conexion_singleton.createConnection()

    def _obtener_siguiente_id_mecanico(self) -> int:
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT MAX(IDMecanico) FROM Mecanicos")
            resultado = cursor.fetchone()
            cursor.close()
            return (resultado[0] or 0) + 1
        except mysql.connector.Error as e:
            print("Error al obtener el siguiente ID del mecanico:", e)
            return 1  
        except Exception as e:
            print("Error general al obtener el siguiente ID de mecanico:", e)
            return 1

    def insertar(self, mecanico: MecanicoVO) -> int:
        cursor = None
        try:
            nuevo_id_mecanico = self._obtener_siguiente_id_mecanico()

            cursor = self.conn.cursor()
            query = """
                INSERT INTO Mecanicos (IDMecanico, IDUsuario, Especialidad, FechaContratacion)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (
                nuevo_id_mecanico,
                mecanico.IDUsuario,
                mecanico.Especialidad,
                mecanico.FechaContratacion
            ))
            self.conn.commit()
            return nuevo_id_mecanico

        except mysql.connector.Error as e:
            print("Error MySQL al insertar mecanico:", e)
            if self.conn: self.conn.rollback()
            return 0
        except Exception as e:
            print("Error general al insertar mecanico:", e)
            if self.conn: self.conn.rollback()
            return 0
        finally:
            if cursor: cursor.close()

    def obtener_mecanicos_disponibles(self) -> list[dict]:
        """
        Devuelve mecánicos que no tienen una orden 'Asignada' activa
        """
        cursor = None
        try:
            cursor = self.conn.cursor(dictionary=True)
            
            query = """
                SELECT m.IDMecanico, u.Nombre, u.Apellidos
                FROM Mecanicos m
                JOIN Usuarios u ON m.IDUsuario = u.IDUsuario
                WHERE m.IDMecanico NOT IN (
                    SELECT os.IDMecanico
                    FROM ordenesservicio os
                    WHERE os.Estado = 'Asignada'
                )
            """
            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print("Error al obtener mecánicos disponibles:", e)
            return []
        finally:
            if cursor: cursor.close()


    def obtener_id_por_usuario(self, id_usuario: int) -> int:
        cursor = None
        try:
            cursor = self.conn.cursor()
            query = "SELECT IDMecanico FROM Mecanicos WHERE IDUsuario = %s"
            cursor.execute(query, (id_usuario,))
            result = cursor.fetchone()
            return result[0] if result else None
        except Exception as e:
            print(f"Error al obtener ID de mecánico: {e}")
            return None
        finally:
            if cursor: cursor.close()
    
    def obtener_mecanico_por_usuario(self, id_usuario):
        cursor = self.conn.cursor(dictionary=True)
        query = "SELECT * FROM Mecanicos WHERE IDUsuario = %s"
        cursor.execute(query, (id_usuario,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return row['IDMecanico']
        return None

            