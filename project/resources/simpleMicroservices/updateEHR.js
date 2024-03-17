// expected input
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

// expected response to EHR
JSON = {
    "responseStatus": "ok", // or "fail"
    "appointmentNotif": "ok" // or "fail" or null
}

