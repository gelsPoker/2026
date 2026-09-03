// INICIALIZACION
const formulario = document.getElementById("formularioReportes");
const resultado = document.getElementById("resultadoReportes");

formulario.addEventListener("submit", function(evento){
    // Evitar que el formulario recargue la página.
    evento.preventDefault();

    //  Obtener los datos del formulario
    const datosFormulario = new FormData(formulario);

    //  Extraer cada valor usando el atributo name del HTML
    const nombre = datosFormulario.get("nombre");
    const fecha = datosFormulario.get("fecha");
    const zona = datosFormulario.get("zona");
    const categoria = datosFormulario.get("categoria");
    const estado = datosFormulario.get("estado");

    // Mostrar en consola para verificar los datos
    console.log("Nombre: ", nombre);
    console.log("Fecha: ", fecha);
    console.log("Zona: ", zona);
    console.log("Categoría: ", categoria);
    console.log("Estado: ", estado);

    //  Mostrar los valores 
    resultado.innerHTML = `
        <div style="background-color: rgba(0, 0, 0, 0.2); padding: 25px; border-radius: 20px; border: 2px solid rgba(255, 255, 255, 0.1); margin-top: 20px;">
            <h3 style="color: #4ed0d0; text-align: center; margin-bottom: 20px; font-size: 22px;">Resumen del Reporte</h3>
            
            <p style="color: #fff; font-size: 18px; line-height: 2; text-align: left; margin-left: 20px;">
                <strong>Nombre Solicitante:</strong> ${nombre || '<span style="color: #b6a1a1;">No ingresado</span>'}<br>
                <strong>Fecha Seleccionada:</strong> ${fecha || '<span style="color: #b6a1a1;">No ingresada</span>'}<br>
                <strong>Zona Asignada:</strong> ${zona || '<span style="color: #b6a1a1;">No seleccionada</span>'}<br>
                <strong>Categoría de Ayuda:</strong> ${categoria || '<span style="color: #b6a1a1;">No seleccionada</span>'}<br>
                <strong>Estado de Solicitud:</strong> ${estado || '<span style="color: #b6a1a1;">No seleccionado</span>'}
            </p>
        </div>
    `;
});