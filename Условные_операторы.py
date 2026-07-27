#Условные операторы

age = int(input("Сколько вам лет: "))

if age >= 18:
    print("Вы подходите!")
elif age < 0:
    print("Ты еще не готов)")
else:
    print("Приходите позже")


food = input("Тебе нравится еда? (Да/Нет): ")

if food == "Да":
    print("Приятного аппетита!")
else:
    print("что именно тебя не устраивает?")


Name = input("Enter y name: ")

if Name == "":
    print("Ты не написал свое имя!!!")
else:
    print(f"Красивое у тебя имя, {Name}, мне очень приятно познакомиться!!!")


For_sale = True

if For_sale:
    print("Этот предмет со скидкой!")
else:
    print("На этот предмет нет скидки")