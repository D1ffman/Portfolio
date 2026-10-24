# from api_client import get_tasks
# import logging

# logging.basicConfig(
#     filename="app.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s",
#     encoding="utf-8"
#     )
# logging.info("Программа запущена")


import logging
from pathlib import Path
from api_client import get_tasks

log_file = Path(__file__).resolve().parent / "app.log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    force=True
)

logging.info("Программа запущена")


tasks = get_tasks()

if tasks is not None:
    logging.info("Задачи успешно получены: %s", len(tasks))
    print()
    
    
    while True:
        try:
            print("\033[1mПривет тебе, выбери пункт из спика для дальнешьего действия:\033[0m")
            Список = int(input( 
            "\n1. Вывести количество задач"
            "\n2. Вывести только выполненные задачи"
            "\n3. Не выполненные задачи"
            "\n4. Найти задачу по ID"
            "\n0. Выход\n"))
            print()

            if Список == 0:
                logging.info("Пользователь завершил программу")
                print("Программа завершена.")
                break
            

            if Список == 1:
                print("Всего задач:", len(tasks))
                print()
                continue
            elif Список == 2:
                print("\033[1mВыполненные задачи:\033[0m")
                for task in tasks:
                    if task["completed"]:
                        print(task["id"], task["title"])
                    
                print()
            elif Список == 3:
                print("\033[1mНе выполненные задачи:\033[0m")
                for task in tasks:
                    if not task["completed"]:
                        print(task["id"], task["title"])
            elif Список == 4:
                task_id = int(input("Введите ID задачи: "))
                print()
                for task in tasks:
                    if task["id"] == task_id:
                        print(f"Задача с ID {task_id}: "
                            f"{task['title']} - Выполнена: {task['completed']}"
                        )
                        print()
                        break
                else:
                    print("Задача с таким ID не найдена.")
                    print()
            elif Список == 0:
                print("Выход из программы.")
                break
            else:
                print("Такого пункта нет. Выбери число от 0 до 4.")
        
        
        except ValueError:
            logging.warning("Пользователь ввёл не число")
            print("Ошибка: введено не число. Пожалуйста, введите целое число.")
else:
    logging.error("Не удалось получить данные о задачах")
    print("Ошибка: не удалось получить данные о задачах.")
    exit()
    