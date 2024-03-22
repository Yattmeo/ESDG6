// this is the expected input to the microservice

JSON = {
    "patientID": 112345,
    "doctorID": 212345,
    "messageCode": -1, // -1: apppointment cancelled, 0: confirm new appointment, 1: please make a new appointment
    "messageDetails": "doctor unavailable" //this can get processed further later by the notify microservice
  }


// get request to updateUserinfo for contact information
JSON = {
  "patientID": 112345,
  "doctorID": 212345,
}
// expected json from updateUserinfo
JSON = {
  "patientNumber": 91234567,
  "doctorNumber": 81234567,
}

// format to send to twillo
//idk gotta go research
message_sent = twilio_client.messages.create(
  body=message,
  from_= +18783488056,
  to=recipient_number
)

// response to whoever
JSON = {
  "responseStatus": "ok", // or "fail"
}