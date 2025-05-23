from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.ClienteVO import ClienteVO
import mysql.connector

class ClienteDao:
    def __init__(self):
        self.conn = Conexion().createConnection()

    def _obtener_siguiente_id_cliente(self) -> int:
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT MAX(IDCliente) FROM Clientes")
            resultado = cursor.fetchone()
            cursor.close()
            return (resultado[0] or 0) + 1
        except mysql.connector.Error as e:
            print("Error al obtener el siguiente ID de cliente:", e)
            return 1  
        except Exception as e:
            print("Error general al obtener el siguiente ID de cliente:", e)
            return 1

    def insertar(self, cliente: ClienteVO) -> int:
        cursor = None
        try:
            nuevo_id_cliente = self._obtener_siguiente_id_cliente()

            cursor = self.conn.cursor()
            query = """
                INSERT INTO Clientes (IDCliente, IDUsuario, Direccion, Contacto)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (
                nuevo_id_cliente,
                cliente.IDUsuario,
                cliente.Direccion,
                cliente.Contacto
            ))
            self.conn.commit()
            return nuevo_id_cliente

        except mysql.connector.Error as e:
            print("Error MySQL al insertar cliente:", e)
            if self.conn: self.conn.rollback()
            return 0
        except Exception as e:
            print("Error general al insertar cliente:", e)
            if self.conn: self.conn.rollback()
            return 0
        finally:
            if cursor: cursor.close()

    def select(self) -> list:
        cursor = None
        try:
            cursor = self.conn.cursor(dictionary=True)
            query = """
                SELECT c.IDCliente, c.IDUsuario, c.Direccion, c.Contacto,
                       u.Nombre, u.Apellidos
                FROM Clientes c
                JOIN Usuarios u ON c.IDUsuario = u.IDUsuario
            """
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print("Error al seleccionar clientes:", e)
            return []
        finally:
            if cursor: cursor.close()

    def obtener_id_cliente_por_usuario(self, id_usuario):
        cursor = self.conn.cursor(dictionary=True)
        query = "SELECT * FROM Clientes WHERE IDUsuario = %s"
        cursor.execute(query, (id_usuario,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return row['IDCliente']
        return None

