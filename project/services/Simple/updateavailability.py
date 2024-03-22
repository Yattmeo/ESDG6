from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data
availability_data = {
    'item1': True,
    'item2': False,
    'item3': True
}

@app.route('/update_availability', methods=['POST'])
def update_availability():
    data = request.get_json()
    for item, availability in data.items():
        if item in availability_data:
            availability_data[item] = availability
        else:
            return jsonify({'error': f'Item {item} not found'}), 404
    return jsonify({'message': 'Availability updated successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)