#4) Задайте число N и создайте список, заполненный числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите целое число : '))
order = []
#i = -n

for i in range(-n, n+1):
    order.append(i)

print(order)

chis = []
path = 'C:\\Users\\antip\\Desktop\\учеба\\python\\DZ\\dz2\\chisla.txt'
data = open(path, 'r')
for line in data:
    chis.append(line)
print(chis)

# ch = chis
# list(map(int, ch))
# print(chis)


