import requests

response = requests.get("http://localhost:5000/data")
data = response.json()
print(data)
