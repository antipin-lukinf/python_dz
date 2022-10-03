# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


ishodnii_spisok = [2, 3, 4, 5]
proizvedenie_par = []

def proizvedenie (ishodnii_spisok):
    dlin_list = int(len(ishodnii_spisok)/2)
    for i in range(1, len(ishodnii_spisok), 1):
        i = int(i)
        proizvedenie_par.append
        proizvedenie_par[i] = str(ishodnii_spisok[i] * ishodnii_spisok(dlin_list - i))
   # if len(ishodnii_spisok) % 2 != 0
    print(ishodnii_spisok)

proizvedenie(ishodnii_spisok)