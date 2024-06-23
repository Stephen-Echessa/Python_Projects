import os
import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    URL = 'https://api.tequila.kiwi.com/locations/query'

    def __init__(self, city) -> None:
        self.params = {
            "term": city,
            "location_types":"city"
        }
        self.headers = {
            "apikey": os.environ.get("APIKEY")
        }
    
    def getIATACode(self):
        response = requests.get(url=self.URL, params=self.params, headers=self.headers)
        return response.json()
