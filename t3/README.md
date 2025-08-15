# 💻 Task 3 - Front-End y Back-End para Gestión de Biblioteca

Este módulo implementa un **servidor Flask** que expone una API REST para gestionar el sistema de biblioteca, permitiendo:
- CRUD de libros.
- CRUD de estudiantes.
- Gestión de préstamos.
- Visualización de reportes.
- Renderizado de vistas HTML que consumen esta API desde el frontend.

---

## 🎯 Objetivo
Crear una aplicación web que conecte el frontend con la base de datos `biblioteca` usando un backend en Python con Flask y MySQL.

---

## 📂 Archivos principales
- `server.py` → Backend con Flask, expone rutas API y renderiza plantillas.
- `/templates/` → Archivos HTML para CRUD y reportes (se documentarán más adelante).
- `/static/` → Archivos CSS y JavaScript.

---

## ⚙️ Tecnologías y Librerías Usadas
**Lenguaje:** Python 3.10+  
**Base de datos:** MariaDB/MySQL (requiere la base `biblioteca` de Task 1)

Dependencias necesarias:
```bash
pip install flask flask-cors mysql-connector-python



Ejecución del servidor

Asegúrate de tener la base biblioteca creada (Task 1).

Instala dependencias:

pip install flask flask-cors mysql-connector-python


Ejecuta el servidor:

python server.py


Abre en el navegador:

http://127.0.0.1:5000



/////////////////////////////////////////////////////////////////////////////////////////

## 🎨 Front-End (JavaScript)

El archivo `app.js` maneja toda la interacción entre el **frontend** y el **backend Flask** (server.py) mediante peticiones AJAX con `fetch()`.

---

### 🔹 Funcionalidades implementadas

#### 1. CRUD Libros
- **GET `/libros`** → Lista todos los libros y los muestra en una tabla.
- **POST `/libros`** → Crea un nuevo libro y automáticamente un ejemplar físico.
- **PUT `/libros/:id`** → Actualiza los datos de un libro.
- **DELETE `/libros/:id`** → Elimina un libro y sus ejemplares asociados.
- Formulario HTML vinculado a `#form-libro` para crear/editar registros.

#### 2. CRUD Préstamos
- **GET `/api/prestados`** → Lista los préstamos activos y los muestra en tabla.
- **POST `/api/prestados`** → Registra un préstamo, asignando un ejemplar disponible.
- **DELETE `/api/prestados/:id`** → Elimina un préstamo y libera el ejemplar.

#### 3. CRUD Estudiantes
- **GET `/api/estudiantes`** → Lista todos los estudiantes.
- **POST `/api/estudiantes`** → Crea un nuevo estudiante.
- **PUT `/api/estudiantes/:id`** → Actualiza un estudiante existente.
- **DELETE `/api/estudiantes/:id`** → Elimina un estudiante.

---

### 🔹 Flujo general
1. Cada CRUD tiene:
   - Función de **carga inicial** (`cargarLibros`, `cargarPrestados`, `cargarEstudiantes`).
   - Formulario con listener `submit` para crear/editar datos.
   - Botones de acción en la tabla (✏️ para editar, 🗑️ para eliminar).
2. Se usan `querySelector` y `getElementById` para manipular el DOM.
3. Todas las peticiones usan `fetch()` con `Content-Type: application/json`.

---

### 🔹 Auto-carga
Dependiendo de la página:
- Si existe `#tabla-libros` → llama a `cargarLibros()`.
- Si existe `#tablaPrestados` → llama a `cargarPrestados()`.
- Si existe `#tabla-estudiantes` → llama a `cargarEstudiantes()`.

---




////////////////////////////////////////////////////////////////////////////////////////////////
### 📄 Plantilla: `crud.html` (Gestión de Libros)

Esta vista permite:
- Crear, actualizar y eliminar libros.
- Mostrar en una tabla todos los registros de la base de datos.
- Interactuar con el backend a través del archivo `app.js`.

---

#### 🔹 Estructura
1. **Formulario `#form-libro`**
   - `hidden id="libro-id"` → para diferenciar entre creación y edición.
   - Campos:
     - `isbn` (texto, requerido).
     - `titulo` (texto, requerido).
     - `anio_publicacion` (numérico, opcional).
     - `categoria` (texto).
     - `autor` (texto).
   - Botón **Guardar**:
     - Si `libro-id` está vacío → se crea un libro nuevo.
     - Si `libro-id` tiene valor → se actualiza el libro.

