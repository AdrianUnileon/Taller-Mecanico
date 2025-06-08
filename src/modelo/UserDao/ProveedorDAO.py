from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.ProveedorVO import ProveedorVO
import mysql.connector

class ProveedorDAO:
    def __init__(self):
        self.conn = Conexion().createConnection()

    def insertar(self, proveedor: ProveedorVO) -> int:
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT MAX(IDProveedor) FROM Proveedores")
            result = cursor.fetchone()
            next_id = (result[0] or 0) + 1

            query = """
                INSERT INTO Proveedores (IDProveedor, Nombre, Contacto, Direccion)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (
                next_id,
                proveedor.Nombre,
                proveedor.Contacto,
                proveedor.Direccion
            ))
            self.conn.commit()
            return next_id

        except mysql.connector.Error as err:
            print(f"Error al insertar proveedor: {err}")
            self.conn.rollback()
            return 0
        finally:
            if cursor:
                cursor.close()

    def obtener_todos(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Proveedores")
        rows = cursor.fetchall()
        cursor.close()
        return [ProveedorVO(**row) for row in rows]

    def modificar_proveedor(self, id_proveedor, nombre, nuevo_contacto, nueva_direccion):
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE Proveedores 
            SET Contacto = %s, Direccion = %s 
            WHERE IDProveedor = %s AND Nombre = %s
        """, (nuevo_contacto, nueva_direccion, id_proveedor, nombre))
        self.conn.commit()
        cursor.close()

    def eliminar(self, id_proveedor: int):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Repuestos WHERE IDProveedor = %s", (id_proveedor,))
        cursor.execute("DELETE FROM Proveedores WHERE IDProveedor = %s", (id_proveedor,))
        self.conn.commit()
        cursor.close()

    def obtener_nombres_proveedores(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT Nombre FROM Proveedores")
            resultados = cursor.fetchall()
            return [nombre[0] for nombre in resultados]
        except mysql.connector.Error as err:
            print(f"Error al obtener nombres de proveedores: {err}")
            return []
        finally:
            cursor.close()

    def obtener_id_por_nombre(self, nombre):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT IDProveedor FROM Proveedores WHERE Nombre = %s", (nombre,))
            resultado = cursor.fetchone()
            return resultado[0] if resultado else None
        except mysql.connector.Error as err:
            print(f"Error al obtener ID del proveedor: {err}")
            return None
        finally:
            cursor.close()
