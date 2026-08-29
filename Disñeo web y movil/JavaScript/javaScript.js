// Inicialización de variables
const formulario = document.getElementById("formularioAyuda");
const Resultado = document.getElementById("resultadoSolicitud");

formulario.addEventListener("submit", function(evento) {
    // Evitar que la página se recargue
    evento.preventDefault();

    // Capturar los datos del formulario
    const datos = new FormData(formulario);

    const nombre = datos.get("nombre");
    const rut = datos.get("rut");
    const telefono = datos.get("telefono");
    const tipoAyuda = datos.get("tipo_ayuda");

    // Imprimir 
    console.log("Nueva solicitud ingresada:");
    console.log("Nombre:", nombre);
    console.log("RUT:", rut);
    console.log("Teléfono:", telefono);
    console.log("Ayuda requerida:", tipoAyuda);

    Resultado.innerHTML = `
        <h3>¡Solicitud Registrada con Exito!</h3>
        <p>Los datos de Nombre:${nombre}<br> y RUT: ${rut}<br> han sido ingresados al sistema.</p>
        <p>Un coordinador se contactará al número: ${telefono} para gestionar el servicio.</p>
    `;
});