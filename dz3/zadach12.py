# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


ishodnii_spisok = [2, 3, 4, 5, 6, 7, 8]
proizvedenie_par = [0]


def proizvedenie (ishodnii_spisok):
    dlin_list = len(ishodnii_spisok)
    x = 0
    for i in range((len(ishodnii_spisok))//2):
                
        proizvedenie_par[i] = int(ishodnii_spisok[i]) * int(ishodnii_spisok[- i -1])
        proizvedenie_par.append(i)
            
    
    if len(ishodnii_spisok) % 2 != 0:
        proizvedenie_par[((len(ishodnii_spisok)//2))] = int((ishodnii_spisok[(len(ishodnii_spisok)//2)])**2)
    else:
        proizvedenie_par.pop()

    print(proizvedenie_par)

proizvedenie(ishodnii_spisok)