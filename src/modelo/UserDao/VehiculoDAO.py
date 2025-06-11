from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.VehiculoVO import VehiculoVO

class VehiculoDAO(Conexion):

    def insertar(self, vehiculo: VehiculoVO) -> int:
        try:
            cursor = self.getCursor()
            cursor.execute("SELECT MAX(IDVehiculo) FROM Vehiculos")
            result = cursor.fetchone()
            next_id = (result[0] or 0) + 1

            query = """
                INSERT INTO Vehiculos (IDVehiculo, Matricula, Marca, Modelo, Año, IDCliente)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                next_id,
                vehiculo.Matricula, 
                vehiculo.Marca,
                vehiculo.Modelo,
                vehiculo.Anio,
                vehiculo.IDCliente
            ))
            self.conexion.jconn.commit()
            return next_id
        except Exception as e:
            print(f"Error en insertar vehículo: {e}")
            try:
                self.conexion.jconn.rollback()
            except Exception as rollback_error:
                print(f"Error al hacer rollback: {rollback_error}")
            return 0
        finally:
            if cursor:
                cursor.close()

    def select(self) -> list[dict]:
        try:
            cursor = self.getCursor()
            query = "SELECT * FROM Vehiculos"
            cursor.execute(query)
            resultados = cursor.fetchall()
            columnas = [desc[0] for desc in cursor.description]
            return [dict(zip(columnas, fila)) for fila in resultados]
        except Exception as e:
            print(f"Error en select de VehiculoDAO: {e}")
            return []
        finally:
            if cursor:
                cursor.close()

    def buscar_por_matricula(self, matricula: str) -> VehiculoVO | None:
        try:
            cursor = self.getCursor()
            query = "SELECT * FROM Vehiculos WHERE Matricula = ?"
            cursor.execute(query, (matricula,))
            row = cursor.fetchone()
            if row:
                columnas = [desc[0] for desc in cursor.description]
                return VehiculoVO(**dict(zip(columnas, row)))
            return None
        except Exception as e:
            print(f"Error en buscar_por_matricula: {e}")
            return None
        finally:
            if cursor:
                cursor.close()

    def obtener_vehiculos_con_clientes(self) -> list[dict]:
        try:
            cursor = self.getCursor()
            query = """
                SELECT v.IDVehiculo, v.Matricula, v.Marca, v.Modelo, u.Nombre AS NombreCliente
                FROM Vehiculos v
                JOIN Clientes c ON v.IDCliente = c.IDCliente
                JOIN Usuarios u ON c.IDUsuario = u.IDUsuario
                ORDER BY v.IDVehiculo
            """
            cursor.execute(query)
            resultados = cursor.fetchall()
            columnas = [desc[0] for desc in cursor.description]
            return [dict(zip(columnas, fila)) for fila in resultados]
        except Exception as e:
            print(f"Error en obtener_vehiculos_con_clientes: {e}")
            return []
        finally:
            if cursor:
                cursor.close()
    def obtener_vehiculos_sin_ordenes(self) -> list[dict]:
        cursor = None
        try:
            cursor = self.getCursor()  # Usa el cursor de JayDeBeApi
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
            
            # Obtener nombres de columnas
            columnas = [desc[0] for desc in cursor.description]
            
            # Mapear resultados a diccionarios
            resultados = []
            for fila in cursor.fetchall():
                resultados.append(dict(zip(columnas, fila)))
            
            return resultados
        except Exception as e:
            print(f"Error en obtener_vehiculos_sin_ordenes: {e}")
            return []
        finally:
            if cursor:
                cursor.close()


    def eliminar_vehiculo(self, id_vehiculo: int) -> bool:
        try:
            cursor = self.getCursor()
            query = """
                DELETE FROM vehiculos
                WHERE IDVehiculo = ?
                AND NOT EXISTS (
                    SELECT 1 FROM ordenesservicio
                    WHERE ordenesservicio.IDVehiculo = vehiculos.IDVehiculo
                )
            """
            cursor.execute(query, (id_vehiculo,))
            self.conexion.jconn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar vehículo: {e}")
            try:
                self.conexion.jconn.rollback()
            except Exception as rollback_error:
                print(f"Error al hacer rollback: {rollback_error}")
            return False
        finally:
            if cursor:
                cursor.close()


