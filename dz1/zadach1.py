# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

den = int(input('Введите номер дня недели '))
if 1 <= den <= 5:
    print('Этот день недели является рабочим')
elif 5 <= den <= 7:
    print('Этот день недели является выходным')
else: print('Дня недели с таким номером не существует')