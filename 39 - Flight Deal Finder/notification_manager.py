import vonage
import os

client = vonage.Client(key=os.environ.get("VONAGE_KEY"), secret=os.environ.get("VONAGE_SECRET"))
sms = vonage.Sms(client)

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass

    def sendSms(self, price, city_from, city_from_code, city_to, city_to_code, date_from, date_to):
        responseData = sms.send_message({
            "from": "Vonage APIs",
            "to": "254759694831",
            "text": f"Low price alert! Only €{price} to fly from"
                    f"{city_from}-{city_from_code} to {city_to}-{city_to_code},"
                    f"from {date_from.split('T')[0]} to {date_to.split('T')[0]}."
        })

        if responseData["messages"][0]["status"] == "0":
            print("Message sent successfully.")
        else:
            print(f"Message failed with error: {responseData['messages'][0]['error-text']}")