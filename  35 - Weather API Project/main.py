import requests
import os
from twilio.rest import Client

MY_LAT = 0.416198
MY_LONG = 9.467268

API_KEY = os.environ.get("API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

parameters = {
    "lat":MY_LAT,
    "lon":MY_LONG,
    "appid":API_KEY
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
json_weather_list = weather_data["list"][:13]

id_list = [weather["weather"][0]["id"] for weather in json_weather_list]

message_body = ""

for id in id_list:
    if id < 700:
        message_body = "Bring an Umbrella"
    else:
        message_body = "You're good to go"

message = client.messages.create(
    body=message_body,
    from_='+19295773684',
    to='+254745449346'
)   

print(message.status)
