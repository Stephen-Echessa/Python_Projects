import requests
from datetime import datetime

TOKEN = "hrtrtrtr234433445"
USERNAME = "stephenechessa"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

today = datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometres did you cycle today?"),
}

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"


response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

pixel_update_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

pixel_update_params = {
    "quantity": "8.5"
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_params, headers=headers)
# print(response.text)

pixel_delete_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)



