import requests
import config

api_id = config.nutritionix_id
api_key = config.nutritionix_api

header = {
'x-app-key': api_key,
'x-app-id': api_id  ,
}

params = {
    'query': "leg workout 60 minutes",
    'gender': "male",
    'weight_kg': 72,
    'height_cm': 183,
    'age': 21
}

url = "https://trackapi.nutritionix.com/v2/natural/exercise"
response = requests.post(url=url,json=params,headers=header)
response.raise_for_status()
data = response.json()
print(data)


