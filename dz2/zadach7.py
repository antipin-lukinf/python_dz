nunber_factorial = int(input('Введите целое число : '))
factorial = 1
print('[', end = ' ')
for i in range(1, nunber_factorial+1):
    factorial *= i
    print(factorial, end = ', ') 

print (']')