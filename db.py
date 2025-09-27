import sqlite3, os

def conectar_db():
    ruta_db = os.path.join(os.path.dirname(__file__), 'salud.db')
    conn = sqlite3.connect(ruta_db)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sintomas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            sintomas TEXT
        )
    ''')
    conn.commit()
    conn.close()