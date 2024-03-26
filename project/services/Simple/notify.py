from flask import Flask, request, jsonify
from os import environ
import os
from twilio.rest import Client

app = Flask(__name__)

# Find your Account SID and Auth Token at twilio.com/console
account_sid = 'ACea65d1e2ea1abe9ca0e8c443e0cbdc79'
# left blank for now, set in Dockerfile (security risk if exposed and twilio will regenerate it --> need to keep changing)
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

@app.route('/send-notification', methods=['POST'])
def send_notification():
    data = request.json

    try:
        message = twilio_client.messages.create(
            body=data['message'],
            from_= twilio_phone_number,  # Twilio phone number
            to=data['to']  # Recipient's phone number
        )
        
        return jsonify({'message': 'Message sent successfully!', 'sid': message.sid}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)