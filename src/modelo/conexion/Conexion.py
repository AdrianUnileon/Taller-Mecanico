import jaydebeapi

class Conexion:
    _instance = None  

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Conexion, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, host='localhost', database='Adios', user='bduser', password='bdpass'):
        if self._initialized:
            return
        if self._initialized:
            return
        self._host = host
        self._database = database
        self._user = user
        self._password = password
        self.conexion = self.createConnection()
        self._initialized = True
        self._initialized = True

    def createConnection(self):
        try:
            jdbc_driver = "com.mysql.cj.jdbc.Driver"
            jar_file = "./lib/mysql-connector-j-9.2.0.jar"
            self.conexion = jaydebeapi.connect(
                jdbc_driver,
                f"jdbc:mysql://{self._host}/{self._database}",
                [self._user, self._password],
                jar_file
            )
            self.conexion.jconn.setAutoCommit(False)
            return self.conexion
        except Exception as e:
            print("Error creando conexión:", e)
            return None

    """Un cursor es una estructura de control que permite recorrer los resultados de una 
    consulta SQL y manipular fila por fila los datos recuperados desde una base de datos."""
    def getCursor(self):
        if self.conexion is None:
            self.createConnection()
        return self.conexion.cursor()

    def closeConnection(self):
        try:
            if self.conexion:
                self.conexion.close()
                self.conexion = None
        except Exception as e:
            print("Error cerrando conexión:", e)