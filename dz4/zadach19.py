# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# -  k=4 => 2*x^4 + 4*x^3 + 5x^2  - 3x + 3 = 0

# import numpy as np
import random
k = int(input('Введите максимальную степень многочлена : '))

def mnog(value):
    lst = []
    eq = ' = 0'
    for i in range(0, value + 1):
        lst.append(random.randint(0, 100))
        if lst[i] != 0:
            if i == 0:
                eq = str(lst[i]) + eq
            elif i == 1:
                eq = str(lst[i]) + ' *x + '+ eq
            else:
                eq = str(lst[i]) + ' *x^' + str(i) + ' + ' + eq 
    return eq

mnog(k)

path = 'C:\\Users\\antip\\Desktop\\учеба\\python\\DZ\\dz4\\pol.txt'
zap = open(path, 'w')
zap.write(f'{mnog(k)}')

zap.close()
