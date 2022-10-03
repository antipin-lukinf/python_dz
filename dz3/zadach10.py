# 5) Реализуйте алгоритм перемешивания списка.(Без использования библиотеки random)

import datetime # подключение библиотеки
import time

spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_spisok = [None] * len(spisok)
j = 1


def random (spisok):
    for i in range(len(spisok)):
        index = datetime.datetime.now().microsecond % 10 # получаем милисекунды и получаем остаток от деления на 10 (рандомное число от 0 до 9 )
        random_spisok[i] = spisok[index]
        time.sleep(0.3)
    print(random_spisok)

random (spisok)