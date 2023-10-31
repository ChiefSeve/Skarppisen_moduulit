import requests
import json

api_key = 'foobar'
city_name = input('Anna nimi: ')
units = 'metric'

call = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units={units}'
result = requests.get(call).json()
weather_main = result['main']
weather_status = result['weather'][0]
print(f'{weather_status["description"]}, {weather_main["temp"]} Celsius')
