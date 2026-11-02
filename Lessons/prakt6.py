# Напиши программу, которая:
# 1. Находит всех уникальных пользователей из обеих групп.
# 2. Находит пользователей, которые есть в обеих группах.
# 3. Находит пользователей, которые есть только в group_a.
# 4. Выводит количество пользователей в каждой полученной группе.
# Используй union(), intersection(), difference() и len().


group_a = {"Egor", "Alex", "Ivan", "Max"}
group_b = {"Alex", "Max", "John", "David"}

print(group_a.union(group_b))
print(group_a&group_b)
print(group_a-group_b)
print(len(group_a.union(group_b)))
print(len(group_a&group_b))
print(len(group_a-group_b))