# Autor uczący się: Jarosław Krefft
# Data utworzenia: 22.05.2026
# Nazwa i wersja programu: chat_bot_simple_no_mem.py
# prosta wersja programu która pozwala na rozmowe z modelem OPEN AI  - bez zapamietywania historii rozmowy

from openai import OpenAI
from dotenv import load_dotenv
import os

# załadowanie klucza API
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

print("Bot Sony")
print("Jeżeli chcesz zakończyć wpisz 'quit'\n")

while True:

    user_input = input("Ty: ")

    if user_input.lower() == "quit":
        print("Żegnaj")
        break

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    ai_response = response.choices[0].message.content

    print(f"\nAI: {ai_response}\n")