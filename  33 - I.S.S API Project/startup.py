import requests

MY_LAT = -1.292066
MY_LONG = 36.821945

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "formatted": 0
}

response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise_hour = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_hour = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise, sunset)
print(sunrise_hour, sunset_hour)
