#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "OAK"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()
# pprint(sheet_data)
# print()

if sheet_data[0]["iatacodes"] == "":
    for row in sheet_data:
        row["iatacodes"] = flight_search.get_destination_code(row["city"])
    pprint(f"sheet_data:\n {sheet_data}")
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

destinations = {
    data["iatacodes"]: {
        "id": data["id"],
        "city": data["city"],
        "price": data["lowestprice"]
    } for data in sheet_data}

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6*30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iatacodes"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )
    if flight is None:
        continue

    if flight.price < destinations[destination]["price"]:

        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstname"] for row in users]

        # print(f"Low price alert: {flight.price}")
        item=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.origin_airport}.{flight.destination_airport}.{flight.return_date}"

        if flight.stop_overs > 0:
            item += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            print(item)

        notification_manager.send_sms(item)
        notification_manager.send_emails(emails, item, link)

# except AttributeError:
#     print("There is no direct flight")

