
# Autor uczący się: Jarosław Krefft
# Data utworzenia: 18.05.2026
# Nazwa i wersja programu: chat_bot_1A.py
# 1 - sza wersja kodu chat-bota który nie posiada mechanizmu historii rozmowy z chat-botem poza tym jest stosowane bezpieczne umieszczenie klucza OPEN_AI KEY z pliku .env 

from dotenv import load_dotenv
import os

# wczytanie zmiennych z pliku .env
load_dotenv()

# pobranie klucza API
api_key = os.getenv("OPENAI_API_KEY")

# inicjalizacja klienta
client = OpenAI(api_key=api_key)

print("Chatbot uruchomiony.")
print("Wpisz 'quit' aby zakończyć.\n")

while True:
    user_input = input("Ty: ")

    if user_input.lower() == "quit":
        print("Koniec programu.")
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

    print(f"AI: {ai_response}\n")