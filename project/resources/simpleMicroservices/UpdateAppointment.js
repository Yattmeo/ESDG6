
// create appointment /appointments/create
// POST request
JSON = {
  "date": "2024-04-01 10:00:00",
  "doctorID": 2,
  "patientID": 3,
  "slot": 2
}


// get appointments /appointments/<string:doctor_id>
// GET request
// no json but just specify the doctor_id after the appointments/ in the url
// returns all appointments for the doctor with the specified doctor_id like this
JSON = {
  "appointments": [
      {
          "AppointmentID": 1,
          "Datetime": "2024-03-25 08:00:00",
          "DoctorID": 1,
          "PatientID": 2,
          "Slot": 1,
          "Status": "Confirmed"
      },
      {
          "AppointmentID": 5,
          "Datetime": "2024-03-27 08:30:00",
          "DoctorID": 1,
          "PatientID": 5,
          "Slot": 1,
          "Status": "Confirmed"
      }
  ],
  "code": 200
}



// update appointment /appointments/update/<string:appointment_id>
// PUT request
JSON = {
  "date": "2024-03-25 08:00:00",
  "doctorID": 1,
  "patientID": 2,
  "slot": 1,
  "status": "Confirmed"
}