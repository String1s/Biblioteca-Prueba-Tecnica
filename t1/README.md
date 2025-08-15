# 📚 Task 1 - Base de Datos para Sistema de Gestión de Biblioteca

Este módulo implementa el diseño y creación de una base de datos para un **Sistema de Gestión de Biblioteca** de la Universidad de los Andes, desarrollado para 5IG Solutions.  
Permite administrar libros físicos y digitales, controlar préstamos, gestionar estudiantes y observar metricas

---

🎯 Objetivo
- Diseñar un modelo entidad-relación (ER) que cumpla con los requisitos del sistema.
- Implementar la base de datos en **MariaDB/MySQL**.
- Garantizar escalabilidad para futuras ampliaciones.

---

## 🗄 Estructura de la Base de Datos

### **Tablas principales**
- **libros**: ISBN, título, año, categoría, autor.
- **ejemplares**: tipo (físico/digital), estado (disponible, prestado, reservado), código interno, URL/formato digital, referencia a `libros` y `estanterias`.
- **estanterias**: ubicación, tema, material, capacidad.
- **estudiantes**: código, nombre, apellido, email.
- **prestamos**: fechas de préstamo y devolución, relación con `ejemplares` y `estudiantes`.

### **Vista**
- **vista_libros_prestados**: muestra información de préstamos activos.



## 📂 Archivos incluidos
- `schema.sql` → Script SQL con la creación completa de tablas, relaciones, índices, vistas y triggers.
- `ER_diagram.png` → Diagrama entidad-relación exportado.

---

## ⚙️ Tecnologías y Librerías Usadas
Este módulo usa:
- **MariaDB** 10.4.24 
- **phpMyAdmin** 6.0.0-dev 

Si quieres conectarte desde Python:
pip install mysql-connector-python


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

CREATE DATABASE biblioteca;
Desde Mysql exportar bibioteca.sql 
o
mysql -u usuario -p biblioteca < schema.sql

Frank Robledo