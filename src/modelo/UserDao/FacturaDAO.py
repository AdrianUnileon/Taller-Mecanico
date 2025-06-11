from src.modelo.vo.FacturaVO import FacturaVO
from src.modelo.conexion.Conexion import Conexion
from datetime import datetime
import jpype
import jpype.imports
from java.sql import Date as JavaSqlDate


class FacturaDAO(Conexion):

    def insertar_factura(self, factura: FacturaVO) -> int:
        cursor = None
        try:
            cursor = self.getCursor()
            cursor.execute("SELECT MAX(IDFactura) FROM facturas")
            result = cursor.fetchone()
            next_id = (result[0] or 0) + 1

            if isinstance(factura.Fecha, datetime):
                java_fecha = JavaSqlDate.valueOf(factura.Fecha.strftime("%Y-%m-%d"))
            else:
                raise ValueError("La fecha debe ser un objeto datetime")

            query = """
                INSERT INTO facturas (IDFactura, Fecha, Total, IDOrden, IDRecepcionista)
                VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                next_id,
                java_fecha,
                factura.Total,
                factura.IDOrden,
                factura.IDRecepcionista
            ))
            self.conexion.jconn.commit()
            return next_id

        except Exception as e:
            print(f"Error al insertar factura: {e}")
            try:
                self.conexion.jconn.rollback()
            except Exception as rollback_error:
                print(f"Error en rollback: {rollback_error}")
            return 0
        finally:
            if cursor:
                cursor.close()

    def obtener_ordenes_finalizadas(self):
        cursor = None
        try:
            cursor = self.getCursor()
            query = '''
                SELECT 
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
                AND o.IDOrden NOT IN (SELECT IDOrden FROM facturas)
            '''
            cursor.execute(query)
            resultados = cursor.fetchall()
            columnas = [desc[0] for desc in cursor.description]
            return [dict(zip(columnas, fila)) for fila in resultados]
        except Exception as e:
            print(f"Error al obtener órdenes finalizadas: {e}")
            return []
        finally:
            if cursor:
                cursor.close()

    def generar_factura_por_orden(self, id_orden: int, precio_sin_iva_y_beneficio: float, id_recepcionista: int) -> bool:
        cursor = None
        try:
            cursor = self.getCursor()
            cursor.execute("SELECT MAX(IDFactura) FROM facturas")
            result = cursor.fetchone()
            next_id = (result[0] or 0) + 1

            fecha_actual = JavaSqlDate.valueOf(datetime.now().strftime('%Y-%m-%d'))

            query = """
                INSERT INTO facturas (IDFactura, Fecha, Total, IDOrden, IDRecepcionista)
                VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                next_id,
                fecha_actual,
                precio_sin_iva_y_beneficio,
                id_orden,
                id_recepcionista
            ))

            self.conexion.jconn.commit()
            return True

        except Exception as e:
            print(f"Error al generar factura: {e}")
            try:
                self.conexion.jconn.rollback()
            except Exception as rollback_error:
                print(f"Error en rollback: {rollback_error}")
            return False
        finally:
            if cursor:
                cursor.close()