from src.modelo.conexion.Conexion import Conexion

class MecanicoDao(Conexion):
    def __init__(self):
        super().__init__()

    def obtener_mecanicos_disponibles(self) -> list[dict]:
        """
        Devuelve mecánicos que no tienen una orden 'Asignada' activa
        """
        conn = None
        cursor = None
        try:
            conn = self.createConnection()
            cursor = conn.cursor(dictionary=True)
            
            query = """
                SELECT m.IDMecanico, u.Nombre, u.Apellidos
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
            if cursor: cursor.close()
            if conn: self.closeConnection()
