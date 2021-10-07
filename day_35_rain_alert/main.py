# https://openweathermap.org/api
import requests
from twilio.rest import Client

api_key = "9f00eb6100a05d1257ec6c7a8539adc1"
latitude = 30.158813
longitude = -85.660210

account_sid = "ACde902588753db3c01b4ed27c002f3ec4"
auth_token = "0992f5f9de1929fe506446dddd073ae9"

# Walnut Creek lat and long
# latitude = 37.901760
# longitude = -122.061920

parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
# https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
# print(response.status_code)
# print()
response.raise_for_status()
data = response.json()

twelve_days = data["hourly"][0:12]

will_rain = False

for day in twelve_days:
    weather_code = day['weather'][0]['id']
    if int(weather_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_='+16364668733',
        to='+19253307691'
    )
    print(message.status)