# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# list_length = int(input("Введите длину списка: "))
# list = []
# for i in range (1, list_length + 1):
#     list.append(i)
# print(*list)
# search_number = int(input("Введите число: "))
# print(f"Ваше число встречается {list.count(search_number)} раз(а)")



# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
list_length = int(input("Введите длину списка: "))
list = []
for i in range (list_length):
    list.append(random.randint(1, 10))
print(list)
user_number = int(input("Введите число: "))
min = abs(user_number - list[0])
index = 0
for i in range(list_length):
    if user_number > list[i]:
        if (user_number - list[i]) < min and (user_number - list[i]) != 0:
            index = i
            min = user_number - list[i]
    if user_number < list[i]:
        if (list[i] - user_number) < min and (list[i] - user_number) != 0:
            index = i
            min = user_number - list[i]
print(f"Близкий элемент к вашему числу с индексом {index}")



