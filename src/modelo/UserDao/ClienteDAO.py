from src.modelo.conexion.Conexion import Conexion
from src.modelo.vo.ClienteVO import ClienteVO

class ClienteDao(Conexion):

    def _obtener_siguiente_id_cliente(self):
        conn = self.createConnection()
        cursor = conn.cursor()
        cursor.execute("SELECT MAX(IDCliente) FROM Clientes")
        resultado = cursor.fetchone()
        cursor.close()
        self.closeConnection()
        return (resultado[0] or 0) + 1  # Si es None (tabla vacía), empieza en 1

    def insertar(self, cliente: ClienteVO) -> int:
        conn = self.createConnection()
        cursor = conn.cursor()

        # Generar IDCliente manualmente
        nuevo_id_cliente = self._obtener_siguiente_id_cliente()

        query = "INSERT INTO Clientes (IDCliente, IDUsuario, Direccion, Contacto) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (nuevo_id_cliente, cliente.IDUsuario, cliente.Direccion, cliente.Telefono))
        conn.commit()

        cursor.close()
        self.closeConnection()
        return nuevo_id_cliente  # ya que no hay AUTO_INCREMENT, devolvemos el que generamos
