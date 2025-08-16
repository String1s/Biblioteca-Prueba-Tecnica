// ==================== CRUD LIBROS ====================
const API_URL = "/libros";

async function crearEjemplarAutomatico(libroId) {
    // Se usa directamente en Flask dentro de /libros POST
    console.log(`Ejemplar generado automáticamente para libro ${libroId}`);
}


document.getElementById("form-libro")?.addEventListener("submit", async e => {
    e.preventDefault();
    const id = document.getElementById("libro-id").value;
    const libro = {
        isbn: document.getElementById("isbn").value,
        titulo: document.getElementById("titulo").value,
        anio_publicacion: document.getElementById("anio_publicacion").value || null,
        categoria: document.getElementById("categoria").value,
        autor: document.getElementById("autor").value
    };

    try {
        let res;
        if (id) {
            // Actualizar libro
            res = await fetch(`${API_URL}/${id}`, {
                method: "PUT",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(libro)
            });
        } else {
            // Crear libro + ejemplar automático
            res = await fetch(API_URL, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(libro)
            });

            if (res.ok) {
                const nuevoLibro = await res.json();
                await crearEjemplarAutomatico(nuevoLibro.libro_id);
            }
        }

        if (!res.ok) throw new Error("Error al guardar libro");

        e.target.reset();
        document.getElementById("libro-id").value = "";
        cargarLibros();
    } catch (error) {
        alert("No se pudo guardar el libro");
        console.error(error);
    }
});

async function cargarLibros() {
    try {
        const res = await fetch(API_URL);
        if (!res.ok) throw new Error("Error al cargar libros");
        const datos = await res.json();
        const tbody = document.querySelector("#tabla-libros tbody");
        tbody.innerHTML = "";
        datos.forEach(libro => {
            const tr = document.createElement("tr");
            tr.innerHTML = `
                <td>${libro.id}</td>
                <td>${libro.isbn}</td>
                <td>${libro.titulo}</td>
                <td>${libro.anio_publicacion || ""}</td>
                <td>${libro.categoria || ""}</td>
                <td>${libro.autor || ""}</td>
                <td>
                    <button onclick="editarLibro(${libro.id}, '${libro.isbn}', '${libro.titulo}', '${libro.anio_publicacion || ""}', '${libro.categoria || ""}', '${libro.autor || ""}')">✏️</button>
                    <button onclick="eliminarLibro(${libro.id})">🗑️</button>
                </td>
            `;
            tbody.appendChild(tr);
        });
    } catch (error) {
        alert("No se pudieron cargar los libros");
        console.error(error);
    }
}

function editarLibro(id, isbn, titulo, anio, categoria, autor) {
    document.getElementById("libro-id").value = id;
    document.getElementById("isbn").value = isbn;
    document.getElementById("titulo").value = titulo;
    document.getElementById("anio_publicacion").value = anio;
    document.getElementById("categoria").value = categoria;
    document.getElementById("autor").value = autor;
}

async function eliminarLibro(id) {
    if (!confirm("¿Seguro que quieres eliminar este libro?")) return;
    try {
        const res = await fetch(`${API_URL}/${id}`, { method: "DELETE" });
        if (!res.ok) throw new Error("No se pudo eliminar el libro");
        cargarLibros();
    } catch (error) {
        alert("Error al eliminar el libro");
        console.error(error);
    }
}

// Auto carga
if (document.querySelector("#tabla-libros")) cargarLibros();

// ==================== CRUD PRÉSTAMOS ====================
const API_PRESTADOS = "/api/prestados";

async function cargarPrestados() {
    try {
        const res = await fetch(API_PRESTADOS);
        const data = await res.json();
        const tbody = document.querySelector("#tablaPrestados tbody");
        tbody.innerHTML = "";

        data.forEach(p => {
            tbody.innerHTML += `
                <tr>
                    <td>${p.id}</td>
                    <td>${p.titulo}</td>
                    <td>${p.nombre} ${p.apellido}</td>
                    <td>${new Date(p.fecha_prestamo).toLocaleDateString()}</td>
                    <td>${new Date(p.fecha_devolucion_estimada).toLocaleDateString()}</td>
                    <td>
                        <button onclick="eliminarPrestamo(${p.id})">🗑️</button>
                    </td>
                </tr>
            `;
        });
    } catch (error) {
        console.error("Error al cargar préstamos:", error);
        alert("No se pudieron cargar los préstamos");
    }
}

