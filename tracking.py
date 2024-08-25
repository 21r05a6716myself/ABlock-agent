from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for simplicity
location_data = {}

@app.route('/update_location', methods=['POST'])
def update_location():
    data = request.json
    device_id = data['device_id']
    location = data['location']
    location_data[device_id] = location
    return jsonify({'status': 'success'})

@app.route('/get_location/<device_id>', methods=['GET'])
def get_location(device_id):
    location = location_data.get(device_id)
    if location:
        return jsonify({'location': location})
    return jsonify({'error': 'Device not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
