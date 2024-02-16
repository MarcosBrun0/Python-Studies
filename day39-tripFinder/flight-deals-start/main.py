#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


pprint.pprint(sheet_data)


for city in sheet_data['prices']:


    new_data ={
        'price': {'iataCode': city['iataCode']}
    }
    sheety_response = requests.put(f"{sheety_url}/{city['id']}",json=new_data)
    sheety_response.raise_for_status()