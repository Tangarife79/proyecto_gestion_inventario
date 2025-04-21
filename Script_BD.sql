
CREATE DATABASE inventario_db;
USE inventario_db;


-- TABLAS

CREATE TABLE Categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE Marcas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE Proveedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    correo VARCHAR(100)
);

CREATE TABLE Ubicaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

CREATE TABLE Productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    id_categoria INT,
    id_marca INT,
    id_proveedor INT,
    precio DECIMAL(10,2),
    FOREIGN KEY (id_categoria) REFERENCES Categorias(id),
    FOREIGN KEY (id_marca) REFERENCES Marcas(id),
    FOREIGN KEY (id_proveedor) REFERENCES Proveedores(id)
);

CREATE TABLE Inventario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_producto INT,
    id_ubicacion INT,
    cantidad INT DEFAULT 0,
    FOREIGN KEY (id_producto) REFERENCES Productos(id),
    FOREIGN KEY (id_ubicacion) REFERENCES Ubicaciones(id)
);

CREATE TABLE Entradas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_producto INT,
    cantidad INT,
    fecha DATETIME DEFAULT NOW(),
    FOREIGN KEY (id_producto) REFERENCES Productos(id)
);

CREATE TABLE Salidas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_producto INT,
    cantidad INT,
    fecha DATETIME DEFAULT NOW(),
    FOREIGN KEY (id_producto) REFERENCES Productos(id)
);

CREATE TABLE Roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50)
);

CREATE TABLE Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    usuario VARCHAR(50) UNIQUE,
    contrasena VARCHAR(100),
    id_rol INT,
    FOREIGN KEY (id_rol) REFERENCES Roles(id)
);

CREATE TABLE Clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    correo VARCHAR(100),
    telefono VARCHAR(20)
);

CREATE TABLE Ventas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    fecha DATETIME DEFAULT NOW(),
    total DECIMAL(10,2),
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id)
);

CREATE TABLE DetallesVenta (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_venta INT,
    id_producto INT,
    cantidad INT,
    precio_unitario DECIMAL(10,2),
    FOREIGN KEY (id_venta) REFERENCES Ventas(id),
    FOREIGN KEY (id_producto) REFERENCES Productos(id)
);

CREATE TABLE LogsInventario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_producto INT,
    movimiento VARCHAR(50),
    cantidad INT,
    fecha DATETIME DEFAULT NOW(),
    FOREIGN KEY (id_producto) REFERENCES Productos(id)
);

-- =====================
-- INSERTS PARA LA BASE DE DATOS
-- =====================

-- CATEGORIAS (La última categoría queda sin productos para probar el procedimiento de eliminación)
INSERT INTO Categorias (nombre) VALUES 
('Electrónica'), 
('Papelería'), 
('Muebles'), 
('Herramientas'),
('Vacia');

-- MARCAS
INSERT INTO Marcas (nombre) VALUES 
('HP'), 
('Dell'), 
('Logitech'), 
('Acer'),
('Brosch');

-- PROVEEDORES
INSERT INTO Proveedores (nombre, telefono, correo) VALUES
('Proveedor Uno', '123456789', 'uno@correo.com'),
('Proveedor Dos', '987654321', 'dos@correo.com'),
('Proveedor Tres', '555555555', 'tres@correo.com'),
('Proveedor Cuatro', '444444444', 'cuatro@correo.com');

-- UBICACIONES
INSERT INTO Ubicaciones (nombre) VALUES 
('Almacén Principal'), 
('Sucursal Norte'), 
('Sucursal Sur'), 
('Depósito');

-- PRODUCTOS (ninguno con id_categoria = 5 que es la vacia)
INSERT INTO Productos (nombre, id_categoria, id_marca, id_proveedor, precio) VALUES
('Laptop HP', 1, 1, 1, 2500000.00),
('Monitor Dell', 1, 2, 2, 800000.00),
('Silla Ejecutiva', 3, 4, 3, 600000.00),
('Mouse Logitech', 1, 3, 1, 15000.00);

