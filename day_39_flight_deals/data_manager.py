"""This file is responsible for talking to the Google Sheet"""

# --------------------Imported Libraries----------------------
import requests
from pprint import pprint
import os

# --------------------Global Variables----------------------
SHEET_ENDPOINT = "https://api.sheety.co/08e59ed6f95edc2c406f133d0a7bc7e4/flightDeals/prices"
SHEET_HEADER = {
    "Authorization": f"Basic {os.environ.get('SHEETY_TOKEN')}"
}

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheet_response = requests.get(url=SHEET_ENDPOINT, headers=SHEET_HEADER)
        sheet_data = sheet_response.json()
        self.destination_data = sheet_data["prices"]
        return self.destination_data

        # self.price_data = [row["lowestprice"] for row in sheet_data["prices"]]

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iatacodes": city["iatacodes"]
                }
            }
            response = requests.put(
                url=f"{SHEET_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=SHEET_HEADER)
            pprint(response.text)