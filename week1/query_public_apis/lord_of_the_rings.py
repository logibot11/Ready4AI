import requests

url = "https://the-one-api.dev/v2/movie"
headers = {"Authorization": "Bearer my_key"}

response = requests.get(url, headers = headers)

if response.status_code == 200:
    print(response.json())
else:
    print("Error:" , response.status_code)