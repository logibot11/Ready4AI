import requests

url = "https://the-one-api.dev/v2/movie"

response = requests.get(url)

if response.status_code == 200:
    print(response.json())
else:
    print("Error:" , response.status_code)
