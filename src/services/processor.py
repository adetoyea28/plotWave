import re
import math as mt
from simpleeval import simple_eval

def resolveFunction(function, x_value):
    string = re.sub(r'\b[a-zA-Z]\b', r'\g<0>', function)
    string = re.sub(r'(d)([a-z])', r'\1*\2', string)
    string = re.sub(r'\^', r'**', string)

    safe_functions = {
        "sin": lambda x: mt.sin(mt.radians(x)),
        "cos": lambda x: mt.cos(mt.radians(x)),
        "tan": lambda x: mt.tan(mt.radians(x)),
        "cosec": lambda x: 1 / mt.sin(mt.radians(x)),
        "sec": lambda x: 1 / mt.cos(mt.radians(x)),
        "cot": lambda x: 1 / mt.tan(mt.radians(x)),
        "ln": lambda x: mt.log(x),
        "log": lambda x, base: mt.log(x,base)
    }
    variables = {
        "x": x_value,
        "e": mt.e,
        "pi": mt.pi
    }
    y_value = simple_eval(string, names=variables, functions=safe_functions)
    return y_value



def processFunction(func_expr, start, stop):
    x_values = []
    y_values = []

    for x in range(start, stop+1, 1):
        y = resolveFunction(func_expr, x)
        x_values.append(x)
        y_values.append(y)
    
    coordinates = []

    for index, x in enumerate(x_values):
        coordinate_pair = [x, y_values[index]]
        coordinates.append(coordinate_pair)
    
    return coordinates
