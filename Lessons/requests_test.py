import requests

url = "https://example.com"
params = {
    "City": "Miass"
    }
response = requests.get(url, params=params)



print("Статус: ", response.status_code)
print("URL", response.url)
print("Ответ: ")
print(response.text)


if response.status_code == 200:
    print("Успешный запрос!!!")
else:
    print("Ошибочка")