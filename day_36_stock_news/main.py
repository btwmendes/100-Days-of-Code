import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# -----------------------------Stock Information-------------------------
stock_api_key = "J3GZI3FUZKZNAO2N"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": stock_api_key
}

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
# print(stock_response.status_code)
stock_response.raise_for_status()
stock_data = stock_response.json()

daily_price_dict = stock_data["Time Series (Daily)"]
# print(daily_price_dict)

yesterday_date = list(daily_price_dict.keys())[0]
# print(yesterday_date)

price_list = [value['4. close'] for (key, value) in daily_price_dict.items()]
# print(price_list)

yesterday_price = float(price_list[0])
day_before_yesterday = float(price_list[1])
# print(yesterday_price, day_before_yesterday)

dollar_differance = abs(yesterday_price - day_before_yesterday)
# print(dollar_differance)

percentage_change = dollar_differance / day_before_yesterday * 100
# print(percentage_change)

# -----------------------------News Information-------------------------
news_api_key = "b055b0797a6c4fe0a0841c1c0a598957"

news_parameters = {
    "apiKey": news_api_key,
    "q": COMPANY_NAME,
    "from": f"{yesterday_date}" + "T00:00:00",
    "language": "en",
    "sortBy": "popularity"
}

news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
# print(news_response.status_code)
news_response.raise_for_status()
news_data = news_response.json()
# print(news_data)

first_three_articles = news_data['articles'][:3]
# print(first_three_articles)
# print()

# -----------------------------Twilio Text-------------------------
news_list = ["Headline: " + story['title'] + "\nBrief: " + story['description'] for story in first_three_articles]
# print(news_list[0])

if yesterday_price > day_before_yesterday:
    percentage_change_message = f"🔺{round(percentage_change)}%"
else:
    percentage_change_message = f"🔻{round(percentage_change)}%"
# print(percentage_change_message)

account_sid = "ACde902588753db3c01b4ed27c002f3ec4"
auth_token = "0992f5f9de1929fe506446dddd073ae9"

if percentage_change >= 5.0:
    for story in news_list:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"{STOCK_NAME}: {percentage_change_message}\n{story}",
            from_='+16364668733',
            to='+19253307691'
        )
        print(message.status)
