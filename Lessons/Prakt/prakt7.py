# Твоя задача:
# 1. Создать функцию binary_search.
# 2. Найти середину списка.
# 3. Сравнить середину с target.
# 4. Вернуть индекс найденного числа.
# 5. Если число отсутствует — вернуть -1.

numbers = [5, 10, 15, 20, 25, 30, 35]
target = 25
left = 0
right = len(numbers) - 1

middle = (left + right) // 2
def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2
        if numbers[middle] == target:
            print(f"Число {target} найдено в списке по индексу {middle}.")
            return middle
        elif numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1

numbers = [5, 10, 15, 20, 25, 30, 35]
target = 25

result = binary_search(numbers, target)
print(result)