#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# pprint(sheet_data)
# print()

flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "OAK"

if sheet_data[0]["iatacodes"] == "":
    for row in sheet_data:
        row["iatacodes"] = flight_search.get_destination_code(row["city"])
    pprint(f"sheet_data:\n {sheet_data}")
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6*30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iatacodes"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )
    try:
        if flight.price < destination["lowestprice"]:
            # print(f"Low price alert: {flight.price}")
            notification_manager.send_sms(
                item=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
            )

    except AttributeError:
        print("There is no direct flight")

