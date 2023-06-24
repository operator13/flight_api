import requests

url = "http://localhost:1337/api/flights/7"

payload = ""
headers = {}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)