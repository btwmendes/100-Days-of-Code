"""    This class is responsible for sending notifications with the deal flight details."""
from twilio.rest import Client
import os
import smtplib

TWILIO_SID = os.environ.get("TWILIO_ID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.environ.get("TWILIO_MOBILE")
TWILIO_VERIFIED_NUMBER = os.environ.get("MY_MOBILE")
GMAIL_PW = os.environ.get("GMAIL_PASS")


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, item):
        message = self.client.messages.create(
            body=item,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )
        print(message.sid)

    def send_emails(self, email, item, link):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login("nedflanders426@gmail.com", GMAIL_PW)
            connection.sendmail(from_addr="nedflanders426@gmail.com",
                                to_addrs=email,
                                msg=f"Subject:New Low Price Flight\n\n{item}\n{link}".encode('utf-8')
                                )

