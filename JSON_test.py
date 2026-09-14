import requests

url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url)
data = response.json()


for i in range(5):
    print("userId:", data[i]["userId"])
    print("Id:", data[i]["id"])
    print("title:", data[i]["title"])
    print("completed:", data[i]["completed"])
 
  