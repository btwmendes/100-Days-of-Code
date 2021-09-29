# ---------------------------Imports---------------------------
import smtplib
import datetime as dt
import random
# ---------------------------Find today's date---------------------------
now = dt.datetime.now()
day_of_week = now.weekday()
# print(day_of_week)

# ---------------------------Pull in the quotes---------------------------
with open("./quotes.txt") as quotes:
    text = quotes.readlines()
    # print(text)

# ---------------------------Random Quote---------------------------
quote = random.choice(text)
# print(quote)

# ---------------------------Send Email---------------------------
flanders_gmail = "nedflanders426@gmail.com"
gmail_password = "kuhsfpkpvlqfrpvw"
yahoo_password = "qqbsvobzyrlmpogv"
web_password = "Springfield17!"
homer_yahoo = "simpsonhomer36@yahoo.com"

gmail = "smtp.gmail.com"
hotmail = "smtp.live.com"
yahoo = "smtp.mail.yahoo.com"

if day_of_week == 0:
    with smtplib.SMTP(yahoo, port=587) as connection:
        connection.starttls()
        connection.login(user=homer_yahoo, password=yahoo_password)
        connection.sendmail(from_addr=homer_yahoo,
                            to_addrs=flanders_gmail,
                            msg=f"Subject:Monday Motivational Quote\n\n{quote}")
else:
    print("Today is not Monday")
