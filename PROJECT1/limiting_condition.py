"""
This is a file to evaluate
the limiting condition for integral
methods. 

"""
import integral_methods as im
import scipy as si
import numpy as np

# Defining the integral
def E_field(x, z=10e10):
    return z*(z+x**2)**(-3/2)

# Setting up the parameters
lower_bound = 0
upper_bound = 5
number_of_itterations = 1000
width = abs((upper_bound-lower_bound)/number_of_itterations)
x_vals = np.arange(lower_bound, upper_bound+width, width)

# Calculations for Reimann Sum
left_RS = im.Reimann_Sum(E_field, lower_bound, upper_bound, number_of_itterations, type='left')
right_RS = im.Reimann_Sum(E_field, lower_bound, upper_bound, number_of_itterations, type='right')
mid_point_RS = im.Reimann_Sum(E_field, lower_bound, upper_bound, number_of_itterations, type='midpoint')

# Calculations for Trepozdial
trepozdial = im.Trapezoidal(E_field, lower_bound, upper_bound, number_of_itterations)
trepozdial_si = si.integrate.trapezoid(E_field(x_vals), dx=width)

# Calculations for Simpson
simpson = im.Simpson(E_field, lower_bound, upper_bound, number_of_itterations)
simpson_si = si.integrate.simpson(E_field(x_vals), dx=width)

# Printing out the results
print("Value for the integral with left Reimann Sum method:", left_RS)
print("Value for the integral with right Reimann Sum method:", right_RS)
print("Value for the integral with mid-point Reimann Sum method:", mid_point_RS)

print("Value for the integral with trepozdial method:", trepozdial)
print("Value for the integral with Scipy impelented trepozdial method:", trepozdial_si)

print("Value for the integral with Simpson method:", simpson)
print("Value for the integral with Scipy impelented Simpson method:", simpson_si)
