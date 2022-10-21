import model_mult as model
import view
x = ''
y = ''
compleks_irracional = ''

def button_click():
    model.init(x, y)
    #value_a = view.get_value()
    #value_b = view.get_value()
    
    value_b, value_a = model.compleks_irracional(type)
    model.compleks_irracional(type)   
    model.mult(x, y) 
    #value_b = model.compleks_irracional(type)
    
    result = model.mult(x, y)
    view.view_data(result, 'mult')