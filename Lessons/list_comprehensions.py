#doubles = [x * 2 for x in range(1, 10)]
#triples = [y * 3 for y in range(1, 9)]
#sqares = [z * 3 for z in range(1, 10)]

#print(sqares)


#fruits = ["apple", "orange", "banana", "cocount"]
#fruits = [fruit.upper() for fruit in fruits]
#fruits = [fruit[0] for fruit in fruits]
#print(fruits)


#numbers = [1, -2, 3, -4, 5, -6]
#positive_nums = [num for num in numbers if num >= 0]
#negative_nums = [num for num in numbers if num < 0]
#even_nums = [num for num in numbers if num % 2 == 0]

#print(positive_nums)
#print(negative_nums)
#print(even_nums)


grades = [85, 42, 79, 90, 51, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)