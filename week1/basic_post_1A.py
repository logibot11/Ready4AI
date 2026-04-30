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

