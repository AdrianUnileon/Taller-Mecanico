from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.RepuestoVO import RepuestoVO
import mysql.connector

class RepuestoDAO:
    def __init__(self):
        self.conexion_singleton = Conexion()  
        self.conn = self.conexion_singleton.createConnection()

    def insertar(self, repuesto: RepuestoVO) -> int:
        cursor = None
        try:
            cursor = self.conn.cursor()

            cursor.execute("SELECT MAX(IDRepuesto) FROM Repuestos")
            result = cursor.fetchone()
            next_id = (result[0] or 0) + 1

            query = """
                INSERT INTO Repuestos (IDRepuesto, Nombre, Cantidad, Ubicacion, PrecioUnitario, IDProveedor)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                next_id,
                repuesto.Nombre,
                repuesto.Cantidad,
                repuesto.Ubicacion,
                repuesto.PrecioUnitario,
                repuesto.IDProveedor
            ))
            self.conn.commit()
            return next_id

        except mysql.connector.Error as err:
            print(f"Error al insertar repuesto: {err}")
            self.conn.rollback()
            return 0
        finally:
            if cursor:
                cursor.close()

    def obtener_todos(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Repuestos")
        rows = cursor.fetchall()
        cursor.close()
        return [RepuestoVO(**row) for row in rows]

    def modificar_repuesto(self, id_repuesto, nombre, nuevo_cantidad, nueva_ubicacion, nuevo_precio):
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE Repuestos
            SET Cantidad = %s, Ubicacion = %s, PrecioUnitario = %s
            WHERE IDRepuesto = %s AND Nombre = %s
        """, (nuevo_cantidad, nueva_ubicacion, nuevo_precio, id_repuesto, nombre))
        self.conn.commit()
        cursor.close()

    def eliminar(self, id_repuesto: int):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Repuestos WHERE IDRepuesto = %s", (id_repuesto,))
        self.conn.commit()
        cursor.close()
