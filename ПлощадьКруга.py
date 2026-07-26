#Площадь круга

import math

radius = float(input("Напиши радиус круга: "))

A = math.pi * pow(radius, 2)

print(f"Площадь круга равна:  {round(A, 2)}")