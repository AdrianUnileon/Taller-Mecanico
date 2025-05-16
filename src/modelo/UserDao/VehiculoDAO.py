from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.VehiculoVO import VehiculoVO
import mysql.connector

class VehiculoDAO:

    def __init__(self):
        self.conn = Conexion().createConnection()  # Usar la conexión Singleton

    def insertar(self, vehiculo: VehiculoVO) -> int:
        cursor = None
        try:
            cursor = self.conn.cursor()
        
            # Obtener el máximo IDVehiculo
            cursor.execute("SELECT MAX(IDVehiculo) FROM Vehiculos")
            result = cursor.fetchone()
            next_id = (result[0] or 0) + 1  # Si no hay registros, empieza en 1

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

            self.conn.commit()
            return next_id  # Retorna el ID generado

        except mysql.connector.Error as err:
            print(f"Error MySQL en insertar vehículo: {err}")
            if self.conn:
                self.conn.rollback()
            return 0
        except Exception as e:
            print(f"Error general en insertar vehículo: {e}")
            if self.conn:
                self.conn.rollback()
            return 0
        finally:
            if cursor: cursor.close()
            # No hace falta cerrar la conexión manualmente aquí, la clase Conexion lo maneja

    def select(self) -> list[dict]:
        cursor = None
        try:
            cursor = self.conn.cursor(dictionary=True)
            query = "SELECT * FROM Vehiculos"
            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print(f"Error en select de VehiculoDAO: {e}")
            return []
        finally:
            if cursor: cursor.close()

    def buscar_por_matricula(self, matricula: str) -> VehiculoVO | None:
        cursor = None
        try:
            cursor = self.conn.cursor(dictionary=True)
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
