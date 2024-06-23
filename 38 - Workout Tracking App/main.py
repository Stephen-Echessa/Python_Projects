import requests
from datetime import datetime
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
BASIC_TOKEN = os.environ.get("BASIC_TOKEN")
nutritionix_endpoint = os.environ.get("NUTRITIONIX_ENDPOINT")
sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")


today = datetime.now()

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

params = {
    "query": input("Tell me which exercises you did: ")
}

nutritionix_response = requests.post(url=nutritionix_endpoint, json=params, headers=headers)
exercise_response = nutritionix_response.json()["exercises"]

sheety_headers = {
    "Authorization": BASIC_TOKEN
}

for exercise in exercise_response:
    print(exercise)

    sheety_params = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(url=sheety_endpoint, json=sheety_params, headers=sheety_headers)
    print(sheety_response.json())
