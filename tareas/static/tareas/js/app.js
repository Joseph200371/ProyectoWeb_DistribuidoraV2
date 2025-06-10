document.addEventListener("DOMContentLoaded", ()=>{

    // Función para obtener el año actual
    const getCurrentYear = () => {
        return new Date().getFullYear();
    }

    document.querySelector("#current-year").textContent = getCurrentYear();
})