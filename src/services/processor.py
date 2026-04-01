import re
import math as mt
from simpleeval import simple_eval

def resolveFunction(function, x_value):
    step1 = re.sub(r'\^', r'**', function)

    step2 = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', step1)

    step3 = re.sub(r'(\))(\d|[a-zA-Z])', r'\1*\2', step2)
    step4 = re.sub(r'(\d)(\()', r'\1*\2', step3)

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
    print(step4)
    y_value = simple_eval(step4, names=variables, functions=safe_functions)
    return y_value



def processFunction(func_expr, start, stop, interval):
    x_values = []
    y_values = []

    for x in range(start, stop+1, interval):
        y = resolveFunction(func_expr, x)
        x_values.append(x)
        y_values.append(y)
    
    coordinates = []
    y_max = max(y_values)
    y_min = min(y_values)

    for index, x in enumerate(x_values):
        coordinate_pair = [x, y_values[index]]
        coordinates.append(coordinate_pair)
    
    return [coordinates, y_max, y_min]
