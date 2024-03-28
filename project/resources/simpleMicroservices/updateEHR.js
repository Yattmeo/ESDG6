// get ehr /ehr/<string:patient_id>
// GET request
// no json but just specify the patient_id after the ehr/ in the url
// returns all ehr with the specified patient_id like this
JSON= {
  "code": 200,
  "data": {
    "allergies": "Penicillin",
    "family_medical_history": "Heart disease in family",
    "immunisations": "Flu Vaccine",
    "medical_conditions": "Hypertension",
    "medications": "Lisinopril",
    "past_appointments": "Sun, 15 Jan 2023 10:30:00 GMT",
    "patient_id": 1,
    "surgeries": "Appendectomy"
  }
}

// expected input POST/PUT ehr /ehr/<string:patient_id>
// POST/PUT request (POST to create if there isn't an EHR. POST/PUT to update ehr)
// specify the patient_id after the ehr/ in the url
// returns all ehr with the specified patient_id like this
// can just send in fields that have been changed


  JSON = {
    "medical_conditions": "Updated condition",
    "allergies": "Updated allergies"
}

// JSON = {
//     "requestCode": 1, // new EHR = 1, amend EHR = 0, delete EHR = -1, GET EHR = 2
//     "patient_id": 1,
//     "medical_conditions" : "",
//     "allergies" : "",
//     "medications" : "",
//     "surgeries" : "",
//     "immunisations" : "",
//     "family_medical_history" : "",
//     "past_appointments" : "",
//   };

// expected response to EHR
// JSON = {
//     "responseStatus": "ok", // or "fail"
//     "appointmentNotif": "ok" // or "fail" or null
// }

