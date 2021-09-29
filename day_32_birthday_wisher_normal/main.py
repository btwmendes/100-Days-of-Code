
import datetime as dt
import pandas as pd
import random
import smtplib

now = dt.datetime.now()
today = (now.month, now.day)
# print(today)

data = pd.read_csv("./birthdays.csv")
# print(data)

birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}
# print(birthdays_dict)

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    num = random.randint(1,3)
    file = f"./letter_templates/letter_{num}.txt"
    with open(file) as letter_file:
        letter = letter_file.read()
        letter = letter.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login("nedflanders426@gmail.com", "kuhsfpkpvlqfrpvw")
        connection.sendmail(from_addr="nedflanders426@gmail.com",
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{letter}"
                            )
