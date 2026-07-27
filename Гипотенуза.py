#Гипотенуза прямого триугольника


import math


a = float(input("введи сторону a: "))
b = float(input("введи сторону b: "))

Гипотенуза = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Гипотенуза равна: {round(Гипотенуза, 2)}см^2")
