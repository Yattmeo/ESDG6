from os import environ

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Date, text, ForeignKey, SmallInteger

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root:root@localhost:3306/schedulingDB'
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

@app.route('/availability', methods=['POST'])
def update_availability():
    data = request.get_json()
    DoctorID_Doctors = data['DoctorID_Doctors']
    Date = data['Date']
    SlotNum = data['SlotNum']

    try:
        availability = DoctorAvailability.query.get((DoctorID_Doctors, Date))
        if availability is None:
            availability = DoctorAvailability(DoctorID_Doctors=DoctorID_Doctors, Date=Date, SlotNum=SlotNum)
            db.session.add(availability)
        else:
            availability.SlotNum = SlotNum
        db.session.commit()
        return jsonify({"responseStatus": "ok", "dateItems": []})
    except Exception as e:
        return jsonify({"responseStatus": "fail", "dateItems": []})

@app.route('/availability/<int:DoctorID_Doctors>', methods=['GET'])
def get_availability(DoctorID_Doctors):
    try:
        availabilities = DoctorAvailability.query.filter_by(DoctorID_Doctors=DoctorID_Doctors).all()
        dateItems = [{"Date": a.Date, "SlotNum": a.SlotNum} for a in availabilities]
        return jsonify({"responseStatus": "ok", "dateItems": dateItems})
    except Exception as e:
        return jsonify({"responseStatus": "fail", "dateItems": []})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005,debug=False)