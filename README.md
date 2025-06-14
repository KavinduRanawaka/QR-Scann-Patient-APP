

# Patient QR Management System

This is a web-based application built using **HTML, CSS, JavaScript**, and **Flask**. It allows for patient registration and QR code generation. Doctors can scan the QR code to instantly navigate to the patient's profile, streamlining access to patient data.

## 🔧 Features

- 📷 Scan QR codes using the `html5-qrcode` library
- 📝 Register new patients
- 🆔 Generate unique QR codes for each registered patient
- 👨‍⚕️ Allow doctors to scan QR codes and access patient profiles
- 🗃️ Flask-based backend to manage data and routing


## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **QR Code Scanning**: [html5-qrcode](https://github.com/mebjas/html5-qrcode)
- **Backend**: Python, Flask
- **QR Code Generation**: Python QR code libraries like `qrcode`

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/KavinduRanawaka/QR-Scann-Patient-APP.git
   cd your-repo-name

    Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Run the Flask app

    python app.py

    Open your browser and navigate to http://127.0.0.1:5000





