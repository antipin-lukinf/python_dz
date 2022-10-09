# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def mnogitel(n):
   i = 2
   mn = []
   while i * i <= n:
       while n % i == 0:
           mn.append(i)
           n /= i
       i += 1
   if n > 1:
       mn.append(n)
   return mn

n = int(input('Введите целое число : '))

print(mnogitel(n))