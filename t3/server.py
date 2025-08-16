import os
import mysql.connector
from flask import Flask, jsonify, render_template, request

# indica explícitamente dónde están tus carpetas (opcionales pero recomendado)
app = Flask(__name__, template_folder="templates", static_folder="static")




def get_db_config():
    return {
        "host": os.getenv("MYSQL_HOST", "tramway.proxy.rlwy.net"),
        "user": os.getenv("MYSQL_USER", "root"),
        "password": os.getenv("MYSQL_PASSWORD", "oBmoAzyFCkrsKNUwXEQaSBrKtLVmXdAp"),
        "database": os.getenv("MYSQL_DB", "railway"),
        "port": int(os.getenv("MYSQL_PORT", 58483))
    }
    
# --------------------------
# MENÚ PRINCIPAL
# --------------------------
@app.route("/")
def menu():
    return render_template("index.html")

# --------------------------
# CRUD LIBROS
# --------------------------
@app.route("/crud")
def crud():
    return render_template("crud.html")

@app.route("/libros", methods=["GET", "POST"])
def libros():
    conn = mysql.connector.connect(**get_db_config())
    cursor = conn.cursor(dictionary=True)

    if request.method == "GET":
        cursor.execute("SELECT * FROM libros")
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(datos)

    if request.method == "POST":
        data = request.get_json()
        if not data:
            cursor.close()
            conn.close()
            return jsonify({"error": "No se recibió JSON válido"}), 400

        try:
            # 1️⃣ Crear el libro
            cursor.execute("""
                INSERT INTO libros (isbn, titulo, anio_publicacion, categoria, autor)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                data.get("isbn", ""),
                data.get("titulo", ""),
                data.get("anio_publicacion"),
                data.get("categoria", ""),
                data.get("autor", "")
            ))
            conn.commit()
            libro_id = cursor.lastrowid

            # 2️⃣ Crear 1 ejemplar por defecto automáticamente
            tipo = "fisico"
            estado = "disponible"
            estanteria_id = 1
            codigo_interno = f"LIB-{libro_id}-001"

            cursor.execute("""
                INSERT INTO ejemplares (libro_id, estanteria_id, tipo, estado, codigo_interno)
                VALUES (%s, %s, %s, %s, %s)
            """, (libro_id, estanteria_id, tipo, estado, codigo_interno))
            conn.commit()

            cursor.close()
            conn.close()

            return jsonify({
                "mensaje": "Libro creado y 1 ejemplar generado",
                "id": libro_id,
                "isbn": data.get("isbn", ""),
                "titulo": data.get("titulo", ""),
                "anio_publicacion": data.get("anio_publicacion"),
                "categoria": data.get("categoria", ""),
                "autor": data.get("autor")
            }), 201

        except Exception as e:
            conn.rollback()
            cursor.close()
            conn.close()
            return jsonify({"error": f"No se pudo crear libro/ejemplar: {e}"}), 400


# --------------------------
# CRUD LIBRO POR ID
# --------------------------
@app.route("/libros/<int:id>", methods=["PUT", "DELETE"])
def libro_id(id):
    conn = mysql.connector.connect(**get_db_config())
    cursor = conn.cursor(dictionary=True)

    if request.method == "PUT":
        data = request.get_json()
        cursor.execute("""
            UPDATE libros
            SET isbn=%s, titulo=%s, anio_publicacion=%s, categoria=%s, autor=%s
            WHERE id=%s
        """, (data["isbn"], data["titulo"], data["anio_publicacion"], data["categoria"], data["autor"], id))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Libro actualizado"})

    if request.method == "DELETE":
        try:
            cursor.execute("DELETE FROM ejemplares WHERE libro_id=%s", (id,))
            cursor.execute("DELETE FROM libros WHERE id=%s", (id,))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({"mensaje": "Libro y ejemplares eliminados"})
        except Exception as e:
            conn.rollback()
            cursor.close()
            conn.close()
            return jsonify({"error": f"No se pudo eliminar: {e}"}), 400

# --------------------------
# CRUD PRÉSTAMOS
# --------------------------
@app.route("/prestados")
def prestados():
    return render_template("prestados.html")

@app.route("/api/prestados", methods=["GET", "POST"])
def api_prestados():
    conn = mysql.connector.connect(**get_db_config())
    cursor = conn.cursor(dictionary=True)

    if request.method == "GET":
        cursor.execute("""
            SELECT p.id, l.titulo, e.nombre, e.apellido, p.fecha_prestamo, p.fecha_devolucion_estimada
            FROM prestamos p
            JOIN ejemplares ej ON p.ejemplar_id = ej.id
            JOIN libros l ON ej.libro_id = l.id
            JOIN estudiantes e ON p.estudiante_id = e.id
            WHERE p.fecha_devolucion_real IS NULL
        """)
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(datos)

    if request.method == "POST":
        data = request.get_json()
        libro_id = data.get("libro_id")
        estudiante_id = data.get("estudiante_id")
        fecha_prestamo = data.get("fecha_prestamo")
        fecha_devolucion_estimada = data.get("fecha_devolucion_estimada")

        # 1️⃣ Buscar un ejemplar disponible de ese libro
        cursor.execute("""
            SELECT id FROM ejemplares
            WHERE libro_id=%s AND estado='disponible'
            ORDER BY id ASC
            LIMIT 1
        """, (libro_id,))
        ejemplar = cursor.fetchone()

        if not ejemplar:
            cursor.close()
            conn.close()
            return jsonify({"error": "No hay ejemplares disponibles para este libro"}), 400

        ejemplar_id = ejemplar["id"]

        # 2️⃣ Registrar el préstamo
        cursor.execute("""
            INSERT INTO prestamos (ejemplar_id, estudiante_id, fecha_prestamo, fecha_devolucion_estimada)
            VALUES (%s, %s, %s, %s)
        """, (ejemplar_id, estudiante_id, fecha_prestamo, fecha_devolucion_estimada))

        # 3️⃣ Marcar ejemplar como no disponible
        cursor.execute("UPDATE ejemplares SET estado='prestado' WHERE id=%s", (ejemplar_id,))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"mensaje": "Préstamo registrado", "ejemplar_id": ejemplar_id}), 201


@app.route("/api/prestados/<int:id>", methods=["DELETE"])
def eliminar_prestamo(id):
    conn = mysql.connector.connect(**get_db_config())
    cursor = conn.cursor()
    cursor.execute("DELETE FROM prestamos WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"mensaje": "Préstamo eliminado"})

# --------------------------
# CRUD ESTUDIANTES
# --------------------------
@app.route("/estudiantes")
def estudiantes():
    return render_template("estudiantes.html")

@app.route("/api/estudiantes", methods=["GET", "POST"])
def api_estudiantes():
    conn = mysql.connector.connect(**get_db_config())
    cursor = conn.cursor(dictionary=True)

    if request.method == "GET":
        cursor.execute("SELECT * FROM estudiantes")
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(datos)

    if request.method == "POST":
        data = request.get_json()
        cursor.execute("""
            INSERT INTO estudiantes (codigo_estudiante, nombre, apellido, email)
            VALUES (%s, %s, %s, %s)
        """, (data["codigo_estudiante"], data["nombre"], data["apellido"], data["email"]))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Estudiante agregado"}), 201

@app.route("/api/estudiantes/<int:id>", methods=["PUT", "DELETE"])
def estudiante_id(id):
    conn = mysql.connector.connect(**get_db_config())
    cursor = conn.cursor(dictionary=True)

    if request.method == "PUT":
        data = request.get_json()
        cursor.execute("""
            UPDATE estudiantes
            SET codigo_estudiante=%s, nombre=%s, apellido=%s, email=%s
            WHERE id=%s
        """, (data["codigo_estudiante"], data["nombre"], data["apellido"], data["email"], id))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Estudiante actualizado"})

    if request.method == "DELETE":
        cursor.execute("DELETE FROM estudiantes WHERE id=%s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Estudiante eliminado"})

# --------------------------
# REPORTES
# --------------------------
@app.route("/reportes")
def reportes():
    return render_template("reportes.html")

@app.route("/api/reportes")
def api_reportes():
    conn = mysql.connector.connect(**get_db_config())

    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) AS total_libros FROM libros")
    total_libros = cursor.fetchone()["total_libros"]

    cursor.execute("""
        SELECT COUNT(*) AS total_prestados
        FROM prestamos
        WHERE fecha_devolucion_real IS NULL
    """)
    total_prestados = cursor.fetchone()["total_prestados"]

    cursor.execute("""
        SELECT categoria, COUNT(*) AS cantidad
        FROM libros
        GROUP BY categoria
    """)
    categorias = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify({
        "total_libros": total_libros,
        "total_prestados": total_prestados,
        "categorias": categorias
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
