#4) Задайте число N и создайте список, заполненный числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите целое число : '))
order = [i for i in range(-n, n+1)]
print(order)

path = 'C:\\Users\\antip\\Desktop\\учеба\\python\\DZ\\dz6\\chisla.txt'
data = open(path, 'r')
chis = [line for line in data]
print(chis)
data.close()

res = 1
for i in range(len(chis)):
    io = chis[i]
    io = int(io)
    vr = order[io]
    res *= vr

print(f'Результат умножения чисел из строки по индексам из файла chisla.txt : {res}')



