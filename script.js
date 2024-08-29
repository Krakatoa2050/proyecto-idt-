const formulario = document.querySelector("form")

formulario.addEventListener("submit",(evento) => {
    evento.preventDefault( )
    const datos = new FormData(formulario)
    fetch("guardar.php",{
       method: "POST",
       body: datos
    }).then(
        cabecera => {
            console.log("Ver que tiene:",cabecera);
            return cabecera.json()
        }
    ).then(
        datos => {
            console.log(datos);
            if (datos.respuesta =="ok"){
                const defaults = {

                }
            }
        }
    )
})