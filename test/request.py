import requests

BASE = "http://127.0.0.1:5000/"
BASE = "http://192.168.178.31:5000"

#response = requests.put(BASE + "/gpio/16/status", {"status": 29})
response = requests.get(BASE + "/gpio/16/status")

print(response)
print(response.json())
