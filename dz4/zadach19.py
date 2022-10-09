# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# -  k=4 => 2*x^4 + 4*x^3 + 5x^2  - 3x + 3 = 0

import numpy as np
from random import randint
k = randint(0, 10)
#print (k)


a= np.array([k,k-1,k-2])
f = np.poly1d(a)
print(f)

path = 'C:\\Users\\antip\\Desktop\\учеба\\python\\DZ\\dz4\\pol.txt'
zap = open(path, 'w')
zap.write(f'{f}')

zap.close()
