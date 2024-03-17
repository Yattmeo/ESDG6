// receive from UI
JSON = {
    "requestCode": 1, // new EHR = 1, amend EHR = 0, delete EHR = -1, GET EHR = 2
    "patientID": 112345,
    "medical_conditions" : "",
    "allergies" : "",
    "surgeries" : "",
    "immunisations" : "",
    "family_medical_history" : "",
    "past_appointments" : "",
    "make_appointment" : "yes", // or "no"
    "make_appointment_details" : "follow up with cardiologist" //this field is only read if make_appointments is yes
  };


// send to updateEHR
JSON = {
    "requestCode": 1, // new EHR = 1, amend EHR = 0, delete EHR = -1, GET EHR = 2
    "patientID": 112345,
    "medical_conditions" : "",
    "allergies" : "",
    "surgeries" : "",
    "immunisations" : "",
    "family_medical_history" : "",
    "past_appointments" : "",
  };


// json to send to notify
JSON = {
    "patientID": 112345,
    "doctorID": null,
    "messageCode": 1, //1: please make a new appointment
    "messageDetails": "follow up with cardiologist" //this can get processed further later by the notify microservice
  }