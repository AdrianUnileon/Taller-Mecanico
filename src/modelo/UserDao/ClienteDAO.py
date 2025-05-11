from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.ClienteVO import ClienteVO

class ClienteDao(Conexion):
    def buscar_por_usuario(self, id_usuario):
        conn = self.createConnection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Clientes WHERE IDUsuario = %s", (id_usuario,))
        row = cursor.fetchone()
        cursor.close()
        self.closeConnection()
        return row

    def insertar(self, cliente: ClienteVO) -> int:
        conn = self.createConnection()
        cursor = conn.cursor()
        query = "INSERT INTO Clientes (IDUsuario, Direccion, Contacto) VALUES (%s, %s, %s)"
        cursor.execute(query, (cliente.IDUsuario, cliente.Direccion, cliente.Contacto))
        conn.commit()
        inserted = cursor.lastrowid
        cursor.close()
        self.closeConnection()
        return inserted
