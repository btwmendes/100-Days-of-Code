import requests
from bs4 import BeautifulSoup
import smtplib

# ---------------------------Set Environment Variables---------------------------
"""Environment Variable Help --> https://stackoverflow.com/questions/42708389/how-to-set-environment-variables-in-pycharm"""
import os
# print(os.environ['YAHOO_PASSWORD'])

# ---------------------------Webscraping---------------------------
URL = "https://www.amazon.com/All-new-Sonos-One-Controlled-Speaker/dp/B079BG3M7D/ref=sr_1_4?crid=IPZ4SPUJ3U3R&dchild=1&keywords=sonos&qid=1635283538&sprefix=sonos%2Caps%2C264&sr=8-4"

accept_language = "en-us"
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15"

headers = {
    "Accept-Language": accept_language,
    "User-Agent": user_agent
}

response = requests.get(URL, headers=headers)
amazon = response.text
# print(amazon)

soup = BeautifulSoup(amazon, "lxml")

# print(soup.prettify())

price = soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString").getText()
price_as_float = float(price.split("$")[1])
print(price_as_float)

# ---------------------------Send Email---------------------------
flanders_gmail = "nedflanders426@gmail.com"
yahoo_password = os.environ['YAHOO_PASSWORD']
homer_yahoo = "simpsonhomer36@yahoo.com"

# gmail = "smtp.gmail.com"
# hotmail = "smtp.live.com"
yahoo = "smtp.mail.yahoo.com"

message = f"Two Room Set with All-New Sonos One is now {price_as_float}."

if price_as_float <= 550:
    with smtplib.SMTP(yahoo, port=587) as connection:
        connection.starttls()
        connection.login(user=homer_yahoo, password=yahoo_password)
        connection.sendmail(from_addr=homer_yahoo,
                            to_addrs=flanders_gmail,
                            msg=f"Subject:Sonos Price Tracker\n\n{message}\n{URL}")
