#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
data = data_manager.getSheetData()
print(data)
sheet_data = [value for value in data["prices"]]

for obj in sheet_data:
    flight_search = FlightSearch(obj["city"])
    flight_obj = flight_search.getIATACode()

    for values in flight_obj["locations"]:
        if values["name"] == obj["city"] and values['code'] != None:
            obj["iataCode"] = values['code']

    body = {
        "price": {
            "iataCode": obj["iataCode"]
        }
    }
    id = obj["id"]

    data_manager.updateSheetData(id=id, body=body)
    
    flight_data = FlightData(obj["iataCode"])
    results = flight_data.getFlightData()
    price_result = results['price']
    city_from = results['cityFrom']
    city_from_code = results['cityCodeFrom']
    city_to = results['cityTo']
    city_to_code = results['cityCodeTo']
    date_from = results['local_departure']
    date_to = results['local_arrival']

    print(f'{obj["city"]}: €{price_result}')

    if(price_result < obj["lowestPrice"]):
        notication_manager = NotificationManager()
        notication_manager.sendSms(price_result, city_from, city_from_code, city_to, city_to_code, date_from, date_to)
    else:
        print(f"Price to travel to {obj['city']} is higher")