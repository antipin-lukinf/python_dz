# 1. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

print(eval('2+2*2'))

primer = input('Введите арифметическое выражение : ')
mult = '*'
div = '/'
plus = '+'
minus = '-'

evalution = '2 + 2 * 2'

eval_lst = evalution.split()
res = 0
i = 0
while len(eval_lst) != 1:
    while True:
        
        if mult or div in eval_lst:
            el = eval_lst[i]
            if el == mult or el == div:
                if el == mult:
                    res = float(eval_lst[i-1]) * float(eval_lst[i+1])
                else:
                    res = float(eval_lst[i-1]) / float(eval_lst[i+1])
                eval_lst[i] = str(res)
                eval_lst.pop(i+1)
                eval_lst.pop(i-1)
                i = 0
                continue
            
        else:
            break
        i += 1

    while True:
        if plus or minus in eval_lst:
            el = eval_lst[i]
            if el == plus or el == minus:
                if el == plus:
                    res = float(eval_lst[i-1]) + float(eval_lst[i+1])
                else:
                    res = float(eval_lst[i-1]) - float(eval_lst[i+1])
                eval_lst[i] = str(res)
                eval_lst.pop(i+1)
                eval_lst.pop(i-1)
                i = 0
                continue
            
        else:
            break
        i += 1




# evalution = evalution.replace(' ', '')
# num_list = []
# num = ''
# for char in evalution:
# if char.isdigit():
# num = num + char
# print(num)
# else:
# num_list.append(int(num))
# num_list.append(char)
# num = ''
# num_list.append(int(num))