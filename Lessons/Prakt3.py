import requests

url = "https://jsonplaceholder.typicode.com/todos"
response = requests.get(url)
data = response.json()

while True:
    try:
        задача = int(input(
        "Выберите задачу:\n"
        "1. Показать задачи\n"
        "2. Показать выполненные задачи\n"
        "3. Показать кол-во задач\n"
        "4. Показать не выполненные задачи\n"
        "5. Поиск задачи\n"
        "0. Выход\n"
        ))
        
        if задача == 0:
            print("Вы выбрали выход")
            print()
            break
        elif задача < 0 or задача > 5:
            print("Введите только число из списка!")
            print()
            continue
        
        if задача == 1:

            for task in data:
                print("Номер: ", task["id"])    

                
            номер = int(input("Выберите номер задачи: "))    

            найдена = False
            
            for task in data:
                if номер == task["id"]:
                    print("Название: ", task["title"])
                    print("Айди пользователя: ", task["userId"])
                    print("Выполнение: ", task["completed"])
                    найдена = True
                    print()
                    break
              
            if not найдена:
                print("Задачи нет в списке")
        
        
        if задача == 2:
            print("Выполненные задачи: ")
            for task in data:
                if task["completed"] == True:
                    print("Название:", task["title"])
                    print("Номер:", task["id"])
                    print("Состояние:", task["completed"])
                    print()

        if задача == 3:
            print("Кол-во задач:", len(data))            
            print()

        if задача == 4:
                    print("Не выполненные задачи: ")
                    for task in data:
                        if task["completed"] == False:
                            print("Название:", task["title"])
                            print("Номер:", task["id"])
                            print("Состояние:", task["completed"])
                            print()
        if задача == 5:
            поиск = input("Введите слово для поиска: ")
            print()

            найдено = 0

            
            for task in data:
                if поиск.lower() in task["title"].lower():
                    print("Номер:", task["id"])
                    print("Название", task["title"])
                    print("Состояние", task["completed"])
                    print()
                    найдено += 1
            print("Найдено:", найдено, "задач с вашим запросом.")
            print()

    except ValueError:
        print("Введите только число из списка!")