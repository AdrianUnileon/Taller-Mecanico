from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.PedidoVO import PedidoVO
from datetime import datetime

class PedidoDAO(Conexion):

    def obtener_id_proveedor(self, nombre_proveedor: str):
        cursor = None
        try:
            cursor = self.getCursor()
            cursor.execute("SELECT IDProveedor FROM Proveedores WHERE Nombre = ?", (nombre_proveedor,))
            resultado = cursor.fetchone()
            return resultado[0] if resultado else None
        except Exception as e:
            print(f"Error al obtener ID del proveedor: {e}")
            return None
        finally:
            if cursor:
                cursor.close()

    def insertar_pedido(self, id_proveedor: int, fecha: datetime, estado: str = 'pendiente') -> int:
        cursor = None
        try:
            cursor = self.getCursor()
            cursor.execute("SELECT MAX(IDPedido) FROM Pedidos")
            result = cursor.fetchone()
            next_id = (result[0] or 0) + 1

            query = """
                INSERT INTO Pedidos (IDPedido, FechaPedido, Estado, IDProveedor)
                VALUES (?, ?, ?, ?)
            """
            cursor.execute(query, (next_id, fecha.strftime('%Y-%m-%d'), estado, id_proveedor))
            self.conexion.jconn.commit()
            return next_id
        except Exception as e:
            print(f"Error al insertar pedido: {e}")
            try:
                self.conexion.jconn.rollback()
            except Exception as rollback_error:
                print(f"Error en rollback: {rollback_error}")
            return 0
        finally:
            if cursor:
                cursor.close()

    def actualizar_estado_pedido(self, id_pedido: int, nuevo_estado: str):
        cursor = None
        try:
            cursor = self.getCursor()
            query = "UPDATE Pedidos SET Estado = ? WHERE IDPedido = ?"
            cursor.execute(query, (nuevo_estado, id_pedido))
            self.conexion.jconn.commit()
        except Exception as e:
            print(f"Error al actualizar estado del pedido: {e}")
            try:
                self.conexion.jconn.rollback()
            except Exception as rollback_error:
                print(f"Error en rollback: {rollback_error}")
        finally:
            if cursor:
                cursor.close()

    def obtener_pedido_por_id(self, id_pedido: int) -> PedidoVO:
        cursor = None
        try:
            cursor = self.getCursor()
            cursor.execute("SELECT * FROM Pedidos WHERE IDPedido = ?", (id_pedido,))
            pedido = cursor.fetchone()
            if pedido:
                columnas = [desc[0] for desc in cursor.description]
                datos = dict(zip(columnas, pedido))
                return PedidoVO(
                    id_pedido=datos['IDPedido'],
                    fecha_pedido=datos['FechaPedido'],
                    estado=datos['Estado'],
                    id_proveedor=datos['IDProveedor']
                )
            return None
        except Exception as e:
            print(f"Error al obtener pedido: {e}")
            return None
        finally:
            if cursor:
                cursor.close()

    def obtener_todos_los_proveedores(self):
        cursor = None
        try:
            cursor = self.getCursor()
            cursor.execute("SELECT Nombre FROM Proveedores")
            resultados = cursor.fetchall()
            return [r[0] for r in resultados]
        except Exception as e:
            print(f"Error al obtener proveedores: {e}")
            return []
        finally:
            if cursor:
                cursor.close()

    def insertar_detalle_pedido(self, id_pedido, id_repuesto, cantidad, precio_unitario):
        cursor = None
        try:
            cursor = self.getCursor()
            query = """
                INSERT INTO DetallePedidos (IDPedido, IDRepuesto, Cantidad, PrecioUnitario)
                VALUES (?, ?, ?, ?)
            """
            cursor.execute(query, (id_pedido, id_repuesto, cantidad, precio_unitario))
            self.conexion.jconn.commit()
        except Exception as e:
            print(f"Error al insertar detalle de pedido: {e}")
            try:
                self.conexion.jconn.rollback()
            except Exception as rollback_error:
                print(f"Error en rollback: {rollback_error}")
        finally:
            if cursor:
                cursor.close()

    def obtener_pedidos_por_estado(self, estado: str):
        cursor = None
        try:
            cursor = self.getCursor()
            query = """
                SELECT 
                    p.IDPedido AS Pedido,
                    p.FechaPedido,
                    p.Estado,
                    pr.Nombre AS Proveedor
                FROM Pedidos p
                JOIN Proveedores pr ON p.IDProveedor = pr.IDProveedor
                WHERE p.Estado = ?
            """
            cursor.execute(query, (estado,))
            resultados = cursor.fetchall()
            columnas = [desc[0] for desc in cursor.description]
            return [dict(zip(columnas, fila)) for fila in resultados]
        except Exception as e:
            print(f"Error al obtener pedidos por estado: {e}")
            return []
        finally:
            if cursor:
                cursor.close()

    def insertar_orden_repuesto(self, id_pedido, id_repuesto, cantidad):
        cursor = None
        try:
            cursor = self.getCursor()
            query = """
                INSERT INTO OrdenesRepuestos (IDOrden, IDRepuesto, Cantidad)
                VALUES (?, ?, ?)
            """
            cursor.execute(query, (id_pedido, id_repuesto, cantidad))
            self.conexion.jconn.commit()
        except Exception as e:
            print(f"Error al insertar orden de repuesto: {e}")
            try:
                self.conexion.jconn.rollback()
            except Exception as rollback_error:
                print(f"Error en rollback: {rollback_error}")
        finally:
            if cursor:
                cursor.close()
