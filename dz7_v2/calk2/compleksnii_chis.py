
def compl(x, y, znak):
    

    if znak in ('+', '-', '/', '*'):
                
        if znak == '+':
            result = str(x) + '+' + str(y) + '=' + str(x + y)              
        elif znak == '-':
            result = str(x) + '-' + str(y) + '=' + str(x - y)         
        elif znak == '*':
            result = str(x) + '*' + str(y) + '=' + str(x * y)         
        elif znak == '/':
            result = str(x) + '/' + str(y) + '=' + str(x / y)         
        else:
            return print('Введен не корректный знак арифметической операции')
        return result
    
    