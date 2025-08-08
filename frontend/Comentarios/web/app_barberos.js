async function listarBarberos() {
    const res = await fetch(API_BASE_BARBERO + ENDPOINTS_BARBERO.read_all);
    const data = await res.json();
    const lista = document.getElementById("listaBarberos");
    lista.innerHTML = "";

    for (const b of data) {
        let nombreBarberia = "Desconocida";

        if (b.id_barberia) {
            try {
                const resBarberia = await fetch(API_BASE_BARBERO + ENDPOINTS_BARBERO.barberias + `/${b.id_barberia}`);
                if (resBarberia.ok) {
                    const barberia = await resBarberia.json();
                    nombreBarberia = barberia.nombre || "Sin nombre";
                }
            } catch (err) {
                console.error(`Error al obtener barbería ${b.id_barberia}:`, err);
            }
        }

        const item = document.createElement("li");
        item.textContent = `ID: ${b.id} - Nombre: ${b.nombre} - Especialidad: ${b.especialidad} - Experiencia: ${b.experiencia_anios} años - Barbería: ${nombreBarberia}`;
        lista.appendChild(item);
    }
}

// Crear barbero
document.getElementById("formBarbero").addEventListener("submit", async function (e) {
    e.preventDefault();

    const idBarberia = document.getElementById("barberiaSelect").value;
    if (!idBarberia) {
        alert("Por favor selecciona una barbería.");
        return;
    }

    const body = {
        nombre: document.getElementById("nombreBarbero").value.trim(),
        especialidad: document.getElementById("especialidadBarbero").value.trim(),
        experiencia_anios: parseInt(document.getElementById("experienciaBarbero").value),
        id_barberia: parseInt(idBarberia)
    };

    try {
        const res = await fetch(API_BASE_BARBERO + ENDPOINTS_BARBERO.create, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(body)
        });

        const data = await res.json();

        if (!res.ok) {
            console.error("Error al crear barbero:", data);
            alert("No se pudo crear el barbero: " + (data.mensaje || "Error desconocido"));
            return;
        }

        alert(data.mensaje || "Barbero creado correctamente");
        listarBarberos();
        mostrarSeccion('lista');

    } catch (error) {
        console.error("Error en la petición:", error);
        alert("Ocurrió un error de conexión al crear el barbero");
    }
});

async function buscarBarbero() {
    const id = document.getElementById("idBuscarBarbero").value;
    if (!id) {
        alert("Ingrese un ID para buscar");
        return;
    }

    try {
        const res = await fetch(API_BASE_BARBERO + ENDPOINTS_BARBERO.read_one.replace("{id}", id));
        if (!res.ok) {
            alert("Barbero no encontrado");
            return;
        }

        const barbero = await res.json();

        // Rellenar campos
        document.getElementById("nombreBarberoAccion").value = barbero.nombre;
        document.getElementById("especialidadBarberoAccion").value = barbero.especialidad;
        document.getElementById("experienciaBarberoAccion").value = barbero.experiencia_anios;

        // Guardar el id_barberia en el select
        const selectBarberia = document.getElementById("barberiaSelectAccion");
        selectBarberia.value = barbero.id_barberia || "";

    } catch (error) {
        console.error("Error al buscar barbero:", error);
        alert("Ocurrió un error al buscar el barbero");
    }
}

async function actualizarBarbero() {
    const id = document.getElementById("idBuscarBarbero").value;
    if (!id) {
        alert("Primero busque un barbero para actualizar");
        return;
    }

    const idBarberia = document.getElementById("barberiaSelectAccion").value;
    if (!idBarberia) {
        alert("Por favor selecciona una barbería antes de actualizar.");
        return;
    }

    const body = {
        nombre: document.getElementById("nombreBarberoAccion").value.trim(),
        especialidad: document.getElementById("especialidadBarberoAccion").value.trim(),
        experiencia_anios: parseInt(document.getElementById("experienciaBarberoAccion").value),
        id_barberia: parseInt(idBarberia)
    };

    try {
        const res = await fetch(API_BASE_BARBERO + ENDPOINTS_BARBERO.update.replace("{id}", id), {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(body)
        });

        const data = await res.json();
        if (!res.ok) {
            alert(data.mensaje || "Error al actualizar barbero");
            return;
        }

        alert(data.mensaje || "Barbero actualizado correctamente");
        listarBarberos();
        mostrarSeccion('lista');

    } catch (error) {
        console.error("Error al actualizar barbero:", error);
        alert("Ocurrió un error al actualizar el barbero");
    }
}

async function eliminarBarbero() {
    const id = document.getElementById("idBuscarBarbero").value;
    if (!id) {
        alert("Ingrese un ID para eliminar");
        return;
    }

    try {
        const res = await fetch(API_BASE_BARBERO + ENDPOINTS_BARBERO.delete.replace("{id}", id), {
            method: "DELETE"
        });
        const data = await res.json();
        if (!res.ok) {
            alert(data.mensaje || "Error al eliminar barbero");
            return;
        }

        alert(data.mensaje || "Barbero eliminado correctamente");
        listarBarberos();
        mostrarSeccion('lista');

    } catch (error) {
        console.error("Error al eliminar barbero:", error);
        alert("Ocurrió un error al eliminar el barbero");
    }
}

// Mostrar secciones
function mostrarSeccion(id) {
    document.querySelectorAll(".seccion").forEach(s => s.style.display = "none");
    document.getElementById(id).style.display = "block";
}

// Cargar barberías en el dropdown
async function cargarBarberias() {
    try {
        const res = await fetch(API_BASE_BARBERO + ENDPOINTS_BARBERO.barberias);
        const barberias = await res.json();

        const selectCrear = document.getElementById("barberiaSelect");
        const selectEditar = document.getElementById("barberiaSelectAccion");

        selectCrear.innerHTML = '<option value="">Seleccione una barbería</option>';
        selectEditar.innerHTML = '<option value="">Seleccione una barbería</option>';

        barberias.forEach(barberia => {
            const optionCrear = document.createElement("option");
            optionCrear.value = barberia.id;
            optionCrear.textContent = barberia.nombre;
            selectCrear.appendChild(optionCrear);

            const optionEditar = document.createElement("option");
            optionEditar.value = barberia.id;
            optionEditar.textContent = barberia.nombre;
            selectEditar.appendChild(optionEditar);
        });
    } catch (error) {
        console.error("Error al cargar barberías:", error);
        alert("No se pudieron cargar las barberías");
    }
}

// Inicialización
document.addEventListener("DOMContentLoaded", () => {
    cargarBarberias();
    listarBarberos();
    mostrarSeccion('crear');
});
