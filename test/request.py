import requests

BASE = "http://raspberrypi:5000/"

response = requests.put(BASE + "/gpio/28/status", {"status": 1})

print(response)
print(response.json())
