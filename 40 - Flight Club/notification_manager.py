import vonage
import os
import smtplib

client = vonage.Client(key=os.environ.get("VONAGE_KEY"), secret=os.environ.get("VONAGE_SECRET"))
sms = vonage.Sms(client)
MY_EMAIL="chescore81194@gmail.com"
EMAIL_PASSWORD="sddfjksasjeuajgt"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
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

    def sendSmsWithStopOvers(self, price, city_from, city_from_code, city_to, city_to_code, date_from, date_to, stop_over_1, stop_over_2):
        responseData = sms.send_message({
            "from": "Vonage APIs",
            "to": "254759694831",
            "text": f"Low price alert! Only €{price} to fly from"
                    f"{city_from}-{city_from_code} to {city_to}-{city_to_code},"
                    f"from {date_from.split('T')[0]} to {date_to.split('T')[0]}.\n\n"
                    f"Flight has 2 stop overs, via {stop_over_1} and {stop_over_2}"
        })

        if responseData["messages"][0]["status"] == "0":
            print("Message sent successfully.")
        else:
            print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
    
    def sendEmails(self,email_address, price, city_from, city_from_code, city_to, city_to_code, date_from, date_to):
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
            to_addrs=email_address,
            msg=f"Subject: New Flight Prices\n\n"
                f"Low price alert! Only £{price} to fly from"
                f"{city_from}-{city_from_code} to {city_to}-{city_to_code},"
                f"from {date_from.split('T')[0]} to {date_to.split('T')[0]}.\n\n"
                f"https://www.google.co.uk/flights?hl=en#flt={city_from_code}.{city_to_code}.{date_from.split('T')[0]}*{city_from_code}.{city_to_code}.{date_to.split('T')[0]}".encode('utf-8'))

