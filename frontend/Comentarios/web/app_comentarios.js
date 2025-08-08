async function listarComentarios() {
  try {
    const res = await fetch(API_BASE + ENDPOINTS.read_all);
    const data = await res.json();
    const lista = document.getElementById("listaComentarios");
    lista.innerHTML = "";

    for (const c of data) {
      let nombreBarbero = "Desconocido";

      if (c.id_barbero) {
        try {
          const resBarbero = await fetch(API_BASE + `/barberos/${c.id_barbero}`);
          if (resBarbero.ok) {
            const barbero = await resBarbero.json();
            nombreBarbero = barbero.nombre || "Sin nombre";
          }
        } catch (err) {
          console.error(`Error al obtener barbero ${c.id_barbero}:`, err);
        }
      }

      const item = document.createElement("li");
      item.textContent = `ID: ${c.id} - Cliente: ${c.cliente_nombre} - Barbero: ${nombreBarbero} - ${c.contenido} (${c.calificacion})`;
      lista.appendChild(item);
    }
  } catch (error) {
    console.error("Error al listar comentarios:", error);
  }
}

// Crear comentario
document.getElementById("formComentario").addEventListener("submit", async function (e) {
  e.preventDefault();

  const idBarbero = document.getElementById("barberoSelect").value;
  if (!idBarbero) {
    alert("Por favor selecciona un barbero.");
    return;
  }

  const body = {
    contenido: document.getElementById("texto").value.trim(),
    cliente_nombre: document.getElementById("email").value.trim(),
    calificacion: parseInt(document.getElementById("calificacion").value),
    id_barbero: parseInt(idBarbero)
  };

  try {
    const res = await fetch(API_BASE + ENDPOINTS.create, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body)
    });

    const data = await res.json();

    if (!res.ok) {
      console.error("Error al crear comentario:", data);
      alert("No se pudo crear el comentario: " + (data.mensaje || "Error desconocido"));
      return;
    }

    alert(data.mensaje || "Comentario creado correctamente");
    listarComentarios();
    mostrarSeccion('lista');

  } catch (error) {
    console.error("Error en la petición:", error);
    alert("Ocurrió un error de conexión al crear el comentario");
  }
});

async function buscarComentario() {
  const id = document.getElementById("idBuscar").value;
  if (!id) {
    alert("Ingrese un ID para buscar");
    return;
  }

  try {
    const res = await fetch(API_BASE + ENDPOINTS.read_one.replace("{id}", id));
    if (!res.ok) {
      alert("Comentario no encontrado");
      return;
    }

    const comentario = await res.json();

    // Rellenar campos
    document.getElementById("textoAccion").value = comentario.contenido;
    document.getElementById("emailAccion").value = comentario.cliente_nombre;
    document.getElementById("calificacionAccion").value = comentario.calificacion;

    // Guardar el id_barbero en el hidden
    document.getElementById("idBarberoHidden").value = comentario.id_barbero || "";

    // Mostrar el barbero
    let nombreBarbero = "Desconocido";
    if (comentario.id_barbero) {
      try {
        const resBarbero = await fetch(API_BASE + `/barberos/${comentario.id_barbero}`);
        if (resBarbero.ok) {
          const barbero = await resBarbero.json();
          nombreBarbero = barbero.nombre || "Sin nombre";
        }
      } catch (err) {
        console.error(`Error al obtener barbero ${comentario.id_barbero}:`, err);
      }
    }

    document.getElementById("barberoComentario").value = nombreBarbero;

  } catch (error) {
    console.error("Error al buscar comentario:", error);
    alert("Ocurrió un error al buscar el comentario");
  }
}

async function actualizarComentario() {
  const id = document.getElementById("idBuscar").value;
  if (!id) {
    alert("Primero busque un comentario para actualizar");
    return;
  }

  const body = {
    contenido: document.getElementById("textoAccion").value,
    cliente_nombre: document.getElementById("emailAccion").value,
    calificacion: parseInt(document.getElementById("calificacionAccion").value),
    id_barbero: parseInt(document.getElementById("idBarberoHidden").value)
  };

  try {
    const res = await fetch(API_BASE + ENDPOINTS.update.replace("{id}", id), {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body)
    });

    if (!res.ok) {
      throw new Error("Error al actualizar comentario");
    }

    const result = await res.json();
    alert(result.mensaje || "Comentario actualizado");
    listarComentarios();
    mostrarSeccion('lista');

  } catch (error) {
    console.error("Error al actualizar comentario:", error);
    alert("Ocurrió un error al actualizar el comentario");
  }
}

async function eliminarComentario() {
  const id = document.getElementById("idBuscar").value;
  if (!id) {
    alert("Primero busque un comentario para eliminar");
    return;
  }
  try {
    const res = await fetch(API_BASE + ENDPOINTS.delete.replace("{id}", id), {
      method: "DELETE"
    });

    const result = await res.json();
    alert(result.mensaje || "Eliminado");
    listarComentarios();
    mostrarSeccion('lista');

  } catch (error) {
    console.error("Error al eliminar comentario:", error);
    alert("Ocurrió un error al eliminar el comentario");
  }
}

// Mostrar secciones
function mostrarSeccion(id) {
  document.querySelectorAll(".seccion").forEach(s => s.style.display = "none");
  document.getElementById(id).style.display = "block";
}

// Cargar barberos en el dropdown
async function cargarBarberos() {
  try {
    const res = await fetch(API_BASE + ENDPOINTS.barberos);
    const barberos = await res.json();
    const selectCrear = document.getElementById("barberoSelect");
    selectCrear.innerHTML = '<option value="">Seleccione un barbero</option>';

    barberos.forEach(barbero => {
      const option1 = document.createElement("option");
      option1.value = barbero.id;
      option1.textContent = `${barbero.nombre} (ID: ${barbero.id})`;
      selectCrear.appendChild(option1);
    });

    selectCrear.addEventListener("change", () => {
      document.getElementById("idBarbero").value = selectCrear.value;
    });
  } catch (error) {
    console.error("Error al cargar barberos:", error);
  }
}

// Inicialización
document.addEventListener("DOMContentLoaded", () => {
  cargarBarberos();
  listarComentarios();
  mostrarSeccion('crear');
});