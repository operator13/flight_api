import requests
import json

url = "http://localhost:1337/api/flights"

payload = json.dumps({
  "data": {
    "FlightNumber": "UA96",
    "Seats": 400,
    "airline": 1,
    "OriginAirport": 1,
    "DestinationAirport": 4
  }
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)