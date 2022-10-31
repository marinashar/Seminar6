# 1. Задайте рандомно список из чисел размером N, где N число с клавиатуры. Напишите программу, которая найдёт сумму 
# элементов списка, стоящих на нечётной позиции.
# *Пример:*
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# import random
# N = int(input('Введите размер списка: '))
# lst = []
# for i in range (N):
#     lst.append(random.randint(0, 10))
# print(lst)

# def GetSumOdd(lst):
#     summa = 0
#     for i in range (len(lst)):
#         if i % 2 != 0:
#             summa += lst[i]
#     print(f"Сумма чисел на нечетных позициях элементов равна {summa}")
# GetSumOdd(lst)

import random
def GetSumOdd(lst):
    summa = 0
    for i in range (len(lst)):
        if i % 2 != 0:
            summa += lst[i]
    print(f"Сумма чисел на нечетных позициях элементов равна {summa}")

lst = list(map(int, input("Введите числа через пробел:\n").split()))
GetSumOdd(lst)

# _________________________________________________________________________________________________________________________

# 2. Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности

# from random import randint as rI
# uniqueList ={}
# finalStr = ''
# listStr = "".join(list(map(str, [rI(0, 9) for i in range(20)])))
# print(f'Задана последовательность цифр {listStr}')
# for c in listStr:
#     if uniqueList.get(c):
#         uniqueList[c] = uniqueList.get(c) + 1
#     else:
#         uniqueList[c] = 1
# for i in uniqueList.items():
#     if i[1] == 1:
#         finalStr += str(i[0])
# print(f'Уникальные цифры {finalStr}') if finalStr else print('Уникальных позиций нет')

from random import randint as rI

listStr = "".join(list(map(str, [rI(0, 9) for i in range(20)])))
print(f'Задана последовательность цифр {listStr}')
finalStr = list(filter(lambda a: listStr.count(a) == 1, listStr))
print(f'Уникальные цифры {finalStr}') if finalStr else print('Уникальных позиций нет')


