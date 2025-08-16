import requests
import mysql.connector
import os
import mysql.connector

# ---------------------------
# Configuración de la base de datos MySQL
# ---------------------------
def get_db_config():
    return {
        "host": os.getenv("MYSQL_HOST", "tramway.proxy.rlwy.net"),
        "user": os.getenv("MYSQL_USER", "root"),
        "password": os.getenv("MYSQL_PASSWORD", "oBmoAzyFCkrsKNUwXEQaSBrKtLVmXdAp"),
        "database": os.getenv("MYSQL_DB", "railway"),
        "port": int(os.getenv("MYSQL_PORT", 58483))
    }
# ---------------------------
# Conexión a la base de datos
# ---------------------------
def conectar_mysql():
    return mysql.connector.connect(**get_db_config)

# ---------------------------
# GET: traer datos de API
# ---------------------------
def obtener_posts():
    print("=== GET: Trayendo posts de la API ===")
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200:
            datos = resp.json()
            print(f"Se obtuvieron {len(datos)} registros de la API.")
            return datos
        else:
            print(f"Error en GET: {resp.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
        return []

# ---------------------------
# Insertar en MySQL
# ---------------------------
def insertar_libros_en_mysql(posts):
    conn = conectar_mysql()
    cursor = conn.cursor()

    
    for post in posts[:5]:
        titulo = post['title'][:100]  # limitar a 100 caracteres
        autor = f"Usuario {post['userId']}"
        categoria = "General"

        # Usar id como ISBN simulado
        isbn = f"API-{post['id']}"

        try:
            cursor.execute("""
                INSERT INTO libros (isbn, titulo, anio_publicacion, categoria, autor)
                VALUES (%s, %s, %s, %s, %s)
            """, (isbn, titulo, 2025, categoria, autor))
        except mysql.connector.Error as err:
            print(f"No se pudo insertar {titulo}: {err}")

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Libros insertados en la base de datos.")

# ---------------------------
# POST: enviar datos a la API
# ---------------------------
def crear_post_api():
    print("\n=== POST: Enviando post a la API ===")
    url = "https://jsonplaceholder.typicode.com/posts"
    nuevo_post = {
        "title": "Libro desde MySQL",
        "body": "Este libro fue registrado primero en MySQL y luego enviado a la API.",
        "userId": 1
    }
    try:
        resp = requests.post(url, json=nuevo_post, timeout=5)
        if resp.status_code == 201:
            print("✅ Post creado con éxito en la API:")
            print(resp.json())
        else:
            print(f"Error en POST: {resp.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")


if __name__ == "__main__":
    posts = obtener_posts()
    if posts:
        insertar_libros_en_mysql(posts)
        crear_post_api()
