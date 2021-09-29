import smtplib

# my_email = "nedflanders426@gmail.com"
# password = "kuhsfpkpvlqfrpvw"
# web_password = "Springfield17!"
# test_email = "simpsonhomer36@yahoo.com"
#
# # gmail = smtp.gmail.com
# # hotmail = smtp.live.com
# # yahoo = smtp.mail.yahoo.com
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=test_email,
#                         msg="Subject:Hello Friend\n\nHi Diddily Ho Neighbor!")


import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.minute
print(month)
# if year == 2021:
#     print("Wear a face mask.")
print(year)

date_of_birth = dt.datetime(year=1887, month=12, day=27, hour=4)
print(date_of_birth)