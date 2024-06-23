import os
import datetime
import requests

today = datetime.datetime.now()

class FlightData:
    #This class is responsible for structuring the flight data.
    URL = 'https://api.tequila.kiwi.com/v2/search'

    def __init__(self, city):
        self.params = {
            "fly_from": "LON",
            "fly_to": city,
            "date_from": today.strftime("%d/%m/%Y"),
            "date_to": (today + datetime.timedelta(days=180)).strftime("%d/%m/%Y"),
            "return_from": (today + datetime.timedelta(days=7)).strftime("%d/%m/%Y"),
            "return_to": (today + datetime.timedelta(days=28)).strftime("%d/%m/%Y"),
            "curr": "GBP"
        }
        self.headers = {
            "apikey": os.environ.get("APIKEY")
        }

    def getFlightData(self):
        response = requests.get(url=self.URL, params=self.params, headers=self.headers)
        return response.json()['data'][0]