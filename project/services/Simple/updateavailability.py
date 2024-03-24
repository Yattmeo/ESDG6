
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
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/order'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)  

class schedule(db.Model):
    __tablename__ = 'DoctorAvailability'

    AppointmentID = db.Column(db.Integer, autoincrement=True, primary_key=True)
    Date = db.Column(db.Date, nullable=False)
    SlotNum = db.Column(db.SmallInteger, nullable=False)
    DoctorID_Doctors = db.Column(db.Integer, db.ForeignKey('Doctors.DoctorID'), nullable=False)

    doctor_relation = relationship("Doctor")


    def json(self):
        dto = {
            'appointmentID': self.AppointmentID,
            'date': self.Date,
            'SlotNum': self.SlotNum,
            'doctorID_doctors': self.DoctorID_Doctors,
        }
        return dto

@app.route("/schedule/create", methods=['POST'])
def create_availability():
    date = request.json.get('date',None)
    doctorID = request.json.get('doctorID',None)
    patientID = request.json.get('patientID',None)
    slot = request.json.get('slot',None)
    
    new_appt = Appointment(date=date,
                           slot=slot, 
                           doctorID=doctorID, 
                           patientID=patientID,
                           status="pending")

    try:
        db.session.add(new_appt)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": new_appt.json(),
                "message": "An error occurred while creating the appointment. " + str(e)
            }
        ), 500
    
    print("Appointment created successfully.")
    print(json.dumps(new_appt.json(), indent=4,default=str))   
    
    return jsonify(
        {
            "code": 201,
            "data": new_appt.json()
        }
    )

@app.route("/appointments/<string:doctor_id>", methods=['GET'])
def get_appointments(doctor_id):
    all_appts = db.session.scalars(db.select(Appointment).filter_by(DoctorID_Doctors=doctor_id))
    if len(all_appts):
        return jsonify(
            {
                "code": 200,
                "appointments": {
                    "orders": [appt.json() for appt in all_appts]
                }
            }
        )
    else:
        return jsonify(
        {
            "code": 404,
            "message": "There are no appointments."
        }
    ), 404

@app.route("/schedule/<string:doctor_id>", methods=['PUT'])
def update_availability(appt_id):

    date = request.json.get('date',None)
    clinic = request.json.get('clinic',None)
    doctorID = request.json.get('doctorID',None)
    patientID = request.json.get('patientID',None)
    status = request.json.get('status',None)
    
    appointment = Appointment.query.get(appt_id)
    if appointment:
        appointment.date = date
        appointment.clinic = clinic
        appointment.doctorID = doctorID
        appointment.patientID = patientID
        appointment.status = status
        try:
            db.session.commit()
        except Exception as e:
            return jsonify(
                {
                    "code": 500,
                    "message": "An error occurred while updating availability. " + str(e)
                }
            ), 500
        return jsonify(
            {
                "code": 200,
                "message": "Availability updated successfully."
            }
        )
    else:
        return jsonify(
            {
                "code": 404,
                "message": "Availability not found."
            }
        ), 404

if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage appointments ...")
    app.run(host='0.0.0.0', port=5001, debug=True)
