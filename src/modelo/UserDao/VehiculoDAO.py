from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.VehiculoVO import VehiculoVO
import mysql.connector

class VehiculoDAO:

    def __init__(self):
        self.conn = Conexion().createConnection()  

    def insertar(self, vehiculo: VehiculoVO) -> int:
        cursor = None
        try:
            cursor = self.conn.cursor()
        
            cursor.execute("SELECT MAX(IDVehiculo) FROM Vehiculos")
            result = cursor.fetchone()
            next_id = (result[0] or 0) + 1  

            query = """
                INSERT INTO Vehiculos (IDVehiculo, Matricula, Marca, Modelo, Año, IDCliente)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                next_id,               
                vehiculo.Matricula,    
                vehiculo.Marca,        
                vehiculo.Modelo,       
                vehiculo.Anio,         
                vehiculo.IDCliente     
            ))

            self.conn.commit()
            return next_id  

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

    def obtener_vehiculos_con_clientes(self) -> list[dict]:
        cursor = None
        try:
            cursor = self.conn.cursor(dictionary=True)
            query = """
                SELECT v.IDVehiculo, v.Matricula, v.Marca, v.Modelo, u.Nombre AS NombreCliente
                FROM Vehiculos v
                JOIN Clientes c ON v.IDCliente = c.IDCliente
                JOIN Usuarios u ON c.IDUsuario = u.IDUsuario
                ORDER BY v.IDVehiculo
            """
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error en obtener_vehiculos_con_clientes: {e}")
            return []
        finally:
            if cursor: cursor.close()

    def obtener_vehiculos_sin_ordenes(self) -> list[dict]:
        cursor = None
        try:
            cursor = self.conn.cursor(dictionary=True)
            query = """
                SELECT v.IDVehiculo, v.Matricula, v.Marca, v.Modelo, u.Nombre AS NombreCliente
                FROM Vehiculos v
                JOIN Clientes c ON v.IDCliente = c.IDCliente
                JOIN Usuarios u ON c.IDUsuario = u.IDUsuario
                WHERE NOT EXISTS (
                    SELECT 1 FROM ordenesservicio o
                    WHERE o.IDVehiculo = v.IDVehiculo
                )
                ORDER BY v.IDVehiculo
            """
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error en obtener_vehiculos_sin_ordenes: {e}")
            return []
        finally:
            if cursor:
                cursor.close()

    def eliminar_vehiculo(self, id_vehiculo: int) -> bool:
        cursor = None
        try:
            cursor = self.conn.cursor()
            query = """
                DELETE FROM vehiculos
                WHERE IDVehiculo = %s
                AND NOT EXISTS (
                    SELECT 1 FROM ordenesservicio
                    WHERE ordenesservicio.IDVehiculo = vehiculos.IDVehiculo
                )
            """
            cursor.execute(query, (id_vehiculo,))
            self.conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar vehículo: {e}")
            if self.conn:
                self.conn.rollback()
            return False
        finally:
            if cursor:
                cursor.close()
