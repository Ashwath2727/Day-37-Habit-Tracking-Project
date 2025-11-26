import requests
import os
from pathlib import Path
from dotenv import load_dotenv
import datetime as dt

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

USERNAME = "ashwath3127"
TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = "graph1234"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# to create a new user
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

POST_PIXEL_ENDPOINT = GRAPH_ENDPOINT + f"/{GRAPH_ID}"

today = dt.datetime.now()


post_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "4.5"
}

response = requests.post(url=POST_PIXEL_ENDPOINT, json=post_pixel_config, headers=headers)
print(response.text)