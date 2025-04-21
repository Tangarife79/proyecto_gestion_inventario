import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="user_ptyhon",
        password="Clas3s1Nt2024_!",
        database="inventario_db"
    )
