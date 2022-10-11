# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

from audioop import reverse


n = int(input('Введите целое число : '))


def fibonachi(n):
    if n <= 0:
        return "Введено не корректное число"
    order = [0, 1]
    if n > 2:
        for i in range(2, n+1):
            order.append(order[i-1] + order[i-2])
    return order
 

def nega_fibonachi(n):
    if n <= 0:
        return "Введено не корректное число"
    order1 = [1, -1]
    if n > 2:
        for i in range(2, n):
            order1.append(order1[i-2] - order1[i-1])
    order1.reverse()
    return order1
 
print (nega_fibonachi(n) + fibonachi(n))








