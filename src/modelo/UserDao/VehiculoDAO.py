from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.VehiculoVO import VehiculoVO
import mysql.connector

class VehiculoDAO(Conexion):
    def insertar(self, vehiculo: VehiculoVO) -> int:
        conn = None
        cursor = None
        try:
            conn = self.createConnection()
            if not conn or not conn.is_connected():
                raise Exception("Error de conexión a MySQL")

            cursor = conn.cursor()
        
        # Obtener el máximo IDVehiculo
            cursor.execute("SELECT MAX(IDVehiculo) FROM Vehiculos")
            result = cursor.fetchone()
            next_id = (result[0] or 0) + 1  # Si no hay registros, empieza en 1
        
        # Consulta corregida (AÑO sin tilde, y 6 parámetros)
            query = """
                INSERT INTO Vehiculos (IDVehiculo, Matricula, Marca, Modelo, Año, IDCliente)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                next_id,               # IDVehiculo (generado manualmente)
                vehiculo.Matricula,    # Matricula (str)
                vehiculo.Marca,        # Marca (str)
                vehiculo.Modelo,       # Modelo (str)
                vehiculo.Anio,         # Año (int)
                vehiculo.IDCliente     # IDCliente (int)
            ))
        
            conn.commit()
            return next_id  # Retorna el ID generado

        except mysql.connector.Error as err:
            print(f"Error MySQL en insertar vehículo: {err}")
            if conn:
                conn.rollback()
            return 0
        except Exception as e:
            print(f"Error general en insertar vehículo: {e}")
            if conn:
                conn.rollback()
            return 0
        finally:
            if cursor: cursor.close()
            if conn: self.closeConnection()

    def select(self) -> list[dict]:
        conn = None
        cursor = None
        try:
            conn = self.createConnection()
            if not conn or not conn.is_connected():
                raise Exception("Error de conexión a MySQL")

            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM Vehiculos"
            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print(f"Error en select de VehiculoDAO: {e}")
            return []
        finally:
            if cursor: cursor.close()
            if conn: self.closeConnection()


    def buscar_por_matricula(self, matricula: str) -> VehiculoVO | None:
        conn = None
        cursor = None
        try:
            conn = self.createConnection()
            if not conn or not conn.is_connected():
                raise Exception("Error de conexión a MySQL")

            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM Vehiculos WHERE Matricula = %s"
            cursor.execute(query, (matricula,))
            row = cursor.fetchone()
            if row:
                return VehiculoVO(**row)
            return None

        except Exception as e:
            print(f"Error en buscar_por_matricula: {e}")
            return None
        finally:
            if cursor: cursor.close()
            if conn: self.closeConnection()
