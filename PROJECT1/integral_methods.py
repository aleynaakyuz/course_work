"""
This script contains implementations of different 
integration methods.
"""


import numpy as np

def Reimann_Sum(f, lower, upper, step_size, type='left'):
    """
    Inputs
    -----------
    f: function, function that is integrated.
    lower: int or float, lower bound of the integral
    upper: int or float, lower bound of the integral
    step_size: int, length of each integral
    type: str, type of reimann sum

    Returns
    -----------
    result: float, area under the curve
    """
    width = abs((upper-lower)/step_size)
    
    x_vals = np.arange(lower, upper+width, width)

    if type == 'left':
        y = f(x_vals[:-1]) * width
        result = np.sum(y)

    if type == 'right':
        y = f(x_vals[1:]) * width
        result = np.sum(y)
    
    if type == 'midpoint':
        x = (x_vals[1:] + x_vals[:-1])/2
        result = np.sum(width*f(x))
    return result


def Trapezoidal(f, lower, upper, step_size):
    """
    Inputs
    -----------
    f: function, function that is integrated.
    lower: int or float, lower bound of the integral
    upper: int or float, lower bound of the integral
    step_size: int, length of each integral

    Returns
    -----------
    sums: float, area under the curve
    """
    
    width = abs((upper-lower)/step_size)
    x_vals = np.arange(lower, upper+width, width)
    
    vals = 2*f(x_vals[1:-1])
    sums = (np.sum(vals) + f(x_vals[0]) + f(x_vals[-1]))*(width/2)
    
    return sums


def Simpson(f, lower, upper, step_size):
    """
    Inputs
    -----------
    f: function, function that is integrated.
    lower: int or float, lower bound of the integral
    upper: int or float, lower bound of the integral
    step_size: int, length of each integral

    Returns
    -----------
    summ: float, area under the curve
    """
    
    width = abs((upper-lower)/step_size)
    x_vals = np.arange(lower, upper+width, width)
    
    mults = x_vals[1:-1]
    odds = f(mults[::2])*4
    evens = f(mults[1::2])*2
    summ = (np.sum(odds) + np.sum(evens) + f(x_vals[0]) + f(x_vals[-1]))*(width/3)
    
    return summ