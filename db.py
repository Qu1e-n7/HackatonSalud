import sqlite3, os

def conectar_db():
    ruta_db = os.path.join(os.path.dirname(__file__), 'salud.db')
    conn = sqlite3.connect(ruta_db)
    conn.row_factory = sqlite3.Row
    return conn
