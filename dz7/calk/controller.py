import model_mult as model
import view
x = ''
y = ''

def button_click():
    #model.compleks_irracional(type)
    #value_a = view.get_value()
    #value_b = view.get_value()
    value_b, value_a = model.compleks_irracional(type)
    #value_b = model.compleks_irracional(type)
    model.init(value_a, value_b)
    result = model.mult(x, y)
    view.view_data(result, 'mult')