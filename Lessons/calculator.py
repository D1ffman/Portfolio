#Calculator


operator = input("Выбери операцию (+ - * /): ")

num1 = float(input("Введи первое число: "))
num2 = float(input("Введи второе число: "))

#print(num1 + num2)

if operator == "+":
    result = num1 + num2
    print(round(result))
elif operator == "-":
    result = num1 - num2
    print(round(result))
elif operator == "*":
    result = num1 * num2
    print(round(result))
elif operator == "/":
    result = num1 / num2
    print(round(result))
else:
    print(f"{operator} не подходит, выбери операцию!")