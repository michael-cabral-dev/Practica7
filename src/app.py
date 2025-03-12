from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

# Configuración de conexión a MySQL
DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "rootpassword")
DB_NAME = os.getenv("DB_NAME", "test_db")

def connect_db():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return conn
    except mysql.connector.Error as err:
        return f"Error: {err}"

@app.route("/")
def hello_world():
    conn = connect_db()
    if isinstance(conn, str):
        return conn  # Retorna el error de conexión
    return "Hola Mundo, conexión a MySQL exitosa!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
