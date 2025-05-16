from src.modelo.conexion.Conexion import Conexion

class OrdenDao(Conexion):
    def __init__(self):
        self.conn = Conexion().createConnection()

    def obtener_ordenes_pendientes(self) -> list[dict]:
        """
        Devuelve las órdenes de servicio que están en estado 'Pendiente'
        """
        cursor = None
        try:
            cursor = self.conn.cursor(dictionary=True)

            query = """
                SELECT os.IDOrden, os.FechaIngreso, os.Descripcion, u.Nombre AS NombreCliente, v.Matricula
                FROM OrdenesServicio os
                JOIN Vehiculos v ON os.IDVehiculo = v.IDVehiculo
                JOIN Usuarios u ON v.IDUsuario = u.IDUsuario
                WHERE os.Estado = 'Pendiente'
            """
            cursor.execute(query)
            return cursor.fetchall()

        except Exception as e:
            print("Error al obtener órdenes pendientes:", e)
            return []
        finally:
            if cursor: cursor.close()
            if self.conn: self.closeConnection()
