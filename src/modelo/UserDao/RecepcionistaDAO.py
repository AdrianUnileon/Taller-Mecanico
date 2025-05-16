from src.modelo.conexion.Conexion import Conexion
class RecepcionistaDAO:
    def __init__(self):
        self.conexion = Conexion()
        self.conn = self.conexion.createConnection()

    def crear_recepcionista(self, id_usuario: int, turno: str=None) -> int:
        cursor = None
        try:
            cursor = self.conn.cursor()
            query = """
                INSERT INTO Recepcionistas (IDUsuario, Turno)
                VALUES (%s, CURDATE())
            """
            cursor.execute(query, (id_usuario, turno))
            self.conn.commit()
            return cursor.lastrowid
        except Exception as e:
            print("Error al crear recepcionista:", e)
            self.conn.rollback()
            return 0
        finally:
            if cursor:
                cursor.close()
