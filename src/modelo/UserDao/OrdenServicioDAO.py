from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.OrdenServicioVO import OrdenServicioVO
import mysql.connector

class OrdenServicioDAO:
    def __init__(self):
        self.conexion_singleton = Conexion()  # Instancia del Singleton
        self.conn = self.conexion_singleton.createConnection()

    def insertar(self, orden: OrdenServicioVO) -> int:
        cursor = None
        try:
            cursor = self.conn.cursor()
            
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
            self.conn.commit()
            return next_id

        except mysql.connector.Error as err:
            print(f"Error MySQL en insertar orden de servicio: {err}")
            if self.conn:
                self.conn.rollback()
            return 0
        except Exception as e:
            print(f"Error general en insertar orden de servicio: {e}")
            if self.conn:
                self.conn.rollback()
            return 0
        finally:
            if cursor:
                cursor.close()

    def buscar_por_id(self, id_orden: int) -> OrdenServicioVO | None:
        cursor = None
        try:
            cursor = self.conn.cursor(dictionary=True)
            query = "SELECT * FROM ordenesservicio WHERE IDOrden = %s"
            cursor.execute(query, (id_orden,))
            row = cursor.fetchone()
            if row:
                return OrdenServicioVO(**row)
            return None

        except Exception as e:
            print(f"Error en buscar_por_id: {e}")
            return None
        finally:
            if cursor:
                cursor.close()

    def select_pendientes(self):
        cursor = None
        try:
            cursor = self.conn.cursor(dictionary=True)
            query = "SELECT * FROM ordenesservicio WHERE Estado = 'Pendiente de asignación'"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [OrdenServicioVO(**row) for row in rows]
        except Exception as e:
            print(f"Error en select_pendientes: {e}")
            return []
        finally:
            if cursor:
                cursor.close()

    def asignar_orden(self, id_orden, id_mecanico):
        cursor = None
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT 1 FROM Mecanicos WHERE IDMecanico = %s", (id_mecanico,))
            if cursor.fetchone() is None:
                print(f"Mecánico con ID {id_mecanico} no existe.")
                return 0  
            query = """
                UPDATE ordenesservicio
                SET IDMecanico = %s, Estado = 'Asignada'
                WHERE IDOrden = %s
            """
            cursor.execute(query, (id_mecanico, id_orden))
            self.conn.commit()
            return cursor.rowcount > 0

        except mysql.connector.Error as err:
            print(f"Error MySQL en asignar orden: {err}")
            if self.conn:
                self.conn.rollback()
            return False
        finally:
            if cursor:
                cursor.close()
    def obtener_ordenes_por_mecanico(self, id_mecanico):
        cursor = self.conn.cursor(dictionary=True)
        query = '''
            SELECT o.IDOrden, o.FechaIngreso, o.Descripcion, o.Estado,
                   v.Marca, v.Modelo, v.Matricula
            FROM OrdenesServicio o
            JOIN Vehiculos v ON o.IDVehiculo = v.IDVehiculo
            WHERE o.IDMecanico = %s AND o.Estado = 'Asignada'
        '''
        cursor.execute(query, (id_mecanico,))
        resultados = cursor.fetchall()
        cursor.close()
        return resultados


    def __del__(self):
        """Cierra la conexión cuando se destruye la instancia"""
        if hasattr(self, 'conn') and self.conn:
            self.conexion_singleton.closeConnection()

