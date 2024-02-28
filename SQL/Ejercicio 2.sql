Nivel de dificultad: Fácil
/*1. Crea una base de datos llamada "MiBaseDeDatos".*/
create database if not exists MiBaseDeDatos ()
/*2. Crea una tabla llamada "Usuarios" con las columnas: "id" (entero, clave
primaria), "nombre" (texto) y "edad" (entero).*/
create table if not exists Usuarios(
	id SERIAL PRIMARY KEY,
	NOMBRE varchar	(255),
	EDAD INT
)
/*3. Inserta dos registros en la tabla "Usuarios".*/
INSERT INTO PUBLIC.Usuarios(nombre,edad)
VALUES('Pepe', 12), ('Antonio', 24)
/*4. Actualiza la edad de un usuario en la tabla "Usuarios".*/
UPDATE public.Usuarios
set edad = 50
WHERE id=1
/*5. Elimina un usuario de la tabla "Usuarios".*/
DELETE FROM public.Usuarios
WHERE id=2
/*Nivel de dificultad: Moderado
1. Crea una tabla llamada "Ciudades" con las columnas: "id" (entero, clave
primaria), "nombre" (texto) y "pais" (texto).*/
CREATE TABLE IF NOT EXISTS Ciudades(
id SERIAL PRIMARY KEY,
	nombre VARCHAR(255),
	pais VARCHAR (255))

/*2. Inserta al menos tres registros en la tabla "Ciudades".*/
INSERT INTO public.ciudades (nombre, pais)
VALUES('salou', 'españa'),('abene', 'senegal'),('montevideo','uruguay'),('damasco','siria')

/*3. Crea una foreign key en la tabla "Usuarios" que se relacione con la columna "id"
de la tabla "Ciudades".*/
ALTER TABLE Usuarios
ADD COLUMN ciudad_id integer,
ADD CONSTRAINT fk_ciudad_id
FOREIGN KEY (ciudad_id) REFERENCES Ciudades(id);

/*4. Realiza una consulta que muestre los nombres de los usuarios junto con el
nombre de su ciudad y país (utiliza un LEFT JOIN).*/
SELECT usuarios.nombre, ciudades.nombre, ciudades.pais
FROM public.usuarios
LEFT JOIN Ciudades
ON ciudades.id=usuarios.ciudad_id;

/*5/ Realiza una consulta que muestre solo los usuarios que tienen una ciudad
asociada (utiliza un INNER JOIN).*/
SELECT usuarios.nombre, ciudades.nombre
FROM public.usuarios
INNER JOIN Ciudades	
ON ciudades.id=ciudades.id;