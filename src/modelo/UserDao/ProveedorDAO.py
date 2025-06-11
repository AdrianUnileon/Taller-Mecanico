from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.ProveedorVO import ProveedorVO
import jpype
import jpype.imports


class ProveedorDAO(Conexion):

    def insertar(self, proveedor: ProveedorVO) -> int:
        cursor = None
        try:
            cursor = self.getCursor()
            cursor.execute("SELECT MAX(IDProveedor) FROM Proveedores")
            result = cursor.fetchone()
            next_id = (result[0] or 0) + 1

            query = """
                INSERT INTO Proveedores (IDProveedor, Nombre, Contacto, Direccion)
                VALUES (?, ?, ?, ?)
            """
            cursor.execute(query, (
                next_id,
                proveedor.Nombre,
                proveedor.Contacto,
                proveedor.Direccion
            ))
            self.conexion.jconn.commit()
            return next_id

        except Exception as e:
            print(f"Error al insertar proveedor: {e}")
            try:
                self.conexion.jconn.rollback()
            except Exception as rollback_err:
                print(f"Error en rollback: {rollback_err}")
            return 0
        finally:
            if cursor:
                cursor.close()

    def obtener_todos(self):
        cursor = None
        try:
            cursor = self.getCursor()
            cursor.execute("SELECT * FROM Proveedores")
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            return [ProveedorVO(**dict(zip(columns, row))) for row in rows]
        except Exception as e:
            print(f"Error al obtener todos los proveedores: {e}")
            return []
        finally:
            if cursor:
                cursor.close()

    def modificar_proveedor(self, id_proveedor, nombre, nuevo_contacto, nueva_direccion):
        cursor = None
        try:
            cursor = self.getCursor()
            cursor.execute("""
                UPDATE Proveedores 
                SET Contacto = ?, Direccion = ? 
                WHERE IDProveedor = ? AND Nombre = ?
            """, (nuevo_contacto, nueva_direccion, id_proveedor, nombre))
            self.conexion.jconn.commit()
        except Exception as e:
            print(f"Error al modificar proveedor: {e}")
            try:
                self.conexion.jconn.rollback()
            except Exception as rollback_err:
                print(f"Error en rollback: {rollback_err}")
        finally:
            if cursor:
                cursor.close()

    def eliminar(self, id_proveedor: int):
        cursor = None
        try:
            cursor = self.getCursor()
            cursor.execute("DELETE FROM Repuestos WHERE IDProveedor = ?", (id_proveedor,))
            cursor.execute("DELETE FROM Proveedores WHERE IDProveedor = ?", (id_proveedor,))
            self.conexion.jconn.commit()
        except Exception as e:
            print(f"Error al eliminar proveedor: {e}")
            try:
                self.conexion.jconn.rollback()
            except Exception as rollback_err:
                print(f"Error en rollback: {rollback_err}")
        finally:
            if cursor:
                cursor.close()

    def obtener_nombres_proveedores(self):
        cursor = None
        try:
            cursor = self.getCursor()
            cursor.execute("SELECT Nombre FROM Proveedores")
            resultados = cursor.fetchall()
            return [nombre[0] for nombre in resultados]
        except Exception as e:
            print(f"Error al obtener nombres de proveedores: {e}")
            return []
        finally:
            if cursor:
                cursor.close()

    def obtener_id_por_nombre(self, nombre):
        cursor = None
        try:
            cursor = self.getCursor()
            cursor.execute("SELECT IDProveedor FROM Proveedores WHERE Nombre = ?", (nombre,))
            resultado = cursor.fetchone()
            return resultado[0] if resultado else None
        except Exception as e:
            print(f"Error al obtener ID del proveedor: {e}")
            return None
        finally:
            if cursor:
                cursor.close()