# Autor uczący się: Jarosław Krefft
# Data utworzenia: 26.05.2026
# Nazwa i wersja programu: chat_bot_KB.py - propozycja Kamila
# prosta wersja programu która pozwala na rozmowe z modelem OPEN AI  - bez zapamietywania historii rozmowy

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def send_message(message):
    if message == 'quit':
        exit()

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=message
        

)

    print(response.output_text)

print('Zacznij rozmowe. Aby zakończyć rozmowe z chat GPT wpisz "quit".')
while True:
    send_message(input('Ty: '))


