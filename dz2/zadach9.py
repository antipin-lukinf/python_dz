#4) Задайте число N и создайте список, заполненный числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите целое число : '))
order = []


for i in range(-n, n+1):
    order.append(i)

print(order)


chis = []
path = 'C:\\Users\\antip\\Desktop\\учеба\\python\\DZ\\dz2\\chisla.txt'
data = open(path, 'r')
for line in data:
    chis.append(line)
print(chis)

data.close()


res = 1
i = 0
len_chis = int(len(chis))
print(f'Длинна массива индексов {len_chis}')
for i in range(0, len_chis, 1):
    print(f'индекс i  {i}')
    io = chis[i]
    io = int(io)
    vr = order[io]
    vr = int(vr)
    print(f'число строки {vr}')
    res *= vr

print(f'Результат умножения чисел из строки по индексам из файла chisla.txt : {res}')






