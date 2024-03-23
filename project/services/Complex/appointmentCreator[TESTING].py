from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/create_appointment', methods=['POST'])
def create_appointment():
    # Get the appointment details from the request
    appointment_data = request.json

    # Make a request to the backend microservice
    response = requests.post('http://backend_microservice_url/appointments/create', json=appointment_data) #need to add backend microservice url

    # Return the response from the backend microservice
    return response.json(), response.status_code

if __name__ == '__main__':
    app.run()