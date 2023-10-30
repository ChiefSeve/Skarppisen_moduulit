import requests
import json

api_key = "2530563768b2b3b4e2f68a1fb113cc1f"
lat = 10
lon = 120

call = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
result = requests.get(call).json()
print(json.dumps(result, indent=2))
