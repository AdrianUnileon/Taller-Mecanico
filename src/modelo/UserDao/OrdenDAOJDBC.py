from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.OrdenVO import OrdenVO

class OrdenDAOJDBC(Conexion):
    def obtener_ordenes_por_mecanico(self, id_mecanico):
        cursor = self.getCursor()
        ordenes = []
        try:
            sql = "SELECT IDOrden, FechaIngreso, Descripcion, Estado, IDVehiculo FROM OrdenesServicio WHERE IDMecanico = ?"
            cursor.execute(sql, (id_mecanico,))
            rows = cursor.fetchall()
            for row in rows:
                ordenes.append(OrdenVO(
                    id_orden=row[0],
                    fecha=row[1],
                    descripcion=row[2],
                    estado=row[3],
                    id_vehiculo=row[4],
                    id_mecanico=id_mecanico
                ))
        except Exception as e:
            print("Error al obtener órdenes:", e)
        finally:
            cursor.close()
            self.closeConnection()
        return ordenes

    def actualizar_estado(self, id_orden, nuevo_estado):
        cursor = self.getCursor()
        try:
            sql = "UPDATE OrdenesServicio SET Estado = ? WHERE IDOrden = ?"
            cursor.execute(sql, (nuevo_estado, id_orden))
            self.conexion.commit()
            return True
        except Exception as e:
            print("Error al actualizar estado:", e)
            return False
        finally:
            cursor.close()
            self.closeConnection()
