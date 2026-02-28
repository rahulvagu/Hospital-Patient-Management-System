from flask import Flask, render_template, request
from db_config import get_connection

app = Flask(__name__)

# Homepage
@app.route('/')
def index():
    return render_template('index.html')

# View all patients
@app.route('/patients')
def view_patients():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Patients")
    patients = cursor.fetchall()
    conn.close()
    return render_template('view_patients.html', patients=patients)

# View all appointments
@app.route('/appointments')
def view_appointments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.appointment_id, p.name, d.name, a.date, a.reason
        FROM Appointments a
        JOIN Patients p ON a.patient_id = p.patient_id
        JOIN Doctors d ON a.doctor_id = d.doctor_id
        ORDER BY a.date DESC
    """)
    appointments = cursor.fetchall()
    conn.close()
    return render_template('view_appointments.html', appointments=appointments)

# Add new patient
@app.route('/add-patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        age = request.form['age']
        contact = request.form['contact']

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Patients (name, gender, age, contact) VALUES (%s, %s, %s, %s)", 
                       (name, gender, age, contact))
        conn.commit()
        conn.close()
        return "✅ Patient added successfully!"

    return render_template('add_patient.html')

# Add new appointment
@app.route('/add-appointment', methods=['GET', 'POST'])
def add_appointment():
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        patient_id = request.form['patient_id']
        doctor_id = request.form['doctor_id']
        date = request.form['date']
        reason = request.form['reason']

        cursor.execute("INSERT INTO Appointments (patient_id, doctor_id, date, reason) VALUES (%s, %s, %s, %s)",
                       (patient_id, doctor_id, date, reason))
        conn.commit()
        conn.close()
        return "✅ Appointment added successfully!"

    cursor.execute("SELECT patient_id, name FROM Patients")
    patients = cursor.fetchall()

    cursor.execute("SELECT doctor_id, name FROM Doctors")
    doctors = cursor.fetchall()

    conn.close()
    return render_template('add_appointment.html', patients=patients, doctors=doctors)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
