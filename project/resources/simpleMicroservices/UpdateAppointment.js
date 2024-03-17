// this is the expected input to the microservice

JSON = {
    "requestCode": 1, // new appointment = 1, amend appointment = 0, delete appointment = -1, GET appointments = 2
  // following fields can be NULL ONLY FOR GET APPOINTMENTS to act as filters
    "patientID": 1,
    "doctorID": 1,
    "date": "2024-05-17T00:00:00.000Z",
    "slot": 9,
    "status": "pending"
  };

  // for amend appointment, this should trigger the deletion of the specific row and creation a new one


  // response (appointments list is only populated in a GET request, otherwise null)
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