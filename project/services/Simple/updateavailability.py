from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    availability = db.Column(db.Boolean, default=True)  # New field

    def __init__(self, name, email, availability=True):
        self.name = name
        self.email = email
        self.availability = availability

@app.route('/update_user', methods=['POST'])
def update_user():
    user_id = request.json['id']
    new_name = request.json['name']
    new_email = request.json['email']

    user = User.query.get(user_id)
    if user:
        user.name = new_name
        user.email = new_email
        db.session.commit()
        return 'User information updated successfully'
    else:
        return 'User not found'

@app.route('/update_availability', methods=['POST'])  # New route
def update_availability():
    user_id = request.json['id']
    new_availability = request.json['availability']

    user = User.query.get(user_id)
    if user:
        user.availability = new_availability
        db.session.commit()
        return 'User availability updated successfully'
    else:
        return 'User not found'

if __name__ == '__main__':
    db.create_all()
    app.run()