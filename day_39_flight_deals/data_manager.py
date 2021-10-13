import requests
from pprint import pprint

sheet_endpoint = "https://api.sheety.co/08e59ed6f95edc2c406f133d0a7bc7e4/flightDeals/prices"
sheet_header = {
    "Authorization": "Basic YnR3bWVuZGVzOlNwcmluZ2ZpZWxkMTch"
}

city = "Los Angeles"
airport_code = "lax"
price = 205.03

# for flight in flights:
sheet_inputs = {
    "price": {
        "city": city,
        "iatacodes": airport_code,
        "lowestprice": price
    }
}

# response = requests.get(url=sheet_endpoint, headers=sheet_header)
# data = response.json()
# pprint(data)

sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, headers=sheet_header)
print(sheet_response.text)


# class DataManager:
#     #This class is responsible for talking to the Google Sheet.
#     pass