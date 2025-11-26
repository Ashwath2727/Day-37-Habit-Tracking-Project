import requests
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

USERNAME = "ashwath3127"
TOKEN = os.getenv("PIXELA_TOKEN")

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