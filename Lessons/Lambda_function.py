#add = lambda a, b, c: (a + b) / c
#print(add(12, 20, 21))

#map - возведенеие в квадрат
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)


#filter оставим в списке только чётные числа.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)