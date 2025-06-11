from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.OrdenServicioVO import OrdenServicioVO
from typing import Optional, Union

class OrdenServicioDAO(Conexion):

    def insertar(self, orden: OrdenServicioVO) -> int:
        cursor = None
        try:
            cursor = self.getCursor()
            cursor.execute("SELECT MAX(IDOrden) FROM ordenesservicio")
            result = cursor.fetchone()
            next_id = (result[0] or 0) + 1

            query = """
                INSERT INTO ordenesservicio (IDOrden, FechaIngreso, Descripcion, Estado, IDVehiculo, IDMecanico)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                next_id,
                orden.FechaIngreso,
                orden.Descripcion,
                orden.Estado,
                orden.IDVehiculo,
                orden.IDMecanico
            ))
            self.conexion.jconn.commit()
            return next_id
        except Exception as e:
            print(f"Error al insertar orden de servicio: {e}")
            if self.conexion:
                self.conexion.jconn.rollback()
            return 0
        finally:
            if cursor:
                cursor.close()

    def buscar_por_id(self, id_orden: int) -> Optional[OrdenServicioVO]:
        cursor = None
        try:
            cursor = self.getCursor()
            query = "SELECT * FROM ordenesservicio WHERE IDOrden = ?"
            cursor.execute(query, (id_orden,))
            row = cursor.fetchone()
            if row:
                keys = ["IDOrden", "FechaIngreso", "Descripcion", "Estado", "IDVehiculo", "IDMecanico", "CostoManoObra"]
                return OrdenServicioVO(**dict(zip(keys, row)))
            return None
        except Exception as e:
            print(f"Error en buscar_por_id: {e}")
            return None
        finally:
            if cursor:
                cursor.close()

    def select_pendientes(self) -> list[OrdenServicioVO]:
        cursor = None
        try:
            cursor = self.getCursor()
            query = "SELECT * FROM ordenesservicio WHERE Estado = 'Pendiente de asignación'"
            cursor.execute(query)
            rows = cursor.fetchall()
            keys = ["IDOrden", "FechaIngreso", "Descripcion", "Estado", "IDVehiculo", "IDMecanico", "CostoManoObra"]
            return [OrdenServicioVO(**dict(zip(keys, row))) for row in rows]
        except Exception as e:
            print(f"Error en select_pendientes: {e}")
            return []
        finally:
            if cursor:
                cursor.close()

    def asignar_orden(self, id_orden, id_mecanico) -> bool:
        cursor = None
        try:
            cursor = self.getCursor()
            cursor.execute("SELECT 1 FROM Mecanicos WHERE IDMecanico = ?", (id_mecanico,))
            if cursor.fetchone() is None:
                print(f"Mecánico con ID {id_mecanico} no existe.")
                return False

            query = """
                UPDATE ordenesservicio
                SET IDMecanico = ?, Estado = 'Asignada'
                WHERE IDOrden = ?
            """
            cursor.execute(query, (id_mecanico, id_orden))
            self.conexion.jconn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al asignar orden: {e}")
            if self.conexion:
                self.conexion.jconn.rollback()
            return False
        finally:
            if cursor:
                cursor.close()

    def obtener_ordenes_por_mecanico(self, id_mecanico) -> list[dict]:
        cursor = self.getCursor()
        query = '''
            SELECT o.IDOrden, o.FechaIngreso, o.Descripcion, o.Estado,
                   v.Marca, v.Modelo, v.Matricula
            FROM OrdenesServicio o
            JOIN Vehiculos v ON o.IDVehiculo = v.IDVehiculo
            WHERE o.IDMecanico = ? AND o.Estado = 'Asignada'
        '''
        cursor.execute(query, (id_mecanico,))
        results = cursor.fetchall()
        cursor.close()
        return [
            {
                "IDOrden": row[0], "FechaIngreso": row[1], "Descripcion": row[2],
                "Estado": row[3], "Marca": row[4], "Modelo": row[5], "Matricula": row[6]
            } for row in results
        ]

    def obtener_ordenes_por_cliente(self, id_cliente) -> list[dict]:
        cursor = self.getCursor()
        query = '''
            SELECT o.IDOrden, o.FechaIngreso, o.Descripcion, o.Estado,
                   v.Marca, v.Modelo, v.Matricula
            FROM OrdenesServicio o
            JOIN Vehiculos v ON o.IDVehiculo = v.IDVehiculo
            WHERE v.IDCliente = ?
        '''
        cursor.execute(query, (id_cliente,))
        results = cursor.fetchall()
        cursor.close()
        return [
            {
                "IDOrden": row[0], "FechaIngreso": row[1], "Descripcion": row[2],
                "Estado": row[3], "Marca": row[4], "Modelo": row[5], "Matricula": row[6]
            } for row in results
        ]

    def obtener_ordenesActuales_por_cliente(self, id_cliente) -> list[dict]:
        cursor = self.getCursor()
        query = '''
            SELECT o.IDOrden, o.FechaIngreso, o.Descripcion, o.Estado,
                   v.Marca, v.Modelo, v.Matricula
            FROM OrdenesServicio o
            JOIN Vehiculos v ON o.IDVehiculo = v.IDVehiculo
            WHERE v.IDCliente = ? AND o.Estado = 'Asignada'
        '''
        cursor.execute(query, (id_cliente,))
        results = cursor.fetchall()
        cursor.close()
        return [
            {
                "IDOrden": row[0], "FechaIngreso": row[1], "Descripcion": row[2],
                "Estado": row[3], "Marca": row[4], "Modelo": row[5], "Matricula": row[6]
            } for row in results
        ]

    def actualizar_estado(self, id_orden: int, nuevo_estado: str, costo_mano_obra: Union[float, None] = None) -> bool:
        cursor = None
        try:
            cursor = self.getCursor()
            if nuevo_estado == "Reparada" and costo_mano_obra is not None:
                query = "UPDATE ordenesservicio SET Estado = ?, CostoManoObra = ? WHERE IDOrden = ?"
                cursor.execute(query, (nuevo_estado, costo_mano_obra, id_orden))
            else:
                query = "UPDATE ordenesservicio SET Estado = ? WHERE IDOrden = ?"
                cursor.execute(query, (nuevo_estado, id_orden))
            self.conexion.jconn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar estado: {e}")
            if self.conexion:
                self.conexion.jconn.rollback()
            return False
        finally:
            if cursor:
                cursor.close()