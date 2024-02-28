/*Crea una tabla llamada "Productos" con las columnas: "id" (entero, clave
primaria), "nombre" (texto) y "precio" (numérico).*/
CREATE TABLE IF NOT EXISTS productos(
	id SERIAL PRIMARY KEY,
	NOMBRE varchar	(255),
	precio INT
)
/*2. Inserta al menos cinco registros en la tabla "Productos".*/
INSERT INTO public.productos(nombre,precio)
VALUES ('Antonio',5000),('Juan',2500),('Pedro',4000),('Filomena',7000),('Mariano',1200),('Lidia',10000)

/*3. Actualiza el precio de un producto en la tabla "Productos".*/
UPDATE public.productos
SET precio = 500
WHERE id=1

/*4. Elimina un producto de la tabla "Productos".*/
DELETE FROM public.productos
WHERE id=4

/*5. Realiza una consulta que muestre los nombres de los usuarios junto con los
nombres de los productos que han comprado (utiliza un INNER JOIN con la
tabla "Productos").*/
CREATE TABLE Pedidos (
    pedido_id SERIAL PRIMARY KEY,
    usuario_id INT,
    producto_id INT,
    cantidad INT
  )
ALTER TABLE Pedidos
ADD CONSTRAINT fk_usuario_id
FOREIGN KEY (usuario_id) REFERENCES Usuarios(id)
ALTER TABLE Pedidos
ADD CONSTRAINT fk_producto_id
FOREIGN KEY (producto_id) REFERENCES Productos(id)

SELECT usuarios.nombre, productos.nombre, pedidos.cantidad
from public.usuarios
inner join public.pedidos on pedidos.pedido_id = usuarios.id
INNER JOIN public.productos ON pedidos.producto_id = productos.id