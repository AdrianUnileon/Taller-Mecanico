from src.modelo.vo.ClienteVO import ClienteVO
from src.modelo.conexion.Conexion import Conexion

class ClienteDao(Conexion):

    SQL_INSERT = """
        INSERT INTO Clientes (IDCliente, IDUsuario, Direccion, Contacto)
        VALUES (?, ?, ?, ?)
    """

    SQL_SELECT = """
        SELECT c.IDCliente, c.IDUsuario, c.Direccion, c.Contacto,
               u.Nombre, u.Apellidos
        FROM Clientes c
        JOIN Usuarios u ON c.IDUsuario = u.IDUsuario
    """

    SQL_OBTENER_ID_POR_USUARIO = "SELECT IDCliente FROM Clientes WHERE IDUsuario = ?"

    def _obtener_siguiente_id_cliente(self) -> int:
        try:
            cursor = self.getCursor()
            cursor.execute("SELECT MAX(IDCliente) FROM Clientes")
            resultado = cursor.fetchone()
            return (resultado[0] or 0) + 1
        except Exception as e:
            print("Error al obtener el siguiente ID de cliente:", e)
            return 1
        finally:
            if cursor:
                cursor.close()

    def insertar(self, cliente: ClienteVO) -> int:
        try:
            cursor = self.getCursor()
            nuevo_id_cliente = self._obtener_siguiente_id_cliente()
            cursor.execute(self.SQL_INSERT, (
                nuevo_id_cliente,
                cliente.IDUsuario,
                cliente.Direccion,
                cliente.Contacto
            ))
            self.conexion.jconn.commit()
            return nuevo_id_cliente
        except Exception as e:
            print("Error al insertar cliente:", e)
            try:
                self.conexion.jconn.rollback()
            except Exception as rollback_error:
                print("Error al hacer rollback:", rollback_error)
            return 0
        finally:
            if cursor:
                cursor.close()

    def select(self) -> list:
        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_SELECT)
            return [
                dict(zip([desc[0] for desc in cursor.description], row))
                for row in cursor.fetchall()
            ]
        except Exception as e:
            print("Error al seleccionar clientes:", e)
            return []
        finally:
            if cursor:
                cursor.close()

    def obtener_id_cliente_por_usuario(self, id_usuario: int) -> int | None:
        try:
            cursor = self.getCursor()
            cursor.execute(self.SQL_OBTENER_ID_POR_USUARIO, [id_usuario])
            row = cursor.fetchone()
            return row[0] if row else None
        except Exception as e:
            print("Error en obtener_id_cliente_por_usuario:", e)
            return None
        finally:
            if cursor:
                cursor.close()

