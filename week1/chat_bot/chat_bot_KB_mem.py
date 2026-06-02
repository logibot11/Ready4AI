# Autor uczący się: Jarosław Krefft
# Data utworzenia: 26.05.2026
# Nazwa i wersja programu: chat_bot_KB.py - propozycja Kamila
# prosta wersja demonstracyjna  programu która pozwala na rozmowe z modelem OPEN AI  - tym razem z użyciem response_id


from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def send_message(message, previous_response_id=None):
    if message == 'quit':
        exit()

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=message,
        previous_response_id=previous_response_id
    )

    print(response.output_text)
    return response.id

print('Zacznij rozmowe. Aby zakończyć rozmowe z chat GPT wpisz "quit".')

response_id = None

while True:
    response_id = send_message(input('Ty: '), response_id)


