#2) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)



nunber_factorial = int(input('Введите целое число : '))
factorial = 1
print('[', end = ' ')
for i in range(1, nunber_factorial+1):
    factorial *= i
    print(factorial, end = ', ') 

print (']')