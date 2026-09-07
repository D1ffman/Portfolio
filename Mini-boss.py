import requests

url = ("https://example.com")
params = {
    "city":"Miass"
    }
response = requests.get(url, params=params)


print(response.url)
if response.status_code == 200:
    print("Молодец", response.status_code)
else:
    print("Ошибочка!")
print("Ответ:", response.text)