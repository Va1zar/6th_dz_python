# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

first_element = int(input("Input 1st element of the list: "))
step = int(input("Input step: "))
my_list_length = int(input("Input length of our list: "))
for i in range(my_list_length):
    print(first_element + i*step)
