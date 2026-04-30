# Autor uczący się: Jarosław Krefft
# Data utworzenia: 30.04.2026
# Nazwa i wersja programu: basic_get_1B.py
# Dane przykładowe API pobierane z: https://jsonplaceholder.typicode.com/
# 2 - ga wersja kodu która wykonuje poniższe zadania: prezentacja liczby rekordów
#                                                     pobranie pierwszego określonego rekordu
#                                                     pobranie 5 pierwszysch rekordów
# Info: Druga wersja kodu powstała po burzliwych naradach z Chat GPT ;)

import requests
from colorama import Fore, Style, init

def get_json(url):
    response = requests.get(url)

    if response.ok:
        return response.json()
    else:
        print("Błąd:", response.status_code)
        return None


url = "https://jsonplaceholder.typicode.com/posts"

data = get_json(url)

print("\nStart ..... \n")

if data:

    # 1. prezentacja liczby rekordów
    #print(Fore.YELLOW +"1. Liczba rekordów:", len(data))
    print(f"{Fore.YELLOW} Informacja o danych. Ilość rekordów: {len(data)}{Style.RESET_ALL}")

    # 2. pierwszy rekord
    first_record = data[0]
    print("\n1. Pierwszy rekord:")
    print("ID:", first_record["id"])
    print("Tytuł:", first_record["title"])
    print("Treść:", first_record["body"])

    # 3. pierwsze 5 rekordów
    print("\n2. Pierwsze 5 rekordów:")
    for record in data[:5]:
        print(record["id"], record["title"])