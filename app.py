from twilio.rest import Client  # Twilio is the API used to send SMS messages
import requests

# getting current quotation of all coins
quotes = requests.get('https://economia.awesomeapi.com.br/last/BRL-CLP,BRL-ARS,USD-BRL,EUR-BRL')
quotes_dic = quotes.json()  # creates a quotation python dict using .json() method

peso_chi = quotes_dic["BRLCLP"]["bid"]
peso_arg = quotes_dic["BRLARS"]["bid"]
dollar = quotes_dic["USDBRL"]["bid"]
euro = quotes_dic["EURBRL"]["bid"]

peso_chi_name = quotes_dic["BRLCLP"]["name"]
peso_arg_name = quotes_dic["BRLARS"]["name"]
dollar_name = quotes_dic["USDBRL"]["name"]
euro_name = quotes_dic["EURBRL"]["name"]

client = Client("ACbade097588007374e1839cb7e55aefc0", "95b2c09867501d18e792eb91fb15af4e")

# getting phone number list registered in Twilio
outgoing_caller_ids = client.outgoing_caller_ids.list(limit=20)

# SMS message block
for record in outgoing_caller_ids:
    print('{}: {}'.format(record.friendly_name, record.phone_number))
    message = client.messages.create(
      from_="+13613155385",
      body=f'Hello, {record.friendly_name}!\n {dollar_name}: R$ {dollar} \n {euro_name}: R$ {euro} \n '
           f'{peso_arg_name}: {peso_arg} pesos \n {peso_chi_name}: {peso_chi} pesos',
      to=record.phone_number
    )
    print(message.status)

