import requests
import datetime


My_lat = -21.754530
My_lng = -41.324612

parameters = {
    "lat": My_lat,
    "lng": My_lng,
    "formatted": 0,
}
print(parameters)
response = requests.get("https://api.sunrise-sunset.org/json",parameters)
response.raise_for_status()
print(response)

data = response.json()
sunrise_unformatted = str(data["results"]["sunrise"])
sunset_unformatted =str(data["results"]["sunset"])
sunrise =sunrise_unformatted[11:16]


now= datetime.datetime.now()
hour = str(now.hour)+":"+str(now.minute)

print(hour)
print(sunrise)


