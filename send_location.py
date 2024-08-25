import requests

def send_location(device_id, location):
    url = "http://your-backend-url/update_location"
    data = {
        'device_id': device_id,
        'location': location
    }
    response = requests.post(url, json=data)
    print(response.json())
