import model_mult as model

def view_data(data, title):
    print(f'{title} = {data}')

# def input_data():
#     print('С какими числами будем работать? Введите 1 для работы с комплексными числами, 2 - для работы с рациональными числами')
#     data_type = get_value()
#     if data_type == '1':
#         print('Введите первое число (используйте формат: "5 + 3j"):')
#         left_value = get_value()
#         print('Введите второе число (используйте формат: "5 + 3j"):')
#         right_value = get_value()
#         print('Выберите операцию:')
#         oper = get_value()
#     elif data_type == '2':
#         print('Введите первое число (используйте формат: "5/11"):')
#         left_value = get_value()
#         print('Введите второе число (используйте формат: "5/11"):')
#         right_value = get_value()
#         print('Выберите операцию:')
#         oper = get_value()
#     return (data_type, left_value, oper, right_value)

def get_value():
    model.compleks_irracional(type)
    return int(input('value = '))

def get_znak():
    znak = input('Введите знак операции : ')
    return znak

def type_calk():
    type = input('Выбирите с каким типом чисел работать. Введите 1 для работы с комплексными числами, 2 - для работы с рациональными числами')
    return type

