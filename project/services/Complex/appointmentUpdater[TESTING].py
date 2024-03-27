from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
@app.route('/updateappointment/<appointment_id>', methods=['POST'])
def update_appointment_microservice(appointment_id):
    # Get the request data from the frontend UI
    data = request.get_json()
    # Make a request to the microservice to update the appointment
    microservice_url = 'http://updateAppointment/appointments/' + appointment_id
    response = requests.put(microservice_url, json=data)

    response_text = response.json()
    
    # Send a request to the notification microservice
    notification_data = {
        'message': 'response_text',
        'appointment_id': appointment_id,
        'doctorID': request.json.get('doctorID', None),
        'patientID': request.json.get('patientID', None),
    }
    notification_microservice_url = 'http://notify/send_notification'
    
    notification_response = requests.post(notification_microservice_url, json=notification_data)
    # Return the response from the microservice to the frontend UI
    return jsonify(response.json()), response.status_code


@app.route('/getappointment/<doctor_id>', methods=['GET'])
def get_appointments(doctor_id):
    # Make a request to the microservice to get all appointment objects for the specific doctorID
    microservice_url = f'http://updateAppointment/appointments/{doctor_id}'
    response = requests.get(microservice_url)
    # Return the response from the microservice to the frontend UI
    return jsonify(response.json()), response.status_code


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)