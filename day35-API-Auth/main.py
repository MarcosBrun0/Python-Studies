from config import weather_api_key,email,password
import requests, smtplib

lat ="-21.754530"
lon ="-41.324612"
cont = 3
url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&cnt={cont}&appid={weather_api_key}"

response = requests.get(url)
response.raise_for_status()
data = response.json()
id_code=[]
for time in range(0,3):
     id_code.append(data["list"][time]["weather"][0]["id"])

feels_like_data = data["list"][0]["main"]["feels_like"]
descriptiom = data["list"][0]["weather"][0]["description"]

Celsius_feelslike = int(feels_like_data) -273.15
will_rain = False


for id in id_code:
    if int(id)<700:
        will_rain = True


if will_rain:

    with smtplib.SMTP("smtp.gmail.com") as conection:
        conection.starttls()
        conection.login(user=email,password=password)
        conection.sendmail(from_addr=email,to_addrs="mbrunocampos20@gmail.com", msg=f"Subject:Its gonna Rain today\n\n will be {descriptiom}, with the temperature feels of {feels_like_data} ")
