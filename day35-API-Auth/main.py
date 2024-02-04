from config import weather_api_key
import requests

lat ="-21.754530"
lon ="-41.324612"
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&cont=3&appid={weather_api_key}"

response = requests.get(url)
response.raise_for_status()
data = response.json()
print(data["weather"][0]["description"])