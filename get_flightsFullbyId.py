import requests

id = 5
url = f"http://localhost:1337/api/flights/{id}/?populate=flightnumber,airline,seats,OriginAirport,DestinationAirport"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)