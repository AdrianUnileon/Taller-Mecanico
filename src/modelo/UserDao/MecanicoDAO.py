from src.modelo.conexion.Conexion import Conexion
from datetime import date

class MecanicoDao:
    def __init__(self):
        self.conexion = Conexion()  
        self.conn = self.conexion.createConnection()

    def crear_mecanico(self, id_usuario: int, especialidad: str = "General", FechaContratacion = None ):
        """Crea un nuevo registro en la tabla Mecanicos"""
        cursor = None
        try:
            cursor = self.conn.cursor()
            query = """
                INSERT INTO Mecanicos (IDUsuario, Especialidad, FechaContratacion)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (
                id_usuario,
                especialidad,
                FechaContratacion
            ))
            self.conn.commit()
            return cursor.lastrowid
        except Exception as e:
            print("Error al crear mecánico:", e)
            self.conn.rollback()
            return 0
        finally:
            if cursor: 
                cursor.close()

    def obtener_mecanicos_disponibles(self) -> list[dict]:
        """Devuelve mecánicos que no tienen una orden 'Asignada' activa"""
        cursor = None
        try:
            cursor = self.conn.cursor(dictionary=True)
            
            query = """
                SELECT m.IDMecanico, u.Nombre, u.Apellidos, m.Especialidad
                FROM Mecanicos m
                JOIN Usuarios u ON m.IDUsuario = u.IDUsuario
                WHERE m.IDMecanico NOT IN (
                    SELECT os.IDMecanico
                    FROM OrdenesServicio os
                    WHERE os.Estado = 'Asignada'
                )
            """
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print("Error al obtener mecánicos disponibles:", e)
            return []
        finally:
            if cursor: 
                cursor.close()
            