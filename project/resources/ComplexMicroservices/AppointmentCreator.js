// receive from UI to create appointment

JSON = {
    "doctorID": 212345, //doctors always start with 2
    "patientID": 112345, //patients always start with 1
    "date" : "2024-05-17T00:00:00.000Z",
    "slot" : 9 // 900 -> 0900hrs, 930 -> 0930hrs, 1000 -> 1000hrs etc. until 1730 -> 1730hrs
}


// receive from UpdateAppointment
JSON = {
    "responseStatus": "ok", // or "fail"
    "appointmentID" : 123
}

// send to UpdateAppointment to create new appointment
JSON = {
    "requestCode": 1, // new appointment = 1
    "patientID": 112345,
    "doctorID": 212345,
    "date": "2024-05-17T00:00:00.000Z",
    "slot": 9,
    "status": "pending"
  };


// send to notify for both patient and doctor
JSON = {
    "contactNumber": 91234567,
    "messageCode": 0, //0: confirm new appointment.
    "messageDetails": "new appointment" //this can get processed further later by the notify microservice
  }