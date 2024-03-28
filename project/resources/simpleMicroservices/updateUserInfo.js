// get user /user/<string:USER_ID>
// GET request
// no json but just specify the USER_ID after the user/ in the url
// returns all user information like this
JSON={
  "code": 200,
  "data": {
    "User_ID": 1,
    "address": "123 Main Street",
    "email": "john@example.com",
    "phone_number": 1234567890
  }
}

  
  // expected response from updateUserinfo
  // JSON = {
  //   "patientNumber": 91234567,
  //   "doctorNumber": 81234567,
  // }
  