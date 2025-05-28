from src.modelo.conexion.Conexion import Conexion
import mysql.connector
from datetime import datetime

class PedidoDAO:
    def __init__(self):
        self.conexion_singleton = Conexion()
        self.conn = self.conexion_singleton.createConnection()

    def obtener_id_proveedor(self, nombre_proveedor: str):
        cursor = None
        try:
            cursor = self.conn.cursor()
            query = "SELECT IDProveedor FROM Proveedores WHERE Nombre = %s"
            cursor.execute(query, (nombre_proveedor,))
            resultado = cursor.fetchone()
            return resultado[0] if resultado else None
        except mysql.connector.Error as err:
            print(f"Error al obtener id proveedor: {err}")
            return None
        finally:
            if cursor:
                cursor.close()

    def insertar_pedido(self, id_proveedor: int, fecha: datetime, estado: str = 'pendiente') -> int:
        cursor = None
        try:
            cursor = self.conn.cursor()
            # Obtener próximo ID (si no es auto_increment)
            cursor.execute("SELECT MAX(IDPedido) FROM Pedidos")
            result = cursor.fetchone()
            next_id = (result[0] or 0) + 1

            query = """
                INSERT INTO Pedidos (IDPedido, FechaPedido, Estado, IDProveedor)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (next_id, fecha.strftime('%Y-%m-%d'), estado, id_proveedor))
            self.conn.commit()
            return next_id
        except mysql.connector.Error as err:
            print(f"Error al insertar pedido: {err}")
            self.conn.rollback()
            return 0
        finally:
            if cursor:
                cursor.close()

    def actualizar_estado_pedido(self, id_pedido: int, nuevo_estado: str):
        cursor = None
        try:
            cursor = self.conn.cursor()
            query = "UPDATE Pedidos SET Estado = %s WHERE IDPedido = %s"
            cursor.execute(query, (nuevo_estado, id_pedido))
            self.conn.commit()
        except mysql.connector.Error as err:
            print(f"Error al actualizar estado del pedido: {err}")
            self.conn.rollback()
        finally:
            if cursor:
                cursor.close()

    def obtener_pedido_por_id(self, id_pedido: int):
        cursor = None
        try:
            cursor = self.conn.cursor(dictionary=True)
            query = "SELECT * FROM Pedidos WHERE IDPedido = %s"
            cursor.execute(query, (id_pedido,))
            pedido = cursor.fetchone()
            return pedido
        except mysql.connector.Error as err:
            print(f"Error al obtener pedido: {err}")
            return None
        finally:
            if cursor:
                cursor.close()

    def obtener_todos_los_proveedores(self):
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT Nombre FROM Proveedores")
            resultados = cursor.fetchall()
            return [r[0] for r in resultados]
        except mysql.connector.Error as err:
            print(f"Error al obtener proveedores: {err}")
            return []
        finally:
            if cursor:
                cursor.close()

    def insertar_detalle(self, id_pedido, id_repuesto, cantidad, precio = 0):
        cursor = None
        try:
            cursor = self.conn.cursor()
            query = """
            INSERT INTO detallepedidos (IDPedido, IDRepuesto, Cantidad, PrecioUnitario)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (id_pedido, id_repuesto, cantidad, precio))
            self.conn.commit()
        except mysql.connector.Error as err:
            print(f"Error al insertar detalle de pedido: {err}")
            self.conn.rollback()
        finally:
            if cursor:
                cursor.close()

    def obtener_pedidos_por_estado(self, estado: str):
        cursor = None
        try:
            cursor = self.conn.cursor(dictionary=True)
            query = """
                SELECT 
                    p.IDPedido AS Pedido,
                    p.FechaPedido,
                    p.Estado,
                    pr.Nombre AS Proveedor
                FROM pedidos p
                JOIN proveedores pr ON p.IDProveedor = pr.IDProveedor
                WHERE p.Estado = %s
            """
            cursor.execute(query, (estado,))
            resultados = cursor.fetchall()
            return resultados
        except mysql.connector.Error as err:
            print(f"Error al obtener pedidos por estado: {err}")
            return []
        finally:
            if cursor:
                cursor.close()
