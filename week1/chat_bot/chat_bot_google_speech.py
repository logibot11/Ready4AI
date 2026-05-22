# Autor uczący się: Jarosław Krefft
# Data utworzenia: 22.05.2026
# Nazwa i wersja programu: basic_get_1A.py
# program pozwala na rozmowe (rozpoznaje mowę) z modelem OPEN AI  - bez zapamietywania historii rozmowy
# program poza tym mechanizm zatrzymania nasłuchiwania dźwięków audio jeżeli nikt nic nie mówi.

from openai import OpenAI
import speech_recognition as sr
from dotenv import load_dotenv
import os

# ------------------------------------------------------------
# załadowanie klucza z pliku .env
# ------------------------------------------------------------
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("Brak OPENAI_API_KEY w pliku .env")

client = OpenAI(api_key=api_key)

# ------------------------------------------------------------
# Speech Recognition
# ------------------------------------------------------------
recognizer = sr.Recognizer()

print("========================================")
print("ENGIBO Voice Assistant (NO WAKE WORD)")
print("Powiedz komendę bez słowa aktywującego")
print("Powiedz 'quit' aby zakończyć")
print("========================================\n")

while True:

    try:
        with sr.Microphone() as source:

            print("Nasłuchiwanie...")

            # stabilizacja mikrofonu
            recognizer.adjust_for_ambient_noise(source, duration=2)

            # nagrywanie wypowiedzi
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

        # ----------------------------------------------------
        # Speech to text
        # ----------------------------------------------------
        text = recognizer.recognize_google(audio, language="pl-PL")

        text_lower = text.lower()

        # debug
        print(f"Rozpoznano: {text_lower}")

        # ----------------------------------------------------
        # exit command
        # ----------------------------------------------------
        if "quit" in text_lower:
            print("Koniec programu.")
            break

        # ----------------------------------------------------
        # bez wake word → cała wypowiedź to komenda
        # ----------------------------------------------------
        command = text_lower.strip()

        if not command:
            print("Pusta komenda\n")
            continue

        # ----------------------------------------------------
        # OpenAI request
        # ----------------------------------------------------
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Jesteś pomocnym asystentem głosowym."
                },
                {
                    "role": "user",
                    "content": command
                }
            ]
        )

        ai_response = response.choices[0].message.content

        print("\nAI:")
        print(ai_response)
        print("\n")

    except sr.WaitTimeoutError:
        print("Brak wypowiedzi (timeout)\n")

    except sr.UnknownValueError:
        print("Nie rozpoznano mowy\n")

    except sr.RequestError as e:
        print(f"Błąd STT: {e}\n")

    except Exception as e:
        print(f"Błąd: {e}\n")