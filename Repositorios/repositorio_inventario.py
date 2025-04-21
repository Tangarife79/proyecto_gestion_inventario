from Utilidades.Configuracion import obtener_conexion
from Entidades.cliente_dto import ClienteDTO
from Entidades.producto_dto import ProductoDTO
from Entidades.inventario_dto import InventarioDTO

class RepositorioInventario:

    def insertar_cliente(self, cliente: ClienteDTO):
        conexion = obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                cursor.callproc("InsertarCliente", [
                    cliente.get_nombre(),
                    cliente.get_correo(),
                    cliente.get_telefono()
                ])
            conexion.commit()
        finally:
            conexion.close()

    def obtener_inventario(self) -> list:
        conexion = obtener_conexion()
        inventario = []
        try:
            with conexion.cursor() as cursor:
                cursor.callproc("ObtenerInventario")
                for resultado in cursor.stored_results():
                    for fila in resultado.fetchall():
                        item = InventarioDTO()
                        item.set_producto(fila[0])
                        item.set_categoria(fila[1])
                        item.set_cantidad(fila[2])
                        item.set_ubicacion(fila[3])
                        inventario.append(item)
        finally:
            conexion.close()
        return inventario

    def actualizar_precio_producto(self, producto: ProductoDTO):
        conexion = obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                cursor.callproc("ActualizarPrecioProducto", [
                    producto.get_id(),
                    producto.get_precio()
                ])
            conexion.commit()
        finally:
            conexion.close()

    def eliminar_categoria(self, id_categoria: int):
        conexion = obtener_conexion()
        try:
            with conexion.cursor() as cursor:
                cursor.callproc("EliminarCategoria", [id_categoria])
            conexion.commit()
        finally:
            conexion.close()
