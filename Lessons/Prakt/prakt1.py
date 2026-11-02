while True:
    import random

    Copliment = ["Красивый", "Тупой", "Нервный"]
    friend = ["Дотер", "Игрок", "Человек"]
    itog = f"{random.choice(Copliment)} {random.choice(friend)}"
    Who_u = input("Как тебя зовут? ")

    print(f"{Who_u} ты {itog}")