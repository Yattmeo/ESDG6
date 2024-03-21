from flask import Flask
from user_details import db, get_user_details  # Import db and the route function
import os
from flask_cors import CORS

# Create the Flask app instance
app = Flask(__name__)

# Configure SQLAlchemy and CORS
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/USERDETAILS'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
CORS(app)

# Register the route function with the app
app.route("/user/<int:User_ID>")(get_user_details)

# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("Welcome to CAREMD " + os.path.basename(__file__))
    app.run(host="0.0.0.0", port=5003, debug=True)