-- INVENTARIO
INSERT INTO Inventario (id_producto, id_ubicacion, cantidad) VALUES
(1, 1, 10),
(2, 1, 5),
(3, 2, 8),
(4, 3, 15);

-- ENTRADAS
INSERT INTO Entradas (id_producto, cantidad, fecha) VALUES
(1, 5, NOW()),
(2, 3, NOW()),
(3, 7, NOW()),
(4, 2, NOW());

-- SALIDAS
INSERT INTO Salidas (id_producto, cantidad, fecha) VALUES
(1, 2, NOW()),
(2, 1, NOW()),
(3, 4, NOW()),
(4, 1, NOW());

-- ROLES
INSERT INTO Roles (nombre) VALUES 
('Administrador'), 
('Vendedor'), 
('Almacenero'), 
('Invitado');

-- USUARIOS
INSERT INTO Usuarios (nombre, usuario, contrasena, id_rol) VALUES
('Ana Admin', 'admin', 'admin123', 1),
('Carlos Ventas', 'carlosv', 'ventas123', 2),
('Laura Almacen', 'lauraa', 'almacen123', 3),
('Marta Invitada', 'martai', 'invitada123', 4);

-- CLIENTES
INSERT INTO Clientes (nombre, correo, telefono) VALUES
('Cliente Uno', 'cliente1@mail.com', '111111111'),
('Cliente Dos', 'cliente2@mail.com', '222222222'),
('Cliente Tres', 'cliente3@mail.com', '333333333'),
('Cliente Cuatro', 'cliente4@mail.com', '444444444');

-- VENTAS
INSERT INTO Ventas (id_cliente, fecha, total) VALUES
(1, NOW(), 1000.00),
(2, NOW(), 500.00),
(3, NOW(), 750.00),
(4, NOW(), 900.00);

-- DETALLES VENTA
INSERT INTO DetallesVenta (id_venta, id_producto, cantidad, precio_unitario) VALUES
(1, 1, 1, 2500.00),
(2, 2, 2, 800.00),
(3, 3, 1, 600.00),
(4, 4, 3, 150.00);

-- LOGS INVENTARIO
INSERT INTO LogsInventario (id_producto, movimiento, cantidad, fecha) VALUES
(1, 'entrada', 5, NOW()),
(2, 'salida', 1, NOW()),
(3, 'entrada', 7, NOW()),
(4, 'salida', 2, NOW());
-- =====================--
-- PROCEDIMIENTOS ALMACENADOS CRUD
-- =====================

-- INSERT: Agregar nuevo cliente
DELIMITER //
CREATE PROCEDURE InsertarCliente(
    IN p_nombre VARCHAR(100),
    IN p_correo VARCHAR(100),
    IN p_telefono VARCHAR(20)
)
BEGIN
    INSERT INTO Clientes (nombre, correo, telefono)
    VALUES (p_nombre, p_correo, p_telefono);
END;
//
DELIMITER ;

-- SELECT: Consultar inventario completo
DELIMITER //
CREATE PROCEDURE ObtenerInventario()
BEGIN
    SELECT 
        p.nombre AS producto,
        c.nombre AS categoria,
        i.cantidad,
        u.nombre AS ubicacion
    FROM Inventario i
    JOIN Productos p ON i.id_producto = p.id
    JOIN Categorias c ON p.id_categoria = c.id
    JOIN Ubicaciones u ON i.id_ubicacion = u.id;
END;
//
DELIMITER ;

-- UPDATE: Cambiar precio de producto
DELIMITER //
CREATE PROCEDURE ActualizarPrecioProducto(
    IN p_id INT,
    IN p_nuevo_precio DECIMAL(10,2)
)
BEGIN
    UPDATE Productos
    SET precio = p_nuevo_precio
    WHERE id = p_id;
END;
//
DELIMITER ;

-- DELETE: Eliminar una categoría (solo si no tiene productos)
DELIMITER //
CREATE PROCEDURE EliminarCategoria(
    IN p_id_categoria INT
)
BEGIN
    DELETE FROM Categorias
    WHERE id = p_id_categoria;
END;
//
DELIMITER ;


