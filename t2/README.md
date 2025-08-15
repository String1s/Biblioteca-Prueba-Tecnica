# 🔌 Task 2 - Consumo de REST API e Integración con MySQL

Este módulo implementa un script en **Python** que:
1. Consume datos desde una **API pública** (JSONPlaceholder).
2. Inserta información procesada en la base de datos **biblioteca** creada en el Task 1.
3. Envía datos nuevos a la API mediante una solicitud **POST**.
4. Maneja errores de conexión y respuestas HTTP.

---

## 🎯 Objetivo
- Practicar el consumo de APIs REST con `requests`.
- Integrar datos externos con una base de datos MySQL/MariaDB.
- Implementar operaciones **GET** y **POST** con manejo de errores.

---

## 📂 Archivos incluidos
- `task2_api_mysql.py` → Script principal.


---

## ⚙️ Tecnologías y Librerías Usadas
**Lenguaje:** Python 3.10+  
**Base de datos:** MariaDB/MySQL (requiere la base `biblioteca` del Task 1)

Librerías (`pip list` relevantes):
- `requests` → Para realizar peticiones HTTP a la API.
- `mysql-connector-python` → Para conectar Python con MySQL/MariaDB.

Instalación de librerías necesarias:
```bash
pip install requests mysql-connector-python

Ejecuta el script:

python task2_api_mysql.py




Funcionamiento del Script
1️⃣ GET: Traer datos de la API

URL usada: https://jsonplaceholder.typicode.com/posts

Recupera una lista de posts ficticios.

Limita la inserción a los 5 primeros registros.

2️⃣ Insertar en MySQL

Cada post se transforma en un libro:

title → Título del libro (máx. 100 caracteres).

userId → Autor simulado (Usuario X).

id → ISBN simulado (API-{id}).

Año fijo: 2025.

Categoría fija: General.

Inserta los libros en la tabla libros de la base biblioteca.

3️⃣ POST: Enviar datos a la API

Envía un objeto JSON con título, cuerpo y userId.

API responde con el objeto creado (simulado por JSONPlaceholder).








pip list
Package                Version
---------------------- --------
blinker                1.9.0   
certifi                2025.8.3
charset-normalizer     3.4.3   
click                  8.2.1
colorama               0.4.6
Flask                  3.1.1
flask-cors             6.0.1
idna                   3.10
itsdangerous           2.2.0
Jinja2                 3.1.6
MarkupSafe             3.0.2
mysql-connector-python 9.4.0
pip                    25.2
requests               2.32.4
urllib3                2.5.0
Werkzeug               3.1.3