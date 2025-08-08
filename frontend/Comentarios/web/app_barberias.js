// Crear barbería
document.getElementById("formBarberia").addEventListener("submit", async (e) => {
    e.preventDefault();

    // Validaciones
    const nombre = document.getElementById("nombreBarberia").value.trim();
    const direccion = document.getElementById("direccionBarberia").value.trim();
    const telefono = document.getElementById("telefonoBarberia").value.trim();
    const email = document.getElementById("emailBarberia").value.trim();

    if (!nombre || !direccion || !telefono || !email) {
        alert("Por favor completa todos los campos.");
        return;
    }

    const barberia = { nombre, direccion, telefono, email };

    try {
        const res = await fetch(API_BASE_BARBERIA + ENDPOINTS_BARBERIA.create, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(barberia)
        });

        const data = await res.json();
        if (!res.ok) {
            alert(data.mensaje || "Error al crear barbería");
            return;
        }

        alert(data.mensaje || "Barbería creada correctamente");
        listarBarberias();
        mostrarSeccion('lista');

    } catch (error) {
        console.error("Error al crear barbería:", error);
        alert("Ocurrió un error de conexión al crear la barbería");
    }
});

// Listar todas las barberías
async function listarBarberias() {
    try {
        const res = await fetch(API_BASE_BARBERIA + ENDPOINTS_BARBERIA.read_all);
        const datos = await res.json();
        const lista = document.getElementById("listaBarberias");
        lista.innerHTML = "";
        datos.forEach(b => {
            const li = document.createElement("li");
            li.textContent = `${b.id} - ${b.nombre} - ${b.direccion} - ${b.telefono} - ${b.email}`;
            lista.appendChild(li);
        });
    } catch (error) {
        console.error("Error al listar barberías:", error);
        alert("No se pudieron cargar las barberías");
    }
}

// Buscar barbería por ID
async function buscarBarberia() {
    const id = document.getElementById("idBuscarBarberia").value;
    if (!id) {
        alert("Ingrese un ID para buscar");
        return;
    }

    try {
        const res = await fetch(API_BASE_BARBERIA + ENDPOINTS_BARBERIA.read_one.replace("{id}", id));
        if (res.ok) {
            const b = await res.json();
            document.getElementById("nombreBarberiaAccion").value = b.nombre;
            document.getElementById("direccionBarberiaAccion").value = b.direccion;
            document.getElementById("telefonoBarberiaAccion").value = b.telefono;
            document.getElementById("emailBarberiaAccion").value = b.email;
        } else {
            alert("Barbería no encontrada");
        }
    } catch (error) {
        console.error("Error al buscar barbería:", error);
        alert("Ocurrió un error al buscar la barbería");
    }
}

// Actualizar barbería
async function actualizarBarberia() {
    const id = document.getElementById("idBuscarBarberia").value;
    if (!id) {
        alert("Primero busque una barbería para actualizar");
        return;
    }

    const nombre = document.getElementById("nombreBarberiaAccion").value.trim();
    const direccion = document.getElementById("direccionBarberiaAccion").value.trim();
    const telefono = document.getElementById("telefonoBarberiaAccion").value.trim();
    const email = document.getElementById("emailBarberiaAccion").value.trim();

    if (!nombre || !direccion || !telefono || !email) {
        alert("Por favor completa todos los campos antes de actualizar.");
        return;
    }

    const barberia = { nombre, direccion, telefono, email };

    try {
        const res = await fetch(API_BASE_BARBERIA + ENDPOINTS_BARBERIA.update.replace("{id}", id), {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(barberia)
        });

        const data = await res.json();
        if (!res.ok) {
            alert(data.mensaje || "Error al actualizar barbería");
            return;
        }

        alert(data.mensaje || "Barbería actualizada correctamente");
        listarBarberias();
        mostrarSeccion('lista');

    } catch (error) {
        console.error("Error al actualizar barbería:", error);
        alert("Ocurrió un error al actualizar la barbería");
    }
}

// Eliminar barbería
async function eliminarBarberia() {
    const id = document.getElementById("idBuscarBarberia").value;
    if (!id) {
        alert("Ingrese un ID para eliminar");
        return;
    }

    try {
        const res = await fetch(API_BASE_BARBERIA + ENDPOINTS_BARBERIA.delete.replace("{id}", id), {
            method: "DELETE"
        });
        const data = await res.json();
        if (!res.ok) {
            alert(data.mensaje || "Error al eliminar barbería");
            return;
        }

        alert(data.mensaje || "Barbería eliminada correctamente");
        listarBarberias();
        mostrarSeccion('lista');

    } catch (error) {
        console.error("Error al eliminar barbería:", error);
        alert("Ocurrió un error al eliminar la barbería");
    }
}

// Mostrar secciones
function mostrarSeccion(id) {
    document.querySelectorAll(".seccion").forEach(s => s.style.display = "none");
    document.getElementById(id).style.display = "block";
}

// Inicialización
document.addEventListener("DOMContentLoaded", () => {
    listarBarberias();
    mostrarSeccion('crear');  // <--- Aquí muestras la sección de creación al cargar
});