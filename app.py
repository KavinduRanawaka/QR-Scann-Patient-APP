from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
import qrcode

app = Flask(__name__)

DB_FILE = 'patients.db'

# Ensure the static/qr_codes/ folder exists
QR_FOLDER = os.path.join('static', 'qr_codes')
os.makedirs(QR_FOLDER, exist_ok=True)


# 🔧 Initialize the database
def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                patient_id TEXT NOT NULL UNIQUE,
                age INTEGER,
                nic TEXT,
                pin TEXT,
                qr_code TEXT
            )
        ''')

# 🏠 Home page — Register new patient
@app.route('/')
def register():
    return render_template('register.html')

# 📝 Handle patient registration
@app.route('/register', methods=['POST'])
def register_patient():
    name = request.form['name']
    patient_id = request.form['patient_id']
    age = request.form['age']
    nic = request.form['nic']
    pin = str(patient_id)[-4:]  # Simple PIN (last 4 digits of patient_id)
    qr_data = f"http://localhost:5000/patient/{patient_id}"  # QR link

    # 🧾 Generate QR Code image
    qr_img = qrcode.make(qr_data)
    qr_filename = f"{patient_id}.png"
    qr_path = os.path.join(QR_FOLDER, qr_filename)
    qr_img.save(qr_path)

    # 💾 Save to SQLite database
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute('''
            INSERT INTO patients (name, patient_id, age, nic, pin, qr_code)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, patient_id, age, nic, pin, qr_filename))

    return render_template("success.html", name=name, pin=pin, qr_image=qr_filename)
@app.route('/access')
def access_page():
    return render_template('access.html')

@app.route('/access/pin', methods=['POST'])
def access_by_pin():
    pin = request.form['pin']
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.execute('SELECT patient_id FROM patients WHERE pin=?', (pin,))
        row = cursor.fetchone()
        if row:
            return redirect(url_for('patient_profile', patient_id=row[0]))
        else:
            return "Invalid PIN", 401

@app.route('/patient/<patient_id>')
def patient_profile(patient_id):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.execute('SELECT name, age, nic, pin, qr_code FROM patients WHERE patient_id=?', (patient_id,))
        row = cursor.fetchone()
        if row:
            return render_template('profile.html', patient_id=patient_id, name=row[0], age=row[1], nic=row[2], pin=row[3], qr_image=row[4])
        else:
            return "Patient not found", 404

# 🔁 Run the app
if __name__ == '__main__':
    if not os.path.exists(DB_FILE):
        init_db()
    app.run(debug=True)
