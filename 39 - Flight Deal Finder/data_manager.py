import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    URL = "https://api.sheety.co/300863c9ad6b89ca8970c77aa0f4c3ae/chescore'sFlightDeals/prices"
    def __init__(self):
        pass

    def getSheetData(self):
        response = requests.get(self.URL)
        return response.json()

    def updateSheetData(self, id, body):
        response = requests.put(url=f'{self.URL}/{id}', json=body)
        return response.text
