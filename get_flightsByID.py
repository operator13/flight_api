import requests

url = "http://localhost:1337/api/flights/5"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)