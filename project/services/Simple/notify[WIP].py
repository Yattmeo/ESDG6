from flask import Flask, request, jsonify
import requests
from invokes import invoke_http
from os import environ
import os
from twilio.rest import Client

app = Flask(__name__)

# Find your Account SID and Auth Token at twilio.com/console
account_sid = 'ACea65d1e2ea1abe9ca0e8c443e0cbdc79'
# left blank for now (security risk if exposed and twilio will regenerate it --> need to keep changing)
auth_token = ''
twilio_phone_number = '+18783488056' #free trial number
# To set up environmental variables, see http://twil.io/secure
# for some reason i cant get env var to work in twilio.env
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']

#initialise twilio client
twilio_client = Client(account_sid, auth_token)

#test
# message = twilio_client.messages \
#                 .create(
#                      body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#                      from_='+18783488056',
#                      to='+6596379881'
#                  )
# print(message.sid)

# Define the mapping for message codes to actual messages
message_templates = {
    -1: "Please log into your account to confirm a new appointment.",
    0: "Your appointment has been confirmed.",
    1: "Your appointment has been cancelled due to: {reason}. Please log into your account to make a new appointment.",
    2: "Your appointment has been completed."
}

@app.route('/notify', methods=['POST'])
def notify():
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
        message_sent = twilio_client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=recipient_number
        )
        # Return a success response
        return jsonify({"message": "Notification sent successfully.", "sid": message_sent.sid}), 200
    except Exception as e:
        # Log the exception e
        return jsonify({"error": "Failed to send notification"}), 500

if __name__ == '__main__':
    app.run(debug=True)