2. **Tabla `#tabla-libros`**
   - Encabezados: ID, ISBN, Título, Año, Categoría, Autor, Acciones.
   - `tbody` se rellena dinámicamente desde `app.js` con los datos del backend.
   - En la columna Acciones se añaden botones:
     - ✏️ → Editar libro.
     - 🗑️ → Eliminar libro.

3. **Script**
   - Incluye `app.js` para manejar eventos y peticiones al backend.

---

#### 🔹 Flujo de funcionamiento
1. Al cargar la página, `app.js` llama a `cargarLibros()` y obtiene datos de `/libros` (GET).
2. El formulario envía datos a `/libros` (POST) o `/libros/<id>` (PUT) según el caso.
3. Los cambios se reflejan automáticamente en la tabla tras cada operación.
4. Los botones de eliminar envían peticiones DELETE a `/libros/<id>`.

---


/////////////////////////////////////////////////////////////////////////////////////////////

### 📄 Plantilla: `estudiantes.html` (Gestión de Estudiantes)

Esta vista permite:
- Crear, editar y eliminar estudiantes.
- Mostrar en una tabla todos los estudiantes registrados en la base de datos.
- Utiliza `app.js` para comunicarse con el backend Flask.

---

#### 🔹 Estructura
1. **Formulario `#form-estudiante`**
   - `hidden id="estudiante-id"` → indica si es edición o creación.
   - Campos:
     - `codigo_estudiante` (texto, requerido).
     - `nombre` (texto, requerido).
     - `apellido` (texto, requerido).
     - `email` (correo, requerido).
   - Botón **Guardar**:
     - Si `estudiante-id` está vacío → crea un nuevo estudiante (POST).
     - Si `estudiante-id` tiene valor → actualiza un estudiante existente (PUT).

2. **Tabla `#tabla-estudiantes`**
   - Columnas: ID, Código, Nombre, Apellido, Email, Acciones.
   - El `tbody` se llena dinámicamente con datos obtenidos de `/api/estudiantes`.
   - En la columna Acciones:
     - ✏️ → Editar estudiante.
     - 🗑️ → Eliminar estudiante.

3. **Script**
   - Incluye `app.js` para manejar los eventos de formulario y tabla.

#### 🔹 Flujo de funcionamiento
1. Al cargar la página, `app.js` llama a `cargarEstudiantes()` para obtener la lista de estudiantes.
2. El formulario envía los datos a:
   - `/api/estudiantes` (POST) para crear.
   - `/api/estudiantes/<id>` (PUT) para actualizar.
3. La tabla se actualiza después de cada operación.
4. Los botones de eliminar hacen una petición DELETE a `/api/estudiantes/<id>`.



///////////////////////////////////////////////////////////////////////////////////////////

### 📄 Plantilla: `index.html` (Dashboard Biblioteca)

Es la página principal de la aplicación.  
Proporciona acceso a las diferentes secciones del sistema y permite buscar libros por título o ID.

---

#### 🔹 Funcionalidades
1. **Menú de navegación**
   - Contiene enlaces rápidos a las secciones:
     - Gestión de libros.
     - Libros prestados.
     - Gestión de estudiantes.
     - Reportes.

2. **Buscador de libros**
   - Campo de texto + botón "Buscar".
   - Filtra resultados consultando `/libros` vía `fetch()`.
   - Muestra coincidencias en tarjetas con información del libro:
     - Título.
     - ID.
     - Autor.
     - Año de publicación.
     - Categoría.

3. **Tarjetas de acceso**
   - Cada tarjeta usa íconos de **Bootstrap Icons**.
   - Diseño responsivo con **Bootstrap 5**.
   - Efecto hover (`scale`) para resaltar.

---

#### 🔹 Tecnologías usadas
- **Bootstrap 5** → para diseño responsivo y componentes.
- **Bootstrap Icons** → íconos visuales.
- **JavaScript Fetch API** → para consultar y filtrar libros.
- **CSS** embebido → estilos personalizados para el dashboard.

---

