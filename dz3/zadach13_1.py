# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

spis = [1.1, 1.2, 3.3, 5.16, 10.01]
drob = list(map(lambda x: x % 1, spis))
for i in range(len(drob)):
    drob[i] = round(list(drob)[i], 2)
  
print(drob)
razn = max(drob) - min (drob)
razn = round(razn, 2)
print(f'Разность максимального элемента массива и минимального : {razn}')

#round(list(decimal)[1], 10)