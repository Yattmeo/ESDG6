from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
@app.route('/api/update_appointment', methods=['POST'])
def update_appointment_microservice():
    # Get the request data from the frontend UI
    data = request.get_json()
    # Make a request to the microservice to update the appointment
    microservice_url = 'http://microservice-url/api/update_appointment'
    response = requests.post(microservice_url, json=data)
    # Send a request to the notification microservice
    notification_microservice_url = 'http://notification-microservice-url/api/send_notification'
    notification_data = {
        'message': 'Appointment updated',
        'appointment_id': data['appointment_id']
    }
    notification_response = requests.post(notification_microservice_url, json=notification_data)
    # Return the response from the microservice to the frontend UI
    return jsonify(response.json()), response.status_code


@app.route('/api/appointments/<doctor_id>', methods=['GET'])
def get_appointments(doctor_id):
    # Make a request to the microservice to get all appointment objects for the specific doctorID
    microservice_url = f'http://microservice-url/api/appointments/{doctor_id}'
    response = requests.get(microservice_url)
    # Return the response from the microservice to the frontend UI
    return jsonify(response.json()), response.status_code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)