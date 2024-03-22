
#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script

from os import environ
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from datetime import datetime
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/order'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)  

## WIP ##
class Appointment(db.Model):
    __tablename__ = 'Appointments'

    # order_id = db.Column(db.Integer, primary_key=True)
    # customer_id = db.Column(db.String(32), nullable=False)
    # status = db.Column(db.String(10), nullable=False)
    # created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    # modified = db.Column(db.DateTime, nullable=False,
    #                      default=datetime.now, onupdate=datetime.now)

    def json(self):
        dto = {
            # 'order_id': self.order_id,
            # 'customer_id': self.customer_id,
            # 'status': self.status,
            # 'created': self.created,
            # 'modified': self.modified
        }

        dto['order_item'] = []
        for oi in self.order_item:
            dto['order_item'].append(oi.json())

        return dto

## WIP ##
class Appointments(db.Model):
    __tablename__ = 'order_item'

    item_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.ForeignKey(
        'order.order_id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    book_id = db.Column(db.String(13), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    # order_id = db.Column(db.String(36), db.ForeignKey('order.order_id'), nullable=False)
    # order = db.relationship('Order', backref='order_item')
    order = db.relationship(
        'Order', primaryjoin='Order_Item.order_id == Order.order_id', backref='order_item')

    def json(self):
        return {'item_id': self.item_id, 'book_id': self.book_id, 'quantity': self.quantity, 'order_id': self.order_id}

## WIP ##
@app.route("/appointments/<string:doctor_id>", methods=['GET'])
def get_appointments(doctor_id):
    all_appts = db.session.scalars(db.select(Appointments).filter_by(doctor_id=doctor_id)).all()
    if len(all_appts):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "orders": [appt.json() for appt in all_appts]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no appointments."
        }
    ), 404

## WIP ##
@app.route("/appointments/<string:appointment_id>", methods=['PUT'])
def update_order(appt_id):
    try:
        order = db.session.scalars(db.select(Appointment).filter_by(appointment_id=appt_id).limit(1)).first()
        if not order:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "order_id": appt_id
                    },
                    "message": "Order not found."
                }
            ), 404

        # update status
        data = request.get_json()
        if data['status']:
            order.status = data['status']
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": order.json()
                }
            ), 200
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "order_id": appt_id
                },
                "message": "An error occurred while updating the order. " + str(e)
            }
        ), 500


if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": manage appointments ...")
    app.run(host='0.0.0.0', port=5001, debug=True)
