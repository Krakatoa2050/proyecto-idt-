<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="./css/estilo.css">
</head>
<body>
<section>
<?php
$conexion = new mysqli(
    "localhost", "root", "", "proyecto1");

$sql = "SELECT id, nombre, contenido, foto, fecha, autor FROM articulos";

$resultado = $conexion->query($sql);

while ($fila = $resultado->fetch_assoc()) {
    echo "
    <article>
        <h3>{$fila["nombre"]}</h3>
        <div>
            <img src='{$fila["foto"]}' alt='{$fila["nombre"]}'>
        </div>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Sequi illum saepe nihil nostrum fugit porro,
        assumenda eveniet in minima dolorem, 
        hic quis quaerat quasi autem non possimus amet a odit?</p>
    </article>";
}
?>
    
</section>
</body>
</html>