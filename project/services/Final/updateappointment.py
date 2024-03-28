
#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script

from os import environ
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy.orm import relationship

from datetime import datetime
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL') or 'mysql+mysqlconnector://root:root@localhost:8889/APPOINTMENTDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)  


# Define the 'Appointments' class
class Appointments(db.Model):
    __tablename__ = 'Appointments'

    AppointmentID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    DoctorID_Doctors = db.Column(db.Integer,db.ForeignKey('Doctors.DoctorID'), nullable=False, )
    PatientID_Patients = db.Column(db.String(255),db.ForeignKey('Patients.PatientID'), nullable=False)
    Datetime = db.Column(db.DateTime, nullable=False)
    Slot = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(255), nullable=False)
    
    doctor_relation = relationship("Doctors", back_populates="appointments")
    patient_relation = relationship("Patients", back_populates="appointments")

    def json(self):
        return {
            'AppointmentID': self.AppointmentID,
            'DoctorID': self.DoctorID_Doctors,
            'PatientID': self.PatientID_Patients,
            'Datetime': self.Datetime.strftime('%Y-%m-%d %H:%M:%S'),
            'Slot': self.Slot,
            'Status': self.status
        }

#  Define the 'Patients' class
class Patients(db.Model):
    __tablename__ = 'Patients'

    PatientID = db.Column(db.Integer, primary_key=True, nullable=False)
    Name = db.Column(db.String(255), nullable=False)

    # Define the relationship after the 'Appointment' class has been defined
    appointments = relationship("Appointments", back_populates="patient_relation")


# Define the 'Doctors' class
class Doctors(db.Model): 
    __tablename__ = 'Doctors'

    DoctorID = db.Column(db.Integer, primary_key=True)
    Specialty = db.Column(db.String(255), nullable=True)
    Name = db.Column(db.String(255), nullable=False)

    # Define the relationship after the 'Appointments' class has been defined
    appointments = relationship("Appointments", back_populates="doctor_relation")


@app.route("/appointments/create", methods=['POST'])
def create_appointment():
    date = request.json.get('date', None)
    doctor_id = request.json.get('doctorID', None)
    patient_id = request.json.get('patientID', None)
    slot = request.json.get('slot', None)
    
    new_appt = Appointments(
        Datetime=date,
        Slot=slot, 
        DoctorID_Doctors=doctor_id, 
        PatientID_Patients=patient_id,
        status="pending"
    )

    try:
        db.session.add(new_appt)
        db.session.commit()
        return jsonify(
            {
                "code": 201,
                "data": new_appt.json(),
                "message": "Appointment created successfully."
            }
        ), 201
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while creating the appointment. " + str(e)
            }
        ), 500

@app.route("/appointments/<string:doctor_id>", methods=['GET'])
def get_appointments(doctor_id):
    all_appts = db.session.query(Appointments).filter_by(DoctorID_Doctors=doctor_id).all()
    if all_appts:
        return jsonify(
            {
                "code": 200,
                "appointments": 
                     [appt.json() for appt in all_appts]
                
            }
        )
    else:
        return jsonify(
            {
                "code": 404,
                "message": "There are no appointments for the specified doctor."
            }
        ), 404

@app.route("/appointments/update/<string:appointment_id>", methods=['PUT'])
def update_appointment(appointment_id):

    date = request.json.get('date', None)
    # clinic = request.json.get('clinic', None)  # This seems to be unused in your function
    doctorID = request.json.get('doctorID', None)
    patientID = request.json.get('patientID', None)
    status = request.json.get('status', None)
    
    appointment = Appointments.query.get(appointment_id)
    if appointment:
        if date is not None:
            appointment.Datetime = date
        if doctorID is not None:
            appointment.DoctorID_Doctors = doctorID
        if patientID is not None:
            appointment.PatientID_Patients = patientID
        if status is not None:
            appointment.status = status
        try:
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "message": "Appointment updated successfully."
                }
            )
        except Exception as e:
            return jsonify(
                {
                    "code": 500,
                    "message": "An error occurred while updating the appointment. " + str(e)
                }
            ), 500
    else:
        return jsonify(
            {
                "code": 404,
                "message": "Appointment not found."
            }
        ), 404

if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage appointments ...")
    app.run(host='0.0.0.0', port=5008, debug=True)