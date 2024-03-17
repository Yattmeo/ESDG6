// receive from UI
JSON = {
    "requestCode": 0, //amend appointment = 0, delete appointment = -1, GET appointments = 2
    "patientID": 112345,
    "doctorID": 212345,
    "date": "2024-05-17T00:00:00.000Z",
    "slot": 9,
    "status": "confirmed"
  };


// example: send to UpdateAppointment to amend appointment details
JSON = {
    "requestCode": 0, // amend appointment = 0
    "patientID": 112345,
    "doctorID": 212345,
    "date": "2024-05-17T00:00:00.000Z",
    "slot": 9,
    "status": "confirmed"
  };

// example: send to UpdateAppointment to search for appointments on this date
JSON = {
    "requestCode": 2, // amend appointment = 0
    "patientID": null,
    "doctorID": null,
    "date": "2024-05-17T00:00:00.000Z",
    "slot": null,
    "status": "null"
  };


// receive from UpdateAppointment (appointments list is only populated in a GET request, otherwise null)
JSON = {
    "responseStatus": "ok", // or "fail"
    "appointments" : [
        {
            "appointmentID": 123,
            "date": "2024-05-17T00:00:00.000Z",
            "slot": 9,
            "patientID": 112345,
            "doctorID": 212345,
            "status": 'confirmed'
        },
        {
            "appointmentID": 124,
            "date": "2024-05-17T00:00:00.000Z",
            "slot": 12,
            "patientID": 112345,
            "doctorID": 212345,
            "status": 'confirmed'
        }
    ]
    
}


// send to notify for cancelled appointment
JSON = {
    "patientID": 112345,
    "doctorID": 212345,
    "messageCode": -1, // -1: apppointment cancelled, 0: confirm new appointment
    "messageDetails": "doctor unavailable due to family emergency, please reschedule" //this can get processed further later by the notify microservice
  }
