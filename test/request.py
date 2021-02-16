import requests
import time

URL = "http://raspberrypi:5000/gpio/2/state"

#response = requests.put(URL, {"state": 0})
# response = requests.get(URL)

#print(response)
#print(response.json())


for i in range(10):
    state = 1 if i % 2 == 0 else 0
    response = requests.put(URL, {"state": state})
    print(response.json())
    time.sleep(0.2)