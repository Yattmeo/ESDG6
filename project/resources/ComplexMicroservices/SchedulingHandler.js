// updating availability
// request from UI
JSON = {
    "requestType" : 1, // 0: get availability, 1: update availability
    "doctorID": 212345,
    "dateItems": [
        {
            "date": "2024-05-17T00:00:00.000Z",
            "slots": [
                930,
                1000,
                1100,
                1200
            ]
        }
    ]
  }

// to send to updateAvailability for each dateItem
JSON = {
    "requestType" : 1, // 0: get availability, 1: update availability
    "doctorID": 212345,
    "date": "2024-05-17T00:00:00.000Z",
    "slots": [
      9,
      10,
      11,
      12
    ]
  }

// expected response
JSON = {
    "responseStatus": "ok", // or "fail"
    "dateItems": []
      }

// send back to UI
JSON = {
    "responseStatus": "ok", // or "fail"
    "dateItems": []
      }

// ########################################################################################################
// aggregating availability and appointments

// request from UI
JSON = {
    "requestType" : 0, // 0: get availability, 1: update availability
    "doctorID": 212345,
    "dateItems": [
        {
            "date": "2024-05-17T00:00:00.000Z",
            "slots": null
        },
        {
            "date": "2024-05-18T00:00:00.000Z",
            "slots": null
        },
        {
            "date": "2024-05-19T00:00:00.000Z",
            "slots": null
        }
    ]
  }

// to send to updateAvailability to get availability
JSON = {
    "requestType" : 0, // 0: get availability, 1: update availability
    "doctorID": 212345,
    "dateItems": [
        {
            "date": "2024-05-17T00:00:00.000Z",
            "slots": null
        },
        {
            "date": "2024-05-18T00:00:00.000Z",
            "slots": null
        },
        {
            "date": "2024-05-19T00:00:00.000Z",
            "slots": null
        }
    ]
  }

// expected response for availability
JSON = {
    "responseStatus": "ok", // or "fail"
    "dateItems": [
      {
        "date": "2024-05-17T00:00:00.000Z",
        "slots": [
            930,
            1000,
            1100,
            1200
        ]
      },
      {
        "date": "2024-05-18T00:00:00.000Z",
        "slots": [
            930,
            1000,
            1100,
            1200
        ]
      },
  ]
  }

// to send to updateAppointment to get Appointments
JSON = {
    "requestCode": 2, //GET appointments = 2
    "doctorID": 212345,
    "date": "2024-05-17T00:00:00.000Z",
    "slot": null,
    "status": null
  };

  // expected response for appointments
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
            "patientID": 112346,
            "doctorID": 212345,
            "status": 'confirmed'
        }
    ]
}

// to send to UI
JSON = {
    "responseStatus": "ok", // or "fail"
    "schedule": [
        {
          "date": "2024-05-17T00:00:00.000Z",
          "slots": [
              930,
              1000,
              1100,
              1200
          ]
        },
        {
          "date": "2024-05-18T00:00:00.000Z",
          "slots": [
              930,
              1000,
              1100,
              1200
          ]
        }],
    "appointments": [
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
            "patientID": 112346,
            "doctorID": 212345,
            "status": 'confirmed'
        }]
      }
