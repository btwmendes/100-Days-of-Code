"""This class is responsible for talking to the Flight Search API."""

# --------------------Imported Libraries----------------------
import requests
from pprint import pprint
from flight_data import FlightData
from datetime import datetime
import os

# --------------------Global Variables----------------------
API_KEY = os.environ.get("FLIGHT_SEARCH_API_KEY")
AIRPORT_CODE_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
HEADERS = {
    "apikey": API_KEY
}
FLIGHT_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"

# --------------------Flight Search Class----------------------
class FlightSearch:

    def get_destination_code(self, city_name):
        # code = "TESTING"
        airport_code_params = {
            "term": city_name,
            "location_types": "city"
            # "limit": 1
        }
        airport_response = requests.get(url=AIRPORT_CODE_ENDPOINT, params=airport_code_params, headers=HEADERS)
        data = airport_response.json()
        code = data["locations"][0]["code"]
        return code
# ---------------------------------
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),       # "27/11/2021"
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }


        response = requests.get(
            url=FLIGHT_ENDPOINT,
            params=query,
            headers=HEADERS)

        try:
            data = response.json()["data"][0]
            # print(f"{destination_city_code} {data['price']}")
            # pprint(data)
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            query["max_stopovers"] = 1
            response = requests.get(
                url=FLIGHT_ENDPOINT,
                params=query,
                headers=HEADERS)
            data = response.json()["data"][0]
            pprint(data)
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: ${flight_data.price}")
            return flight_data
