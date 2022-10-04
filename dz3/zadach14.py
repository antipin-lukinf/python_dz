# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите целое число : '))





def fibonachi(n):
    if n <= 0:
        return "Введено не корректное число"
    order = [0, 1]
    if n > 2:
        for i in range(2, n):
            order.append(order[i-1] + order[i-2])
    return order[n-1]
 

# fibonachi (n)

# def nega_fibonachi(n):
#     if n <= 0:
#         return "Введено не корректное число"
#     order = [-1, 0]
#     if n > 2:
#         for i in range(-2, -n, -1):
#             order.append(order[i+2] - order[n+1])
#     return order[n+1]
 

fibonachi (n)
print (fibonachi(n))
#nega_fibonachi(-n)
fibonachi (-n)
print (fibonachi(-n))
#print (nega_fibonachi(-n))


