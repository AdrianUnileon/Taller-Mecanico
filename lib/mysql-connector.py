import pyodbc
from tabulate import tabulate

# Conexión a SQL Server
conexion = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=ADRIÁN\\SQLEXPRESS;'
    'DATABASE=Adios;'
    'Trusted_Connection=yes;'
)

cursor = conexion.cursor()

# Obtener tablas
cursor.execute("""
    SELECT TABLE_NAME 
    FROM INFORMATION_SCHEMA.TABLES 
    WHERE TABLE_TYPE = 'BASE TABLE'
""")
tablas = cursor.fetchall()

for (tabla,) in tablas:
    print(f"\n📄 Tabla: {tabla}")
    cursor.execute(f"""
        SELECT COLUMN_NAME AS 'Nombre de Columna',
               DATA_TYPE AS 'Tipo',
               IS_NULLABLE AS 'Permite NULL'
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = ?
    """, tabla)

    columnas = cursor.fetchall()
    headers = ['Nombre de Columna', 'Tipo', 'Permite NULL']
    print(tabulate(columnas, headers=headers, tablefmt='fancy_grid'))

conexion.close()

'''import mysql.connector

conexion=mysql.connector.connect( host='127.0.0.1', user='bduser', password='bdpass', database = "Hola")
cursor=conexion.cursor()
cursor.execute("show tables")
for base in cursor:
    print(base)
conexion.close()'''


