import requests, pprint
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.sheety_url = "https://api.sheety.co/1ffd929df22e32b9c0d35457dd58501c/flightDeals/prices"

        self.sheety_response = requests.get(self.sheety_url)
        self.sheety_response.raise_for_status()
        self.sheet_data = self.sheety_response.json()
        pprint.pprint(sheet_data)
        for city in sheet_data['prices']:
            city['iataCode'] = "Testing"