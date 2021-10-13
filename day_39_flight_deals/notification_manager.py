"""    This class is responsible for sending notifications with the deal flight details."""
from twilio.rest import Client
import os

TWILIO_SID = os.environ.get("TWILIO_ID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.environ.get("TWILIO_MOBILE")
TWILIO_VERIFIED_NUMBER = os.environ.get("MY_MOBILE")


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