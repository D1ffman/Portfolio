# Создай словарь developer со следующими данными:
# - name — твоё имя;
# - age — твой возраст;
# - language — Python;
# - level — Beginner.
# Затем программа должна:
# 1. Вывести имя и язык программирования.
# 2. Изменить level на Intermediate.
# 3. Добавить ключ city с названием города.
# 4. Проверить, существует ли ключ Git.
# 5. Вывести все ключи и значения через .items().


developer = {
    "name": "Egor", 
    "age": 30,
    "language": "Python",
    "level": "Beginner"
    }
print(developer["name"], developer["language"])
developer["level"] = "Intermediate"
developer["city"] = "Miass"
print("git" in developer)
print(developer.items())
