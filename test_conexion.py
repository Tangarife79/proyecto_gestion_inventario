from Utilidades.Configuracion import obtener_conexion

try:
    conexion = obtener_conexion()
    print("Conexión exitosa a la base de datos.")
    conexion.close()
except Exception as e:
    print("Error al conectar:", e)


from Utilidades.Configuracion import obtener_conexion

try:
    conexion = obtener_conexion()
    print("Conexión exitosa a la base de datos.")
    conexion.close()
except Exception as e:
    print("Error al conectar:", e)
