# 3) Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
#  Пример:
# Для n = 5: сумма = 11,55



n = int(input('Введите целое число : '))
order = []

for i in range(1, n+1):
    order.append((1 + (1/i))**i)

print(order)

print (sum(order))

