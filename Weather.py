import requests

url = " "

params = {
    "Ширина": 55.75, 
    "Долгота": 37.62, 
    "Данные": "temperature_2m,relative-humidity_2m,wind_speed_10m"
}

response = requests.get(url, params=params)

print(response.status_code)
print(response.json())

