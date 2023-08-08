from twilio.rest import Client  # Twilio is the API used to send SMS messages
from dotenv import load_dotenv
import requests
import os

# getting current quotation of all coins
quotes = requests.get('https://economia.awesomeapi.com.br/json/all')
quotes_dic = quotes.json()  # creates a quotation python dict using .json() method

dollar = quotes_dic["USD"]["bid"]
euro = quotes_dic["EUR"]["bid"]
peso = quotes_dic["ARS"]["bid"]

client = Client()

# getting phone number list registered in Twilio
outgoing_caller_ids = client.outgoing_caller_ids.list(limit=20)

# SMS message block
for record in outgoing_caller_ids:
    print('{}: {}'.format(record.friendly_name, record.phone_number))
    message = client.messages.create(
      from_="+13613155385",
      body=f'Hello, {record.friendly_name}!\n Dollar quotation: R$ {dollar} \n Euro quotation: R$ {euro} \n '
           f'Peso (ARG) quotation: R$ {peso}',
      to=record.phone_number
    )
    print(message.status)

