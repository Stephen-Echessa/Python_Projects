from json import JSONDecodeError
from data_manager import DataManager
from data_manager import DataManager
from pprint import pprint
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()

print("Welcome to Chescore's Flight Club.")
print("We find the best flight deals and email you.")

firstname = input("What is your first name?\n")
lastname = input("What is your lastname?\n")
email = input("What is your email?\n")
email_confirmation = input("Type your email again.\n")
if email_confirmation == email:
    print("You're in the club!")
    body = {
        "user": {
            "firstName": firstname,
            "lastName": lastname,
            "email": email
        }
    }
    data_manager.postToSheetData(body)

    data = data_manager.getSheetData()
    sheet_data = [value for value in data["prices"]]

    for obj in sheet_data:
        try:
            flight_data = FlightData(obj["iataCode"], stop_overs=0)
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
                notication_manager.sendEmails(email, price_result, city_from, city_from_code, city_to, city_to_code, date_from, date_to)
            else:
                print(f"Price to travel to {obj['city']} is higher")

        except(IndexError):
            print(f"There is currently no route to reach {obj['city']} through direct flight means")
            flight_data = FlightData(obj["iataCode"], stop_overs=2)
            results = flight_data.getFlightData()
            stops = results['route']
            price_result = results['price']
            city_from = results['cityFrom']
            city_from_code = results['cityCodeFrom']
            city_to = results['cityTo']
            city_to_code = results['cityCodeTo']
            date_from = results['local_departure']
            date_to = results['local_arrival']

            print(f'{obj["city"]}: €{price_result}')

            # if(price_result < obj["lowestPrice"]):
            #     notication_manager = NotificationManager()
            #     notication_manager.sendSmsWithStopOvers(price_result, city_from, city_from_code, city_to, city_to_code, date_from, date_to, stops[0]['cityTo'], stops[1]['cityTo'])
            # else:
            #     print(f"Price to travel to {obj['city']} is higher")