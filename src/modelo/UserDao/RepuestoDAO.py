from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.RepuestoVO import RepuestoVO
import mysql.connector

class RepuestoDAO:
    def __init__(self):
        self.conn = Conexion().createConnection()

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
        cursor.execute("DELETE FROM detallepedidos WHERE IDRepuesto = %s", (id_repuesto,))
        cursor.execute("DELETE FROM Repuestos WHERE IDRepuesto = %s", (id_repuesto,))
        self.conn.commit()
        cursor.close()

    def obtener_id_por_nombre(self, nombre_repuesto: str):
        cursor = None
        try:
            cursor = self.conn.cursor()
            query = "SELECT IDRepuesto FROM Repuestos WHERE Nombre = %s"
            cursor.execute(query, (nombre_repuesto,))
            resultado = cursor.fetchone()
            return resultado[0] if resultado else None
        except mysql.connector.Error as err:
            print(f"Error al obtener ID del repuesto: {err}")
            return None
        finally:
            if cursor:
                cursor.close()
                
    def insertar_repuesto(self, nombre, cantidad=0, ubicacion='Pendiente', precio_unitario=0.0, id_proveedor=None):
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
                nombre,
                cantidad,
                ubicacion,
                precio_unitario,
                id_proveedor
            ))
            self.conn.commit()
            return next_id
        except mysql.connector.Error as err:
            print(f"Error al insertar repuesto: {err}")
            self.conn.rollback()
            return None
        finally:
            if cursor:
                cursor.close()


