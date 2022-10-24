# Доделать решение задачи с телефонным справочником.
# Дополнение: добавить формат ввода данных:
# - под форматами понимаем структуру файлов, например:в файле на одной строке 
# хранится одна часть записи, пустая строка - разделитель
# Фамилия_1
# Имя_1
# Телефон_1
# Описание_1
# Фамилия_2
# Имя_2
# Телефон_2
# Описание_2
# и т.д.в файле на одной строке хранится все записи, символ разделитель - *;***
# Фамилия_1,Имя_1,Телефон_1,Описание_1
# Фамилия_2,Имя_2,Телефон_2,Описание_2
# и т.д.

import re
from distutils.command.clean import clean
from turtle import clear
from vvod import new_contact
from zapros import new_zapros
from zapis_v_spravochnik import zapis

zap = ''
print ('для добавления записи в справочник нажмите 1')
print ('для поиска записи в справочнике нажмите 2')
vibor = int(input())

ln = []
if vibor == 1:
    zapis(str(new_contact()))

if vibor == 2:
    
    zap = new_zapros()
       
    # получим объект файла
    with open(r'DZ\\dz8\\spravochnik.csv', 'r') as file1:
        while True:
            # считываем строку
            for line in file1:
                ln.append(line)
                # прерываем цикл, если строка пустая
                if not line:
                    break
            
            

            
            break
        file1.close

#print(ln)    
for i in ln:
    if zap in i:
        print(f'Искомый контакт  {i}')
    else: print('Контакт с такими данными не существует')

        
   