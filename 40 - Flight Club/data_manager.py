from urllib import response
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    URL = "https://api.sheety.co/300863c9ad6b89ca8970c77aa0f4c3ae/chescore'sFlightDeals"
    def __init__(self):
        pass

    def getSheetData(self):
        response = requests.get(url=f'{self.URL}/prices')
        return response.json()

    def postToSheetData(self, body):
        response = requests.post(url=f'{self.URL}/users', json=body)
        return response.text
