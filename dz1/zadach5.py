# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = int(input('Введите координату X1 первой точки : '))
y1 = int(input('Введите координату Y1 первой точки : '))

x2 = int(input('Введите координату X2 второй точки : '))
y2 = int(input('Введите координату Y2 второй точки : '))

import math
dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print (f'Расстояние между введенными точками : {dist}')