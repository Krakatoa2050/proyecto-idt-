<?php
header("content-Tyoe: application/json");
$nombre = $_POST["nombre"];
$fecha = $_POST["fecha"];
$foto = $_POST["foto"];
$contenido = $_POST["contenido"];

$conexion = new mysqli("localhost", "root", "", "proyecto1");

$sql = "INSERT INTO articulos
(nombre, contenido, foto, fecha, autor) 

VALUES 
('$nombre', '$contenido', '$foto', '$fecha', 1)";

$conexion->query($sql);
$conexion->insert_id;

if ($conexion->insert_id > 0) {
    echo json_encode([
        "respuesta" => "ok"
    ]);
}else{
    echo json_encode([
        "respuesta" => "error"
    ]);
    
}

$conexion->close();
