from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.route('/create_appointment', methods=['POST'])
def create_appointment():
    # Get the appointment details from the request
    appointment_data = request.json

    # Make a request to the backend microservice
    response = requests.post('http://updateappointment/appointments/create', json=appointment_data) #need to add backend microservice url

    # Return the response from the backend microservice
    return response.json(), response.status_code


if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage appointments ...")
    app.run(host='0.0.0.0', port=5007, debug=True)