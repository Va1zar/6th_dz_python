# Определить индексы элементов массива(списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Диапазон от 5 до 15
# Вывод: [1, 9, 13, 14, 19]

import random
length_mass_1 = int(input("Input length of list: "))
random_mass_1 = [random.randint(1, 20) for _ in range(length_mass_1)]
print(random_mass_1)
min_number = int(input("Input min grade: "))
max_number = int(input("Input max grade: "))
for i in range(len(random_mass_1)):
    if min_number <= random_mass_1[i] <= max_number:
        print(i)
