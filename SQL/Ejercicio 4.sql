/*Nivel de dificultad: Experto
1. Crea una tabla llamada "Pedidos" con las columnas: "id" (entero, clave
primaria), "id_usuario" (entero, clave foránea de la tabla "Usuarios") y
"id_producto" (entero, clave foránea de la tabla "Productos").*/
CREATE TABLE Pedidos (
    pedido_id SERIAL PRIMARY KEY,
    usuario_id INT,
    producto_id INT
     )
ALTER TABLE Pedidos
ADD CONSTRAINT fk_usuario_id
FOREIGN KEY (usuario_id) REFERENCES Usuarios(id)
ALTER TABLE Pedidos
ADD CONSTRAINT fk_producto_id
FOREIGN KEY (producto_id) REFERENCES Productos(id)

/*2. Inserta al menos tres registros en la tabla "Pedidos" que relacionen usuarios con
productos.*/
INSERT INTO public.pedidos (usuario_id, producto_id)
VALUES(1,1),(3,3),(4,5)

/*3. Realiza una consulta que muestre los nombres de los usuarios y los nombres de
los productos que han comprado, incluidos aquellos que no han realizado
ningún pedido (utiliza LEFT JOIN y COALESCE).*/
SELECT usuarios.nombre, COALESCE(productos.nombre, 'Sin pedido') 
FROM public.usuarios
LEFT JOIN public.pedidos ON pedidos.usuario_id = usuarios.id
LEFT JOIN public.productos ON pedidos.producto_id = productos.id

/*4. Realiza una consulta que muestre los nombres de los usuarios que han
realizado un pedido, pero también los que no han realizado ningún pedido
(utiliza LEFT JOIN).*/
SELECT usuarios.nombre
FROM public.usuarios
LEFT JOIN public.pedidos ON pedidos.usuario_id = usuarios.id
LEFT JOIN public.productos ON pedidos.producto_id = productos.id

/*5. Agrega una nueva columna llamada "cantidad" a la tabla "Pedidos" y actualiza
los registros existentes con un valor (utiliza ALTER TABLE y UPDATE)*/
ALTER TABLE public.pedidos
ADD COLUMN cantidad INT

UPDATE public.pedidos 
SET cantidad=10