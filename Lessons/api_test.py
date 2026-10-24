import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)
data = response.json()

#print("Статус:", response.status_code)
#print("Ответ:", response.text)

#print(data)
print(response.status_code)
print(data["title"])
print(data["completed"])
