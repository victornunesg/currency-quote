from twilio.rest import Client
from dotenv import load_dotenv
import requests
import os

# pegando a cotação atual de todas as moedas
quotes = requests.get('https://economia.awesomeapi.com.br/json/all')
quotes_dic = quotes.json()  # cria um dicionário python para cotações usando o método .json()

dollar = quotes_dic["USD"]["bid"]
euro = quotes_dic["EUR"]["bid"]
peso = quotes_dic["ARS"]["bid"]

load_dotenv()  # loading environment variables to authenticate in Twilio

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

contacts = {
    "Victor": "+5561999350868",
    "ABR": "+5561992199483"
}

for name in contacts:
    print('{}: {}'.format(name, contacts[name]))
    message = client.messages.create(
      from_='+13613155385',
      body=f'Olá, {name}!\n Cotação do Dólar: R$ {dollar} \n Cotação do Euro: R$ {euro} \n '
           f'Cotação do Peso (Argentina): R$ {peso}',
      to=contacts[name]
    )

print(message.status)
