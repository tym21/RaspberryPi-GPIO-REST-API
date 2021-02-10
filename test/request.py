import requests

URL = "http://raspberrypi:5000/gpio/2/state"

response = requests.put(URL, {"state": 0})
# response = requests.get(URL)

print(response)
print(response.json())
