import os
import mysql.connector
from flask import Flask, jsonify, render_template, request

app = Flask(__name__, template_folder="templates", static_folder="static")

# --------------------------
# CONFIG Y CONEXIÓN MYSQL
# --------------------------
def get_db_config():
    host = os.getenv("MYSQL_HOST", "localhost")
    user = os.getenv("MYSQL_USER", "root")
    password = os.getenv("MYSQL_PASSWORD", "")
    database = os.getenv("MYSQL_DB", "railway")
    port_str = os.getenv("MYSQL_PORT")
    try:
        port = int(port_str) if port_str else 3306
    except ValueError:
        port = 3306
    return {"host": host, "user": user, "password": password, "database": database, "port": port}

def get_db_connection():
    try:
        return mysql.connector.connect(**get_db_config())
    except mysql.connector.Error as e:
        print(f"[ERROR MySQL] {e}")
        return None

# --------------------------
# RUTAS PRINCIPALES
# --------------------------
@app.route("/")
def menu():
    return render_template("index.html")

@app.route("/crud")
def crud():
    return render_template("crud.html")

# --------------------------
# CRUD LIBROS
# --------------------------
@app.route("/libros", methods=["GET", "POST"])
def libros():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500
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

            # Crear 1 ejemplar por defecto
            cursor.execute("""
                INSERT INTO ejemplares (libro_id, estanteria_id, tipo, estado, codigo_interno)
                VALUES (%s, %s, %s, %s, %s)
            """, (libro_id, 1, "fisico", "disponible", f"LIB-{libro_id}-001"))
            conn.commit()

            cursor.close()
            conn.close()
            return jsonify({"mensaje": "Libro creado y 1 ejemplar generado", "id": libro_id}), 201
        except Exception as e:
            conn.rollback()
            cursor.close()
            conn.close()
            return jsonify({"error": f"No se pudo crear libro/ejemplar: {e}"}), 400

@app.route("/libros/<int:id>", methods=["PUT", "DELETE"])
def libro_id(id):
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500
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
# CRUD EJEMPLARES
# --------------------------
@app.route("/ejemplares", methods=["GET", "POST"])
def ejemplares():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500
    cursor = conn.cursor(dictionary=True)

    if request.method == "GET":
        cursor.execute("SELECT * FROM ejemplares")
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(datos)

    if request.method == "POST":
        data = request.get_json()
        try:
            cursor.execute("""
                INSERT INTO ejemplares (libro_id, estanteria_id, tipo, estado, codigo_interno)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                data["libro_id"],
                data.get("estanteria_id", 1),
                data.get("tipo", "fisico"),
                data.get("estado", "disponible"),
                data.get("codigo_interno", "")
            ))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({"mensaje": "Ejemplar creado"}), 201
        except Exception as e:
            conn.rollback()
            cursor.close()
            conn.close()
            return jsonify({"error": str(e)}), 400

# --------------------------
# CRUD ESTUDIANTES
# --------------------------
@app.route("/estudiantes", methods=["GET", "POST"])
def estudiantes():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500
    cursor = conn.cursor(dictionary=True)

    if request.method == "GET":
        cursor.execute("SELECT * FROM estudiantes")
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(datos)

    if request.method == "POST":
        data = request.get_json()
        try:
            cursor.execute("""
                INSERT INTO estudiantes (nombre, correo, telefono)
                VALUES (%s, %s, %s)
            """, (
                data["nombre"],
                data["correo"],
                data.get("telefono", "")
            ))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({"mensaje": "Estudiante creado"}), 201
        except Exception as e:
            conn.rollback()
            cursor.close()
            conn.close()
            return jsonify({"error": str(e)}), 400

# --------------------------
# CRUD PRÉSTAMOS
# --------------------------
@app.route("/prestamos", methods=["GET", "POST"])
def prestamos():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500
    cursor = conn.cursor(dictionary=True)

    if request.method == "GET":
        cursor.execute("""
            SELECT p.id, p.ejemplar_id, p.estudiante_id, p.fecha_prestamo, p.fecha_devolucion,
                   e.codigo_interno AS ejemplar, s.nombre AS estudiante
            FROM prestamos p
            LEFT JOIN ejemplares e ON p.ejemplar_id = e.id
            LEFT JOIN estudiantes s ON p.estudiante_id = s.id
        """)
        datos = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(datos)

    if request.method == "POST":
        data = request.get_json()
        try:
            cursor.execute("""
                INSERT INTO prestamos (ejemplar_id, estudiante_id, fecha_prestamo, fecha_devolucion)
                VALUES (%s, %s, %s, %s)
            """, (
                data["ejemplar_id"],
                data["estudiante_id"],
                data.get("fecha_prestamo"),
                data.get("fecha_devolucion")
            ))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({"mensaje": "Préstamo registrado"}), 201
        except Exception as e:
            conn.rollback()
            cursor.close()
            conn.close()
            return jsonify({"error": str(e)}), 400

# --------------------------
# REPORTES
# --------------------------
@app.route("/reportes/libros-disponibles", methods=["GET"])
def reportes_libros_disponibles():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT l.titulo, COUNT(e.id) AS disponibles
        FROM libros l
        LEFT JOIN ejemplares e ON l.id = e.libro_id AND e.estado='disponible'
        GROUP BY l.id
    """)
    datos = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(datos)

# --------------------------
# RUN APP
# --------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
