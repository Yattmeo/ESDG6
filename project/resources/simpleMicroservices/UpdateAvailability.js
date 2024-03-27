// expected for update availability
JSON = {
    "requestType" : 1, // 0: get availability, 1: update availability
    "doctorID": 212345,
    "date": "2024-05-17T00:00:00.000Z",
    "slots": [
      4
    ]
  }
// every time availability for a specific date is updated, it will rewrite the slots attribute in the database for the specific date

// response for update availability
JSON = {
  "responseStatus": "ok", // or "fail"
  "dateItems": []
    }


// expected for GET availability
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

// response for GET availibility
JSON = {
  "responseStatus": "ok", // or "fail"
  "dateItems": [
    {
      "date": "2024-05-17T00:00:00.000Z",
      "slots": [
          12
      ]
    },
    {
      "date": "2024-05-18T00:00:00.000Z",
      "slots": [
          14
      ]
    },
]
}