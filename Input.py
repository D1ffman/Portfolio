#Input

name = input("what is u name?:")
print(f"Hello {name}!")

age = int(input("how old are u?:"))

age = age + 1
print("Happy Birthday!")
print(f"you are {age} years old")



#Практика 1

Длина = float(input("Введи длину: "))
Ширина = float(input("Введи ширину: "))
площадь = Длина * Ширина

print (f"площадь = {площадь}")

#Практика 2

item = input("waht item would you like to buy?: ")
price = float(input("what is the price?: "))
quantity = int(input("how many would you like?: "))

total = price * quantity 

print(f"you have bought {quantity} x {item}/s")
print(f"your total is: ${total}")