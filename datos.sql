CREATE DATABASE IF NOT EXISTS proyecto1;
use proyecto1;

create table articulos(
    id int primary key auto_increment,
    nombre varchar(255)
    fecha date,
    contenido text,
    foto text,
    autor int,
    foreign key (autor) references usuario(id)
);

insert into usuario(nombre, correo, contraseña) values ("Santiago", "santi@gmail.com", 12345);

create table usuario(
    id int primary key auto_increment,
    nombre varchar(255),
    correo varchar(255),
    contraseña text
);

insert into articulos(nombre, fecha, contenido, foto, autor) values ("Desde la base de datos", "2024-08-08", "Lorem ipsum", "https://www.clarin.com/2012/02/04/BJbM2IRnQg_1200x0.jpg", 1);