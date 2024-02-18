import requests,config,datetime

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_API_KEY = config.tequila_api



headers = {
    'apikey': TEQUILA_API_KEY
}

class FlightSearch:

    def __init__(self):
        self.data = None

    def search_for_flight(self,citycode):
        tomorrowdate = datetime.datetime.now() + datetime.timedelta(hours=24)
        sixmonthslater = datetime.datetime.now() + datetime.timedelta(days=(30 * 6))
        tomorrowdate = str(datetime.datetime.strftime(tomorrowdate,"%d/%m/%Y"))
        sixmonthslater = str(datetime.datetime.strftime(sixmonthslater,"%d/%m/%Y"))
        query = {
            "fly_from": "LON",
            "fly_to": citycode,
            "date_from": tomorrowdate,
            "date_to": sixmonthslater,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        print(citycode,tomorrowdate,sixmonthslater)
        tequila_request = requests.get(url=f"https://api.tequila.kiwi.com/v2/search",headers=headers, params=query)
        tequila_request.raise_for_status()
        data = tequila_request.json()
        print(data)
        return data
    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.

        tequila_request = requests.get(url=f"{TEQUILA_ENDPOINT}?term={city_name}",headers=headers)
        tequila_request.raise_for_status()
        data = tequila_request.json()
        code = data['locations'][0]['code']
        return code
