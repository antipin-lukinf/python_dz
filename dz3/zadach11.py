# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from unittest import result


spisok = [1, 8, 5, 9, 2, 3, 7, 5, 8, 2]
#resut = 0

def spis_nechet (spisok):
    result = 0
    for i in range(1, len(spisok), 2):
        result += spisok[i]
    print(f'Сумма нечетных элементов списка : {result}')

spis_nechet(spisok)
