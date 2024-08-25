import requests
import os

def check_subscription(device_id):
    url = f"http://your-backend-url/check_subscription/{device_id}"
    response = requests.get(url)
    data = response.json()
    if data.get('status') == 'expired':
        crash_system()

def crash_system():
    os.system("shutdown -h now")

# Simulate periodic subscription check
check_subscription('device123')
