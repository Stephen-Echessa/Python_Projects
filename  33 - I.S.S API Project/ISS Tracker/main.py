import requests
from datetime import datetime
import smtplib
import time
import os

my_email = os.environ.get("EMAIL")
my_password = os.environ.get("PASSWORD")

MY_LAT = -1.292066  # Your latitude
MY_LONG = 36.821945  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
print(iss_latitude, iss_longitude)


# Your position is within +5 or -5 degrees of the ISS position.
def is_overhead(lat, long):
    lat_upper = int(lat+5)
    lat_lower = int(lat-5)
    long_upper = int(long+5)
    long_lower = int(long-5)

    if int(iss_latitude) in range(lat_lower, lat_upper) and int(iss_longitude) in range(long_lower, long_upper):
        return True
    else:
        return False


def is_dark(time):
    new_sunrise = sunrise + 24
    print(new_sunrise)
    print(sunset)
    if sunset < time < new_sunrise:
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

print(is_dark(time_now.hour))
while True:
    time.sleep(60)
    if is_overhead(MY_LAT, MY_LONG) and is_dark(time_now.hour):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="chescore81194@yahoo.com",
                                msg="Subject:LOOK UP!\n\nIts about to pass")
