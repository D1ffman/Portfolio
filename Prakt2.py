import requests

url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(url)

data = response.json()

#for task in data[:5]:
  #  print("userId:", task["userId"])
    #print("Id:", task["id"])
    #print("title:", task["title"])
    #print()
#print("Кол-во задач:", len(data))

#for task in data[:5]:
    
    #if task["completed"] == True:
        #print("Id:", task["id"])
        #print("Название:", task["title"])
        #print("Выполнено:", task["completed"])

while True:
    
    try:
        Задача = int(input("Какую задачу нужно вывести?: "))
        if Задача == 0:
                    break
        найдена = False
        
        for task in data:
                if Задача == task["id"]:
                    print("Айди:", task["id"])
                    print("Название:", task["title"])
                    print("Статус:", task["completed"])
                    print()
                    найдена = True                
        if not найдена:
            print("Задача не найдена, введите число от 1 до 200")        
    except ValueError:
        print("Введите число от 1 до 200")
        print()
            
    
