# Autor uczący się: Jarosław Krefft
# Data utworzenia: 30.04.2026
# Nazwa i wersja programu: basic_get_1A.py
# Dane przykładowe API pobierane z: https://jsonplaceholder.typicode.com/
# 1 - sza wersja kodu która pobiera wybrany rekord i na końcu pokazuje ilość rekordów w zasobie danych api

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

# status odpowiedzi
if response.status_code == 200:
    print("Status code: ", response.status_code)
    #dane w formacie JSON
    data = response.json()
    print("Tytuł: ", data["title"])
    print("Treść: ", data["body"])
else:
    print("Błąd:", response.status_code)


#sprawdzenie liczby rekordów 
url_check = "https://jsonplaceholder.typicode.com/posts"
response_check = requests.get(url_check)

if response_check.status_code == 200:
    data2 = response_check.json()
    print("Liczba rekordów: ", len(data2))
else:
    print("Błąd:" ,response_check.status_code)