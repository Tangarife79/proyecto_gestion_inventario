# from Repositorios.repositorio_inventario import (
#     insertar_cliente,
#     obtener_inventario,
#     actualizar_precio_producto,
#     eliminar_categoria
# )
# from Entidades.cliente_dto import ClienteDTO

# def prueba_insert():
#     cliente = ClienteDTO()
#     cliente.set_nombre("Cliente Nuevo")
#     cliente.set_correo("nuevo@cliente.com")
#     cliente.set_telefono("555123456")
    
#     insertar_cliente(cliente)
#     print("Cliente insertado correctamente.")

# def prueba_select():
#     inventario = obtener_inventario()
#     print("Inventario actual:")
#     for fila in inventario:
#         print(f"Producto: {fila[0]}, Categoría: {fila[1]}, Cantidad: {fila[2]}, Ubicación: {fila[3]}")

# def prueba_update():
#     id_producto = 1
#     nuevo_precio = 199.99
#     actualizar_precio_producto(id_producto, nuevo_precio)
#     print(f"Precio actualizado para producto con ID {id_producto}.")

# def prueba_delete():
#     id_categoria = 5  # asegurarse que esta categoría no tenga productos asociados
#     eliminar_categoria(id_categoria)
#     print(f"Categoría con ID {id_categoria} eliminada (si no tenía productos).")

# if __name__ == "__main__":
#     print("Pruebas CRUD de Inventario\n")
    
#     prueba_insert()
#     print("\n--------------------------\n")
    
#     prueba_select()
#     print("\n--------------------------\n")
    
#     prueba_update()
#     print("\n--------------------------\n")
    
#     prueba_delete()
#     print("\n--------------------------\n")


from Utilidades.Configuracion import obtener_conexion

def probar_insertar_cliente():
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.callproc('InsertarCliente', ['Juan Pérez', 'juan@example.com', '123456789'])
        conexion.commit()
        print("Cliente insertado correctamente.")
    except Exception as e:
        print("Error al insertar cliente:", e)
    finally:
        cursor.close()
        conexion.close()

def probar_obtener_inventario():
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.callproc('ObtenerInventario')
        
        for result in cursor.stored_results():
            inventario = result.fetchall()
            print("Inventario:")
            for fila in inventario:
                print(f"Producto: {fila[0]}, Categoría: {fila[1]}, Cantidad: {fila[2]}, Ubicación: {fila[3]}")
    except Exception as e:
        print("Error al obtener inventario:", e)
    finally:
        cursor.close()
        conexion.close()

def probar_actualizar_precio_producto(id_producto, nuevo_precio):
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.callproc('ActualizarPrecioProducto', [id_producto, nuevo_precio])
        conexion.commit()
        print(f"Precio actualizado para producto ID {id_producto}.")
    except Exception as e:
        print("Error al actualizar precio:", e)
    finally:
        cursor.close()
        conexion.close()

def probar_eliminar_categoria(id_categoria):
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.callproc('EliminarCategoria', [id_categoria])
        conexion.commit()
        print(f"Categoría con ID {id_categoria} eliminada")
    except Exception as e:
        print("Error al eliminar categoría:", e)
    finally:
        cursor.close()
        conexion.close()


if __name__ == "__main__":
    print("=== Probando procedimientos almacenados ===")
    
    # INSERT
    probar_insertar_cliente()
    
    # SELECT
    probar_obtener_inventario()
    
    # UPDATE (ajustar el ID y el precio del producto según la base de datos)
    probar_actualizar_precio_producto(1, 199000.00)
    
    # DELETE (ajustar el ID según la categoría 'vacío' sin relaciones)
    probar_eliminar_categoria(6)
