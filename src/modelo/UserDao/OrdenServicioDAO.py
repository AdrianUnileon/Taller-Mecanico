from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.OrdenServicioVO import OrdenServicioVO
import mysql.connector

class OrdenServicioDAO(Conexion):
    def insertar(self, orden: OrdenServicioVO) -> int:
        conn = None
        cursor = None
        try:
            conn = self.createConnection()
            if not conn or not conn.is_connected():
                raise Exception("Error de conexión a MySQL")

            cursor = conn.cursor()

            # Obtener el siguiente IDOrden
            cursor.execute("SELECT MAX(IDOrden) FROM ordenesservicio")
            result = cursor.fetchone()
            next_id = (result[0] or 0) + 1

            query = """
                INSERT INTO ordenesservicio (IDOrden, FechaIngreso, Descripcion, Estado, IDVehiculo, IDMecanico)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                next_id,
                orden.FechaIngreso,
                orden.Descripcion,
                orden.Estado,
                orden.IDVehiculo,
                orden.IDMecanico
            ))
            conn.commit()
            return next_id

        except mysql.connector.Error as err:
            print(f"Error MySQL en insertar orden de servicio: {err}")
            if conn:
                conn.rollback()
            return 0
        except Exception as e:
            print(f"Error general en insertar orden de servicio: {e}")
            if conn:
                conn.rollback()
            return 0
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.closeConnection()

    def buscar_por_id(self, id_orden: int) -> OrdenServicioVO | None:
        conn = None
        cursor = None
        try:
            conn = self.createConnection()
            if not conn or not conn.is_connected():
                raise Exception("Error de conexión a MySQL")

            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM OrdenesServicio WHERE IDOrden = %s"
            cursor.execute(query, (id_orden,))
            row = cursor.fetchone()
            if row:
                return OrdenServicioVO(**row)
            return None

        except Exception as e:
            print(f"Error en buscar_por_id: {e}")
            return None
        finally:
            if cursor: cursor.close()
            if conn: self.closeConnection()
