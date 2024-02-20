import requests
import Config
import datetime

def exercise_api():

    api_id = config.nutritionix_id
    api_key = config.nutritionix_api
    inputtext = input("Qual exercicio voce fez hoje?")

    header = {
    'x-app-key': api_key,
    'x-app-id': api_id,
    }
    params = {
        'query': inputtext,
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
    return data


def today_date():
    date = datetime.date.today()
    date2 = str(datetime.datetime.strftime(date,"%d/%m/%y"))
    return date2


def hour_now():
    now = datetime.datetime.now()
    hour = str(now.strftime("%H:%M:%S"))
    return hour
#{'exercises': [{'tag_id': 843, 'user_input': 'chest', 'duration_min': 1.67, 'met': 3.5, 'nf_calories': 7.01, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/843_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/843_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 2054, 'name': 'chest press', 'description': None, 'benefits': None}]}

now_time = 0
sheet_endpoint = "https://api.sheety.co/1ffd929df22e32b9c0d35457dd58501c/myWorkouts/workouts"

result = exercise_api()

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date(),
            "time": hour_now(),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)

    print(sheet_inputs)


    #