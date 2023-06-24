import requests
import json

url = "http://localhost:1337/api/flights/7"

payload = json.dumps({
  "data": {
    "FlightNumber": "AA707",
    "Seats": 60,
    "airline": 2,
    "OriginAirport": 3,
    "DestinationAirport": 2
  }
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)