from os import environ

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Date, text, ForeignKey, SmallInteger
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root:root@localhost:8889/schedulingDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)
CORS(app)

class Doctor(db.Model):
    __tablename__ = 'Doctors'

    DoctorID = Column(Integer, primary_key=True)
    Specialty = Column(String)
    Name = Column(String, nullable=False)

class DoctorAvailability(db.Model):
    __tablename__ = 'DoctorAvailability'

    AppointmentID = Column(Integer, primary_key=True)
    Date = Column(Date, nullable=False)
    SlotNum = Column(SmallInteger, nullable=False)
    DoctorID_Doctors = Column(Integer, ForeignKey('Doctors.DoctorID'), nullable=False)

    def json(self):
            dto = {
            'AppointmentID': self.AppointmentID,
            'Date': self.Date,
            'SlotNum': self.SlotNum,
            'DoctorID_Doctors': self.DoctorID_Doctors,
        }
            return dto

@app.route('/availability/<string:doctorID>/<string:date>', methods=['POST'])
def update_availability(doctorID, date):
    doctorID = int(doctorID)  # Convert doctorID to int
    date = datetime.strptime(date, '%Y-%m-%d').date()  # Convert date to Date object

    if (db.session.query(DoctorAvailability).filter_by(DoctorID_Doctors=doctorID, Date=date).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "DoctorID_Doctors": doctorID,
                    "Date": date
                },
                "message": "Availability already exists."
            }
        ), 400

    data = request.get_json()
    slotNum = data['SlotNum']

    # If SlotNum is a list, get the first element
    if isinstance(slotNum, list):
        slotNum = slotNum[0]

    availability = DoctorAvailability(DoctorID_Doctors=doctorID, Date=date, SlotNum=slotNum)

    try:
        db.session.add(availability)
        db.session.commit()
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "DoctorID_Doctors": doctorID,
                    "Date": date
                },
                "message": "An error occurred updating the availability: " + str(e)
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": availability.json()
        }
    ), 201

@app.route('/availability/<int:DoctorID_Doctors>', methods=['GET'])
def get_availability(DoctorID_Doctors):
    try:
        availabilities = DoctorAvailability.query.filter_by(DoctorID_Doctors=DoctorID_Doctors).all()
        dateItems = [{"Date": a.Date, "SlotNum": a.SlotNum} for a in availabilities]
        if len(dateItems) == 0:
            return jsonify({"responseStatus": 404, "dateItems": []})
        else:
            return jsonify({"responseStatus": 200, "dateItems": dateItems})
    except Exception as e:
        return jsonify({"responseStatus": 404, "dateItems": []})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005,debug=False)