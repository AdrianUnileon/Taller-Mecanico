from src.modelo.vo.FacturaVO import FacturaVO
from src.modelo.conexion.Conexion import Conexion
import mysql.connector

class FacturaDAO:
    def __init__(self):
        self.conn = Conexion().createConnection()

    def insertar_factura(self, factura: FacturaVO) -> int:
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT MAX(IDFactura) FROM facturas")
            result = cursor.fetchone()
            next_id = (result[0] or 0) + 1

            query = """
                INSERT INTO facturas (IDFactura, Fecha, Total, IDOrden, IDRecepcionista)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                next_id,
                factura.Fecha,
                factura.Total,
                factura.IDOrden,
                factura.IDRecepcionista
            ))
            self.conn.commit()
            return next_id

        except mysql.connector.Error as err:
            print(f"Error MySQL al insertar factura: {err}")
            self.conn.rollback()
            return 0
        finally:
            if cursor:
                cursor.close()

    def obtener_ordenes_finalizadas(self):
        cursor = self.conn.cursor(dictionary=True)
        try:
            query = '''SELECT 
                o.IDOrden, 
                o.Descripcion, 
                o.Estado, 
                o.CostoManoObra,
                u.Nombre AS NombreCliente,
                CONCAT(v.Marca, ' ', v.Modelo) AS Vehiculo
                FROM ordenesservicio o
                JOIN vehiculos v ON o.IDVehiculo = v.IDVehiculo
                JOIN clientes c ON v.IDCliente = c.IDCliente
                JOIN usuarios u ON c.IDUsuario = u.IDUsuario
                WHERE o.Estado = 'Reparada'
                    AND o.IDOrden NOT IN (SELECT IDOrden FROM facturas);'''

            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener órdenes finalizadas: {e}")
            return []
        finally:
            cursor.close()

    def generar_factura_por_orden(self, id_orden: int, precio_sin_iva_y_beneficio: float, id_recepcionista: int) -> bool:
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT MAX(IDFactura) FROM facturas")
            result = cursor.fetchone()
            next_id = (result[0] or 0) + 1

            from datetime import datetime
            fecha_actual = datetime.now().strftime('%Y-%m-%d')

            query = """
                INSERT INTO facturas (IDFactura, Fecha, Total, IDOrden, IDRecepcionista)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (next_id, fecha_actual, precio_sin_iva_y_beneficio, id_orden, id_recepcionista))
            self.conn.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print(f"Error MySQL al generar factura: {err}")
            self.conn.rollback()
            if cursor:
                cursor.close()
            return False
