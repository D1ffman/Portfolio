import requests

url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url)
data = response.json()


for task in data[:5]:
    print("userId:", task["userId"])
    print("Id:", task["id"])
    print("title:", task["title"])
    print("completed:", task["completed"])
    print()
  