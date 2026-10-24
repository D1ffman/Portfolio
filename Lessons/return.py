"""
Подробное знакомство с return в Python.

Запусти этот файл, чтобы увидеть примеры и их результаты.
"""


# 1. return передает результат из функции в место ее вызова.
def add(a, b):
    result = a + b
    return result


sum_result = add(3, 5)
print("1. Результат функции add:", sum_result)


# Значение можно вернуть сразу, не сохраняя его в промежуточную переменную.
def multiply(a, b):
    return a * b


print("2. Результат функции multiply:", multiply(4, 6))


# 2. return и print делают разные вещи.
# print показывает текст на экране, а return возвращает значение вызывающему коду.
def show_greeting(name):
    print(f"Привет, {name}!")


def make_greeting(name):
    return f"Привет, {name}!"


print("3. Функция с print выводит сообщение:")
show_greeting("Аня")

greeting = make_greeting("Аня")
print("Функция с return дает значение, которое можно сохранить:", greeting)


# 3. Полученный результат можно использовать дальше.
def square(number):
    return number * number


number_squared = square(7)
print("4. Квадрат числа:", number_squared)
print("Можно использовать результат в вычислении:", number_squared + 1)


# 4. return сразу завершает функцию.
# После первого return оставшиеся строки этой функции не выполняются.
def check_number(number):
    if number < 0:
        return "Число отрицательное"

    if number == 0:
        return "Это ноль"

    return "Число положительное"


print("5. Проверка числа -3:", check_number(-3))
print("Проверка числа 0:", check_number(0))
print("Проверка числа 10:", check_number(10))


# 5. Если написать return без значения, функция вернет None.
def say_hello():
    print("Привет!")
    return


hello_result = say_hello()
print("6. Результат функции с пустым return:", hello_result)


# Если функция дошла до конца без return, она тоже вернет None.
def print_message():
    print("В этой функции нет return.")


message_result = print_message()
print("7. Результат функции без return:", message_result)


# 6. Функция может вернуть строку, число, список или другое значение.
def get_colors():
    return ["красный", "зеленый", "синий"]


colors = get_colors()
print("8. Список, возвращенный функцией:", colors)


# 7. Частая ошибка: ожидать, что print вернет напечатанный текст.
# На самом деле print выводит сообщение, но возвращает None.
def print_sum(a, b):
    print(a + b)


print("9. print_sum выводит сумму:")
print_sum(2, 8)

print("Значение, возвращенное print_sum:", print_sum(2, 8))


# Главное:
# - return отдает результат функции вызывающему коду;
# - после return функция прекращает работу;
# - print только выводит информацию на экран;
# - без значения после return (или без return) результатом будет None.
