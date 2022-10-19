import cmath
import math

from fractions import Fraction
import view

x = 0
y = 0
znak = ''
i = 0

def init(a, b):
    global x           # для доступа к глобальным переменным
    global y
    global znak
    type = view.type_calk()
    x, y = compleks_irracional(type)
    #y = compleks_irracional(type)
    znak = view.get_znak()
    x = a
    y = b

def mult(x, y):
    
    if znak in ('+', '-', '/', '*'):        
        if znak == '+':
            return x + y
        elif znak == '-':
            #print(f'{x} - {y} = ', x-y)
            return x - y
        elif znak == '*':
            return x * y
        elif znak == '/':
            return x / y
        else:
            return print('Введен не корректный знак арифметической операции')

def compleks_irracional(type):
    global x           # для доступа к глобальным переменным
    global y
    
    if type == '1':
        print('Введите первое число (используйте формат: "5.11"):')
        x = complex(input('x = '))
        y = complex(input('y = '))
        print (x)
        print (y)
        #x = complex(x)
        #y = complex(y)
    
    elif type == '2':
        x = Fraction(input('x = '))
        y = Fraction(input('y = '))

        #a = x
        x = Fraction(int(x[0: x.index('/')]), int(x[x.index('/')+1:len(x)]))
        #g = y
        y = Fraction(int(y[0: y.index('/')]), int(y[y.index('/')+1:len(y)]))
    return x, y





    #  if data_type == '1':

    #     left_value = complex(left_value)

    #     right_value = complex(right_value)

    # elif data_type == '2':

    #     a = left_value
    #     left_value = Fraction(int(a[0: a.index(
    #         '/')]), int(a[a.index('/')+1:len(a)]))

    #     g = right_value
    #     right_value = Fraction(int(g[0: g.index(
    #         '/')]), int(g[g.index('/')+1:len(g)]))

    # return (left_value, oper, right_value)
        