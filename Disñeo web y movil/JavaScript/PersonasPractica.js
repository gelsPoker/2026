// INICIALIZACION
formulario = document.getElementById("formularioPersona")
resultado = document.getElementById("resultados")

formulario.addEventListener("submit", function(evento){
    // evitar que el formulario recargue la paguina.
    evento.preventDefault();

    // Obtener los datos del formulario
    const datosFormulario = new FormData(formulario)

    // Extrae cada valor usando el atributo name
    const nombre = datosFormulario.get("nombre")
    const rut = datosFormulario.get("rut")
    const direccion = datosFormulario.get("direccion")

    console.log("Nombre: ", nombre)
    console.log("Rut: ", rut)
    console.log("Direccion: ", direccion)

    // Mostrar los valores en el HTML
    resultado.innerHTML = `
    Nombre: ${nombre}<br>
    Rut: ${rut}<br>
    Direccion: ${direccion}
    `
})