import requests

URL = "http://raspberrypi:5000/gpio/7/state"

response = requests.put(URL, {"state": 1})
#response = requests.get(URL)


print(response)
print(response.text)
print(response.json())
