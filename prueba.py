from src.modelo.conexion.Conexion import Conexion
conn = Conexion().createConnection()
print("Conexión exitosa!" if conn and conn.is_connected() else "Error de conexión")