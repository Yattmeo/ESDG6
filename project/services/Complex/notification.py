from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define the mapping for message codes to actual messages
message_templates = {
    -1: "Please log into your account to confirm a new appointment.",
    0: "Your appointment has been confirmed.",
    1: "Your appointment has been cancelled due to: {reason}. Please log into your account to make a new appointment.",
    2: "Your appointment has been completed."
}

@app.route('/trigger-notification', methods=['POST'])
def trigger_notification():
    # Extract data from incoming JSON
    data = request.get_json()
    
    # Get contact information from updateUserinfo microservice (to update endpoint for updateUserInfo)
    user_info_response = requests.get('http://updateUserinfo_microservice_endpoint', json={
        "patientID": data["patientID"],
        "doctorID": data["doctorID"],
    })

    # Make sure the request was successful
    if user_info_response.status_code != 200:
        return jsonify({"error": "Failed to get user info"}), 500

    user_info = user_info_response.json()
    
    # Determine the recipient and their number
    recipient_type = 'doctor' if data["messageCode"] == -1 else 'patient'
    recipient_number = "+65" + user_info[f"{recipient_type}Number"]

    # Prepare the message
    message = message_templates.get(data["messageCode"]).format(reason=data["messageDetails"])
    
    # Send the message via Twilio
    try:
        twilio_response = requests.post(
            'http://127.0.0.1:5005/send-notification',
            json={
                'message': message,
                'to': data.get('to')
            }
        )

        if twilio_response.ok:
            return jsonify({'message': 'Message sent successfully!'}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, debug=True)