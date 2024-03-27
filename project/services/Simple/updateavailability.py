from os import environ

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Date, text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@root:8889/availabilitydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)
CORS(app)

class Doctor(db.Model):
    __tablename__ = 'doctors'

    doctorID = Column(Integer, primary_key=True)
    Specialty = Column(String)
    Name = Column(String)

class Availability(db.Model):
    __tablename__ = 'availability'

    doctorID = Column(Integer, primary_key=True)
    date = Column(Date, primary_key=True)
    slots = Column(String)

def json(self):
        dto = {
            'doctorID': self.doctorID,
            'date': self.date,
            'Slots': self.slots,
        }
        return dto

@app.route('/availability', methods=['POST'])
def update_availability():
    data = request.get_json()
    doctorID = data['doctorID']
    date = data['date']
    slots = data['slots']

    try:
        availability = Availability.query.get((doctorID, date))
        if availability is None:
            availability = Availability(doctorID=doctorID, date=date, slots=str(slots))
            db.session.add(availability)
        else:
            availability.slots = str(slots)
        db.session.commit()
        return jsonify({"responseStatus": "ok", "dateItems": []})
    except Exception as e:
        return jsonify({"responseStatus": "fail", "dateItems": []})

@app.route('/availability/<int:doctorID>', methods=['GET'])
def get_availability(doctorID):
    try:
        availabilities = Availability.query.filter_by(doctorID=doctorID).all()
        dateItems = [{"date": a.date, "slots": eval(a.slots)} for a in availabilities]
        return jsonify({"responseStatus": "ok", "dateItems": dateItems})
    except Exception as e:
        return jsonify({"responseStatus": "fail", "dateItems": []})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)