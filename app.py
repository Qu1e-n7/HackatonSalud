from flask import Flask, render_template, request, jsonify
import sqlite3, os
import salud

app = Flask(__name__)

# --- Conexión a DB ---
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

init_db()

# --- Páginas ---
@app.route('/')
def index():
    return render_template('html/index.html')

@app.route('/health')
def health():
    return render_template('html/health.html')

@app.route('/medicine')
def medicine():
    return render_template('html/medicine.html')

@app.route('/news')
def news():
    return render_template('html/news.html')

@app.route('/client')
def client():
    return render_template('html/client.html')

@app.route('/contact')
def contact():
    return render_template('html/contact.html')

@app.route("/sedes")
def sedes():
    data = salud.dataframePrestadoresSedes()
    return render_template("sedes.html", data=data)
# --- API ---
@app.route('/api/sintomas', methods=['POST'])
def registrar_sintomas():
    data = request.get_json()
    nombre, sintomas = data['nombre'], data['sintomas']

    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO sintomas (nombre, sintomas) VALUES (?, ?)', (nombre, sintomas))
    conn.commit()
    conn.close()

    return f"Gracias, {nombre}. Registramos tus síntomas: {sintomas}"

@app.route('/api/sintomas', methods=['GET'])
def ver_sintomas():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT nombre, sintomas FROM sintomas')
    datos = cursor.fetchall()
    conn.close()
    return jsonify([dict(fila) for fila in datos])

@app.route('/api/jornadas')
def jornadas():
    jornadas_simuladas = [
        {"fecha": "2025-10-02", "lugar": "Garagoa", "tipo": "Vacunación"},
        {"fecha": "2025-10-05", "lugar": "Provenir", "tipo": "Optometría"},
        {"fecha": "2025-10-10", "lugar": "Sáchica", "tipo": "Odontología"}
    ]
    return jsonify(jornadas_simuladas)



if __name__ == '__main__':
    app.run(debug=True)
