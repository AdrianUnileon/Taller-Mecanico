from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.RepuestoVO import RepuestoVO
import jpype
import jpype.imports


class RepuestoDAO(Conexion):

    def insertar(self, repuesto: RepuestoVO) -> int:
        cursor = None
        try:
            cursor = self.getCursor()
            cursor.execute("SELECT MAX(IDRepuesto) FROM Repuestos")
            result = cursor.fetchone()
            next_id = (result[0] or 0) + 1

            query = """
                INSERT INTO Repuestos (IDRepuesto, Nombre, Cantidad, Ubicacion, PrecioUnitario, IDProveedor)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                next_id,
                repuesto.Nombre,
                repuesto.Cantidad,
                repuesto.Ubicacion,
                repuesto.PrecioUnitario,
                repuesto.IDProveedor
            ))
            self.conexion.jconn.commit()
            return next_id

        except Exception as e:
            print(f"Error al insertar repuesto: {e}")
            try:
                self.conexion.jconn.rollback()
            except Exception as rollback_err:
                print(f"Error al hacer rollback: {rollback_err}")
            return 0
        finally:
            if cursor:
                cursor.close()

    def obtener_todos(self):
        cursor = None
        try:
            cursor = self.getCursor()
            cursor.execute("SELECT * FROM Repuestos")
            rows = cursor.fetchall()
            columnas = [desc[0] for desc in cursor.description]
            return [RepuestoVO(**dict(zip(columnas, row))) for row in rows]
        except Exception as e:
            print(f"Error al obtener todos los repuestos: {e}")
            return []
        finally:
            if cursor:
                cursor.close()

    def modificar_repuesto(self, id_repuesto, nombre, nuevo_cantidad, nueva_ubicacion, nuevo_precio):
        cursor = None
        try:
            cursor = self.getCursor()
            cursor.execute("""
                UPDATE Repuestos
                SET Cantidad = ?, Ubicacion = ?, PrecioUnitario = ?
                WHERE IDRepuesto = ? AND Nombre = ?
            """, (nuevo_cantidad, nueva_ubicacion, nuevo_precio, id_repuesto, nombre))
            self.conexion.jconn.commit()
        except Exception as e:
            print(f"Error al modificar repuesto: {e}")
            try:
                self.conexion.jconn.rollback()
            except Exception as rollback_err:
                print(f"Error en rollback: {rollback_err}")
        finally:
            if cursor:
                cursor.close()

    def eliminar(self, id_repuesto: int):
        cursor = None
        try:
            cursor = self.getCursor()
            cursor.execute("DELETE FROM detallepedidos WHERE IDRepuesto = ?", (id_repuesto,))
            cursor.execute("DELETE FROM Repuestos WHERE IDRepuesto = ?", (id_repuesto,))
            self.conexion.jconn.commit()
        except Exception as e:
            print(f"Error al eliminar repuesto: {e}")
            try:
                self.conexion.jconn.rollback()
            except Exception as rollback_err:
                print(f"Error en rollback: {rollback_err}")
        finally:
            if cursor:
                cursor.close()

    def obtener_id_por_nombre(self, nombre_repuesto: str):
        cursor = None
        try:
            cursor = self.getCursor()
            query = "SELECT IDRepuesto FROM Repuestos WHERE Nombre = ?"
            cursor.execute(query, (nombre_repuesto,))
            resultado = cursor.fetchone()
            return resultado[0] if resultado else None
        except Exception as e:
            print(f"Error al obtener ID del repuesto: {e}")
            return None
        finally:
            if cursor:
                cursor.close()

    def insertar_repuesto(self, nombre, cantidad=0, ubicacion='Pendiente', precio_unitario=0.0, id_proveedor=None):
        cursor = None
        try:
            cursor = self.getCursor()
            cursor.execute("SELECT MAX(IDRepuesto) FROM Repuestos")
            result = cursor.fetchone()
            next_id = (result[0] or 0) + 1

            query = """
                INSERT INTO Repuestos (IDRepuesto, Nombre, Cantidad, Ubicacion, PrecioUnitario, IDProveedor)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                next_id,
                nombre,
                cantidad,
                ubicacion,
                precio_unitario,
                id_proveedor
            ))
            self.conexion.jconn.commit()
            return next_id
        except Exception as e:
            print(f"Error al insertar repuesto: {e}")
            try:
                self.conexion.jconn.rollback()
            except Exception as rollback_err:
                print(f"Error al hacer rollback: {rollback_err}")
            return None
        finally:
            if cursor:
                cursor.close()


