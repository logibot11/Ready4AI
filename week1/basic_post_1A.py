# Autor uczący się: Jarosław Krefft
# Data utworzenia: 30.04.2026
# Nazwa i wersja programu: basic_post_1A.py
# Adres : https://jsonplaceholder.typicode.com/
# Kod wysyła żądanie HTTP POST do API JSONPlaceholder, tworząc nowy „post” z podanymi danymi i wyświetlając odpowiedź zwróconą przez serwer.

import requests

url = "https://jsonplaceholder.typicode.com/posts"

new_post = {
    "userId": 1,
    "title": "Mój post testowy - JK",
    "body" : "Post wygenerowany na potrzeby edukacyjne w języku Python"   
}

response = requests.post(url, json=new_post)

data = response.json()

print("ID:", data["id"])
print("Tytuł:", data["title"])
print("Body:", data["body"])

