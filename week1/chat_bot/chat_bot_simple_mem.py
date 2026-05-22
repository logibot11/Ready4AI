# Autor uczący się: Jarosław Krefft
# Data utworzenia: 22.05.2026
# Nazwa i wersja programu: chat_bot_simple_mem.py
# prosta wersja programu która pozwala na rozmowe z modelem OPEN AI  - z zapamietywaniem historii rozmowy


from openai import OpenAI
from dotenv import load_dotenv
import os

# Załadowanie klucza OPEN AI
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Obsługa pamięci konwersacji
messages = [
    {
        "role": "system",
        "content": "Jesteś pomocnym chatbotem AI."
    }
]

print("=== CHATBOT AI ===")
print("Wpisz 'quit' aby zakończyć\n")

while True:

    user_input = input("Ty: ")

    if user_input.lower() == "quit":
        print("Koniec programu.")
        break

# Dodanie użytkownika - do konwersacji
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

   # Obsługa request
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )

    ai_response = response.choices[0].message.content

# Zapamiętanie historii konwersacji
    messages.append(
        {
            "role": "assistant",
            "content": ai_response
        }
    )

    print(f"\nAI: {ai_response}\n")
