#Создать калькулятор для работы с рациональными и комплексными числами,
# организовать меню, добавив в неё систему логирования.
from fractions import Fraction

from compleksnii_chis import compl
from racional import racio
from logger import logger_file
##import comp.calk_complex(x, y, znak)
x = ''
y = ''
znak = ''
result = ''


type = input('Выбирите с каким типом чисел работать. Введите 1 для работы с комплексными числами,\n 2 - для работы с рациональными числами')
znak = input('Введите знак операции (+, -, *, /): ')

if type == '1':
        print('Введите число (используйте формат: "5+3j"):')
        x = complex(input('x = '))
        y = complex(input('y = '))
        result = compl(x, y, znak)
        
    
elif type == '2':
        print('Введите число (используйте формат: "2/3j"):')
        x = Fraction(input('x = '))
        y = Fraction(input('y = '))
        result = racio(x, y, znak)

print(result)
logger_file(result)




