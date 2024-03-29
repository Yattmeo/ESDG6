from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL') or 'mysql+mysqlconnector://root:root@localhost:3306/USERDETAILS'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user_details'
    User_ID = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.BigInteger)
    email = db.Column(db.String(255))
    address = db.Column(db.String(255))

    def __init__(self, User_ID, phone_number, email, address):
        self.User_ID = User_ID
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def json(self):
        return {"User_ID": self.User_ID, "phone_number": self.phone_number, "email": self.email, "address": self.address}

# Route to get user details by User_ID
@app.route("/user/<int:User_ID>")
def get_user_details(User_ID):
    user = User.query.filter_by(User_ID=User_ID).first()
    if user:
        return jsonify({"code": 200, "data": user.json()})
    return jsonify({"code": 404, "message": "User not found."}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
