import requests

url = "http://localhost:1337/api/flights?populate=flightnumber,airline,seats,OriginAirport,DestinationAirport"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)