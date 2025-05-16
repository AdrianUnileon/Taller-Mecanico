import mysql.connector

class Conexion:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Conexion, cls).__new__(cls)
            cls._instancia._conexion = None
        return cls._instancia

    def createConnection(self):
        if not self._conexion or not self._conexion.is_connected():
            self._conexion = mysql.connector.connect(
                host="localhost",
                user="bduser",
                password="bdpass",
                database="Adios"
            )
        return self._conexion

    def closeConnection(self):
        if self._conexion and self._conexion.is_connected():
            self._conexion.close()
            self._conexion = None

