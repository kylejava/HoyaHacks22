import requests
from keys import *
import json
from api import *
from twilio.rest import Client
from User import *

client = Client(twilio_account_sid, twilio_auth_token)


def sendMessage(user):
    horoscope = getHoroscope(user.sign, 'today')

    message = client.messages \
                    .create(
                         body="Hello " + user.name + "!!! Welcome to ScopeMobile, get your horoscope through your phone!!! Here is today's horoscope: " + horoscope['description'],
                         from_='+17853775708',
                         to='+1'+str(user.phone_number)
                     )

    print(message.sid)