#### 🔹 Flujo del buscador
1. El usuario ingresa un texto o ID y presiona **Buscar**.
2. El script hace `fetch("/libros")` para obtener todos los libros.
3. Filtra los resultados por coincidencia en `titulo` o por coincidencia exacta en `id`.
4. Si hay resultados → genera tarjetas con la información.
5. Si no hay resultados → muestra mensaje de advertencia.



//////////////////////////////////////////////////////////////////////////////////////////////

### 📄 Plantilla: `prestados.html` (Gestión de Préstamos)

Esta vista permite:
- Registrar nuevos préstamos de libros a estudiantes.
- Mostrar una lista de los préstamos activos.
- Eliminar préstamos existentes.

---

#### 🔹 Estructura
1. **Formulario `#formPrestamo`**
   - `libro_id` (select): lista desplegable con libros disponibles (excluye los ya prestados).
   - `estudiante_id` (select): lista desplegable con todos los estudiantes.
   - `fecha_prestamo` (date): fecha en que se realiza el préstamo.
   - `fecha_devolucion_estimada` (date): fecha esperada de devolución.
   - Botón **Registrar**: envía la información al backend para crear el préstamo.

2. **Tabla `#tablaPrestados`**
   - Columnas: ID, Título del libro, Estudiante, Fecha de préstamo, Fecha estimada de devolución, Acciones.
   - Muestra los préstamos activos obtenidos de `/api/prestados`.
   - Botones 🗑️ para eliminar un préstamo.

---

#### 🔹 Funcionalidades JavaScript
- **cargarLibrosDropdown()**
  - Consulta `/libros` y `/api/prestados`.
  - Filtra libros que no están prestados y los carga en el select.
- **cargarEstudiantesDropdown()**
  - Consulta `/api/estudiantes` y llena el select de estudiantes.
- **cargarPrestados()**
  - Consulta `/api/prestados` y muestra los registros en la tabla.
  - Llama a `cargarLibrosDropdown()` para mantener actualizada la lista de libros disponibles.
- **Registrar préstamo**
  - Envío POST a `/api/prestados`.
  - Si es exitoso → recarga la lista y resetea el formulario.
- **Eliminar préstamo**
  - Envío DELETE a `/api/prestados/:id`.
  - Recarga la tabla tras la eliminación.

---

#### 🔹 Flujo de uso
1. Seleccionar un libro disponible y un estudiante.
2. Ingresar las fechas de préstamo y devolución estimada.
3. Presionar **Registrar**.
4. El préstamo aparece en la tabla y el libro desaparece de la lista de disponibles.
5. Para devolver un libro, se elimina el préstamo (lo que libera el ejemplar en la base de datos).


/////////////////////////////////////////////////////////////////////////////////////////////////////
### 📄 Plantilla: `reportes.html` (Panel de Reportes)

Esta vista muestra estadísticas generales de la biblioteca de forma numérica y gráfica.

---

#### 🔹 Estructura
1. **Encabezado**
   - Título: 📊 Reportes Biblioteca.
2. **Indicadores numéricos**
   - `#totalLibros`: total de libros registrados.
   - `#totalPrestados`: total de libros actualmente prestados.
3. **Gráfico de categorías**
   - Lienzo `<canvas>` para renderizar un gráfico de barras con la cantidad de libros por categoría.

---

#### 🔹 Funcionalidades JavaScript
- **Consulta de datos**
  - Hace un `fetch("/api/reportes")` para obtener:
    ```json
    {
      "total_libros": <número>,
      "total_prestados": <número>,
      "categorias": [
        { "categoria": "Ficción", "cantidad": 5 },
        { "categoria": "Historia", "cantidad": 3 }
      ]
    }
    ```
- **Renderizado de datos**
  - Inserta los valores en los elementos `#totalLibros` y `#totalPrestados`.
  - Genera un gráfico de barras usando **Chart.js**:
    - Eje X: nombres de las categorías.
    - Eje Y: cantidad de libros.
    - Color: azul semitransparente.

---

#### 🔹 Flujo de uso
1. El usuario entra a la página `/reportes`.
2. Se hace automáticamente la petición a `/api/reportes`.
3. Se muestran los totales y el gráfico categorizado.
4. No hay interacción directa del usuario, solo visualización.

