document.addEventListener('DOMContentLoaded', function () {
    const formulario = document.getElementById('miFormulario');

    formulario.addEventListener('submit', function (event) {
        // Aquí puedes agregar lógica de validación adicional si es necesario
        if (!validarFormulario()) {
            event.preventDefault(); // Evitar que el formulario se envíe si no es válido
        }
    });
});

function validarFormulario() {
    // Puedes realizar validaciones adicionales aquí
    const nombre = document.getElementById('nombre').value;
    const email = document.getElementById('email').value;

    if (nombre.trim() === '' || email.trim() === '') {
        alert('Por favor, completa todos los campos.');
        return false;
    }

    return true;
}