document.getElementById("formPrestamo")?.addEventListener("submit", async e => {
    e.preventDefault();

    const prestamo = {
        libro_id: document.getElementById("libro_id").value, // usamos libro_id
        estudiante_id: document.getElementById("estudiante_id").value,
        fecha_prestamo: document.getElementById("fecha_prestamo").value,
        fecha_devolucion_estimada: document.getElementById("fecha_devolucion_estimada").value
    };

    try {
        await fetch(API_PRESTADOS, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(prestamo)
        });
        e.target.reset();
        cargarPrestados();
    } catch (error) {
        console.error("Error al registrar préstamo:", error);
        alert("No se pudo registrar el préstamo");
    }
});

async function eliminarPrestamo(id) {
    if (!confirm("¿Eliminar este préstamo?")) return;

    try {
        await fetch(`${API_PRESTADOS}/${id}`, { method: "DELETE" });
        cargarPrestados();
    } catch (error) {
        console.error("Error al eliminar préstamo:", error);
        alert("No se pudo eliminar el préstamo");
    }
}

// Auto carga al iniciar
if (document.querySelector("#tablaPrestados")) cargarPrestados();

// ==================== CRUD ESTUDIANTES ====================
const API_ESTUDIANTES = "/api/estudiantes";

async function cargarEstudiantes() {
    try {
        const res = await fetch(API_ESTUDIANTES);
        if (!res.ok) throw new Error("Error al cargar estudiantes");
        const datos = await res.json();
        const tbody = document.querySelector("#tabla-estudiantes tbody");
        tbody.innerHTML = "";
        datos.forEach(est => {
            const tr = document.createElement("tr");
            tr.innerHTML = `
                <td>${est.id}</td>
                <td>${est.codigo_estudiante}</td>
                <td>${est.nombre}</td>
                <td>${est.apellido}</td>
                <td>${est.email}</td>
                <td>
                    <button onclick="editarEstudiante(${est.id}, '${est.codigo_estudiante}', '${est.nombre}', '${est.apellido}', '${est.email}')">✏️</button>
                    <button onclick="eliminarEstudiante(${est.id})">🗑️</button>
                </td>
            `;
            tbody.appendChild(tr);
        });
    } catch (error) {
        alert("No se pudieron cargar los estudiantes");
        console.error(error);
    }
}

document.getElementById("form-estudiante")?.addEventListener("submit", async e => {
    e.preventDefault();
    const id = document.getElementById("estudiante-id").value;
    const estudiante = {
        codigo_estudiante: document.getElementById("codigo_estudiante").value,
        nombre: document.getElementById("nombre").value,
        apellido: document.getElementById("apellido").value,
        email: document.getElementById("email").value
    };

    try {
        let res;
        if (id) {
            res = await fetch(`${API_ESTUDIANTES}/${id}`, {
                method: "PUT",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(estudiante)
            });
        } else {
            res = await fetch(API_ESTUDIANTES, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(estudiante)
            });
        }
        if (!res.ok) throw new Error("Error al guardar estudiante");
        e.target.reset();
        document.getElementById("estudiante-id").value = "";
        cargarEstudiantes();
    } catch (error) {
        alert("No se pudo guardar el estudiante");
        console.error(error);
    }
});

function editarEstudiante(id, codigo, nombre, apellido, email) {
    document.getElementById("estudiante-id").value = id;
    document.getElementById("codigo_estudiante").value = codigo;
    document.getElementById("nombre").value = nombre;
    document.getElementById("apellido").value = apellido;
    document.getElementById("email").value = email;
}

async function eliminarEstudiante(id) {
    if (confirm("¿Seguro que quieres eliminar este estudiante?")) {
        try {
            const res = await fetch(`${API_ESTUDIANTES}/${id}`, { method: "DELETE" });
            if (!res.ok) throw new Error("No se pudo eliminar");
            cargarEstudiantes();
        } catch (error) {
            alert("Error al eliminar estudiante");
            console.error(error);
        }
    }
}

// ==================== AUTO CARGA SEGÚN PÁGINA ====================
if (document.querySelector("#tabla-libros")) cargarLibros();
if (document.querySelector("#tablaPrestados")) cargarPrestados();
if (document.querySelector("#tabla-estudiantes")) cargarEstudiantes();



// ==================== AUTO CARGA SEGÚN PÁGINA ====================
if (document.querySelector("#tabla-libros")) {
    cargarLibros();
}
