import requests

URL = "http://raspberrypi:5000/gpio/1/state"

response = requests.put(URL, {"state": 0})
#response = requests.get(URL)


print(response)
print(response.text)
print(response.json())
