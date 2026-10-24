
import requests
import logging

def get_tasks():
    url = "https://jsonplaceholder.typicode.com/todos"
    #url = "https://jsonplaceholder.typicode.com/wrong_path"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        tasks = response.json()
        logging.info("API: успешно получено задач: %s", len(tasks))
        return tasks

    except requests.Timeout:
        logging.error("API: превышено время ожидания ответа")
    except requests.ConnectionError:
        logging.error("API: не удалось подключиться к серверу")
    except requests.HTTPError as error:
        logging.error("API: HTTP-ошибка: %s", error)
    except requests.RequestException:
        logging.exception("API: непредвиденная ошибка запроса")

    return None
