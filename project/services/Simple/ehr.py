from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL') or 'mysql+mysqlconnector://root:root@localhost:3306/EHR'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

class Ehr(db.Model):
    __tablename__ = 'ehr'
    patient_id = db.Column(db.Integer, primary_key=True)
    medical_conditions = db.Column(db.String(255))
    allergies = db.Column(db.String(255))
    medications = db.Column(db.String(255))
    surgeries = db.Column(db.String(255))
    immunisations = db.Column(db.String(255))
    family_medical_history = db.Column(db.String(255))
    past_appointments = db.Column(db.DateTime) 

    def __init__(self, patient_id, medical_conditions, allergies, medications, surgeries, immunisations, family_medical_history, past_appointments):
        self.patient_id = patient_id
        self.medical_conditions = medical_conditions
        self.allergies = allergies
        self.medications = medications
        self.surgeries = surgeries
        self.immunisations = immunisations
        self.family_medical_history = family_medical_history
        self.past_appointments = past_appointments

    def json(self):
        return {
            "patient_id": self.patient_id,
            "medical_conditions": self.medical_conditions,
            "allergies": self.allergies,
            "medications": self.medications,
            "surgeries": self.surgeries,
            "immunisations": self.immunisations,
            "family_medical_history": self.family_medical_history,
            "past_appointments": self.past_appointments
        }

# Route to get ehr by patient_id
@app.route("/ehr/<int:patient_id>")
def get_patient_ehr(patient_id):
    ehr = Ehr.query.filter_by(patient_id=patient_id).first()
    if ehr:
        return jsonify(
            {
                "code": 200,
                "data": ehr.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "No EHR for patient"
        }
    ), 404

# Route to create or update Ehr data for a specific patient
@app.route("/ehr/<int:patient_id>", methods=['POST', 'PUT'])
def create_or_update_patient_ehr(patient_id):
    try:
        # Check if the Ehr record exists
        ehr = Ehr.query.filter_by(patient_id=patient_id).first()
        if ehr:
            # Update the existing Ehr record
            data = request.get_json()
            ehr.medical_conditions = data.get('medical_conditions', ehr.medical_conditions)
            ehr.allergies = data.get('allergies', ehr.allergies)
            ehr.medications = data.get('medications', ehr.medications)
            ehr.surgeries = data.get('surgeries', ehr.surgeries)
            ehr.immunisations = data.get('immunisations', ehr.immunisations)
            ehr.family_medical_history = data.get('family_medical_history', ehr.family_medical_history)
            ehr.past_appointments = data.get('past_appointments', ehr.past_appointments)
        else:
            # Create a new Ehr record
            data = request.get_json()
            ehr = Ehr(
                patient_id=patient_id,
                medical_conditions=data.get('medical_conditions'),
                allergies=data.get('allergies'),
                medications=data.get('medications'),
                surgeries=data.get('surgeries'),
                immunisations=data.get('immunisations'),
                family_medical_history=data.get('family_medical_history'),
                past_appointments=data.get('past_appointments')
            )
            db.session.add(ehr)
            db.session.commit()
            return jsonify(
                {
                    "code": 201,
                    "data": ehr.json(),
                    "message": "EHR created successfully."
                }
            ), 201
        
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": ehr.json(),
                "message": "EHR updated successfully."
            }
        ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "patient_id": patient_id
                },
                "message": "An error occurred while updating the record. " + str(e)
            }
        ), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)
