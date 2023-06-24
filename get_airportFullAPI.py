import requests

url = "http://localhost:1337/api/airports"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)