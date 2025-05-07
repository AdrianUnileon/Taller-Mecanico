import mysql.connector

class Conexion:
    def __init__(self, host='127.0.0.1', database='Adios', user='bduser', password='bdpass'):
        self._host = host
        self._database = database
        self._user = user
        self._password = password
        self.conexion = self.createConnection()

    def createConnection(self):
        try:
            conexion = mysql.connector.connect(
                host=self._host,
                user=self._user,
                password=self._password,
                database=self._database
            )
            print("✅ Conexión exitosa a la base de datos.")
            return conexion
        except mysql.connector.Error as e:
            print("❌ Error creando conexión:", e)
            return None

    def getCursor(self):
        if self.conexion:
            return self.conexion.cursor()
        else:
            print("⚠️ Conexión no disponible.")
            return None

    def closeConnection(self):
        try:
            if self.conexion and self.conexion.is_connected():
                self.conexion.close()
                print("🔌 Conexión cerrada.")
        except Exception as e:
            print("❌ Error cerrando conexión:", e)
