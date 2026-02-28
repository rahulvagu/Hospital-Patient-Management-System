# 🏥 Hospital Patient Management System

A web-based Hospital Patient Management System developed using **Flask** and **MySQL** to efficiently store and manage patient records.  
The system allows adding, updating, viewing, and deleting patient details along with diagnosis and treatment information.

---

## 🚀 Features

- Add new patient records
- View patient details
- Update patient information
- Delete patient records
- Store diagnosis and treatment data
- Search patient by ID or name
- MySQL database integration
- Clean and responsive UI

---

## 🛠️ Tech Stack

- Frontend: HTML, CSS, Bootstrap
- Backend: Flask (Python)
- Database: MySQL
- Template Engine: Jinja2

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository
### 2️⃣ Create Virtual Environment
    python -m venv venv
### 3️⃣ Install Dependencies
    pip install -r requirements.txt
### 4️⃣ Database Configuration (MySQL)
    Open MySQL and create a database:
    CREATE DATABASE hospital_db;
    Import the provided SQL file into the database.
    Update your MySQL credentials in app.py:
    mysql = MySQL(app)
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'your_username'
    app.config['MYSQL_PASSWORD'] = 'your_password'
    app.config['MYSQL_DB'] = 'hospital_db'
### 5️⃣ Run the Application
    python app.py
    Open in browser:
    http://127.0.0.1:5000
```bash
git clone https://github.com/rahulvagu/your-hospital-repo-name.git
cd your-hospital-repo-name
