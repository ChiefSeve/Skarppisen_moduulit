import json
import requests

pyyntö = "https://api.chucknorris.io/jokes/random"
tulos = requests.get(pyyntö).json()
print(tulos["value"])
