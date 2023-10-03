"""
This script contains implementations of different 
ODE solver methods.
"""

import numpy as np

def Runge_Kuta(f, dur, y, num_step):
    """
    Input
    --------
    f: function, function that needs to be solved.
    dur: list, time interval that ODE is solved
    y: list, initial condisitons
    num_step: int, number of itterations

    Returns
    ---------
    y: numpy array, solutions to ODE
    t: numpy array, time interval
    """
    
    step_size = (dur[1] - dur[0])/num_step
    t = np.linspace(dur[1], dur[0], num_step+1)
    for i in range(num_step):
        k1 = step_size * f(y[i], t[i])
        k2 = step_size * f(np.array(y[i]) + step_size/2, t[i] + k1/2)
        k3 = step_size * f(np.array(y[i]) + step_size/2, t[i] + k2/2)
        k4 = step_size * f(np.array(y[i]) + step_size, t[i] + k3)
        arr = y[i] + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
        y.append(arr.tolist())
    return np.array(y), np.array(t)

def Euler(f, dur, y, num_step):
    """
    Input
    --------
    f: function, function that needs to be solved.
    dur: list, time interval that ODE is solved
    y: list, initial condisitons
    num_step: int, number of itterations

    Returns
    ---------
    x_list: numpy array, position solutions
    u_list: numpy array, velocity solutions
    """
    step_size = (dur[1] - dur[0])/num_step
    t = np.linspace(dur[1], dur[0], num_step+1)
    x_list = []
    u_list = []
    for i in range(num_step):
        x = (y[:3] + step_size * y[3:]).tolist()
        u = (y[3:] + step_size * f(t[i], y)[3:]).tolist()       
        x_list.append(x)
        u_list.append(u)
    return np.array(x_list), np.array(u_list)