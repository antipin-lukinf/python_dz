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





# import math

# def make_pairs_prodact():
# try:
# num_list = input("Enter numbers without spaces: ")
# num_list = [int(i) for i in num_list]
# pair_list = []
# for i in range(math.ceil(len(num_list)/2)):
# pair_prodact = num_list[i]*num_list[-1*(i+1)]
# pair_list.append(pair_prodact)
# print("\033[36m{}{}{}".format(num_list, " --> ", pair_list))
# except ValueError:
# print("\033[1m\033[31m{}".format("You must enter an integer!"))

# make_pairs_prodact()