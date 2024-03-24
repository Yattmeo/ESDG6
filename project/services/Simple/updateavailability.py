from os import environ
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/schedulingDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)
CORS(app)

class Doctor(db.Model):
    __tablename__ = 'Doctors'

    DoctorID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Specialty = db.Column(db.VARCHAR(255))
    Name = db.Column(db.VARCHAR(255), nullable=False)

class DoctorAvailability(db.Model):
    __tablename__ = 'DoctorAvailability'

    AppointmentID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Date = db.Column(db.Date, nullable=False)
    SlotNum = db.Column(db.TINYINT, nullable=False)
    DoctorID_Doctors = db.Column(db.Integer, db.ForeignKey('Doctors.DoctorID'), nullable=False)

    doctor = relationship("Doctor")

@app.route("/schedule/create", methods=['POST'])
def create_availability():
    req_json = request.json
    if 'date' in req_json and 'slots' in req_json and 'doctorID' in req_json:
        date = req_json['date']
        slots = req_json['slots']
        doctor_id = req_json['doctorID']
        try:
            new_avails = [DoctorAvailability(Date=date, SlotNum=slot, DoctorID_Doctors=doctor_id) for slot in slots]
            db.session.add_all(new_avails)
            db.session.commit()
            return jsonify(
                {
                    "responseStatus": "ok",
                    "dateItems": [avail.json() for avail in new_avails]
                }
            )
        except Exception as e:
            return jsonify(
                {
                    "responseStatus": "fail",
                    "message": "An error occurred while creating availability.",
                    "error": str(e)
                }
            ), 500
    else:
        return jsonify(
            {
                "responseStatus": "fail",
                "message": "Missing required fields 'date', 'slots', or 'doctorID' in the request."
            }
        ), 400

@app.route("/appointments/<string:doctor_id>", methods=['GET'])
def get_appointments(doctor_id):
    all_availability = DoctorAvailability.query.filter_by(DoctorID_Doctors=doctor_id).all()
    if all_availability:
        return jsonify(
            {
                "responseStatus": "ok",
                "dateItems": [avail.json() for avail in all_availability]
            }
        )
    else:
        return jsonify(
            {
                "responseStatus": "fail",
                "message": "No availability found for the specified doctor."
            }
        ), 404

@app.route("/schedule/<string:doctor_id>", methods=['PUT'])
def update_availability(doctor_id):
    req_json = request.json
    if 'date' in req_json and 'slots' in req_json:
        date = req_json['date']
        slots = req_json['slots']
        try:
            DoctorAvailability.query.filter_by(DoctorID_Doctors=doctor_id, Date=date).delete()
            new_avails = [DoctorAvailability(Date=date, SlotNum=slot, DoctorID_Doctors=doctor_id) for slot in slots]
            db.session.add_all(new_avails)
            db.session.commit()
            return jsonify(
                {
                    "responseStatus": "ok",
                    "dateItems": [avail.json() for avail in new_avails]
                }
            )
        except Exception as e:
            return jsonify(
                {
                    "responseStatus": "fail",
                    "message": "An error occurred while updating availability.",
                    "error": str(e)
                }
            ), 500
    else:
        return jsonify(
            {
                "responseStatus": "fail",
                "message": "Missing required fields 'date' or 'slots' in the request."
            }
        ), 400

if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage availability ...")
    app.run(host='0.0.0.0', port=5001, debug=True)
