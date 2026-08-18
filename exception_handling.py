try:
    number = int(input("Enter u number: "))


except TypeError:
    print("Что ты пишешь?...")
except ZeroDivisionError:
    print("Нельзя делать тебе так")
except ValueError:
    print("Только числа нужны...")

else:
    print("Вот твой ответ:", 1 / number)
