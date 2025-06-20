document.addEventListener("DOMContentLoaded", function () {
    const btnEliminar = document.getElementById('btn-eliminar');
    const modal = document.getElementById('modal-confirm');
    const btnCancel = document.getElementById('cancel-btn');
    const btnConfirm = document.getElementById('confirm-btn');
    const formEliminar = document.getElementById('form-eliminar');

    if (!btnEliminar || !modal || !btnCancel || !btnConfirm || !formEliminar) {
        console.warn("Algún elemento no se encontró en el DOM");
        return;
    }

    btnEliminar.addEventListener('click', () => {
        console.log("Click detectado"); // para debug
        modal.style.display = 'flex';  // muestra el modal (flex para centrar)
    });

    btnCancel.addEventListener('click', () => {
        modal.style.display = 'none';  // oculta el modal
    });

    // También cerrar modal si se hace clic fuera del contenido
    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.style.display = 'none';
        }
    });

    btnConfirm.addEventListener('click', () => {
        formEliminar.submit();  // envía el formulario si confirma
    });
});