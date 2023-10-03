"""
This is main file for ODE solutions
"""
import ode_methods as om
import scipy as si
import numpy as np
import matplotlib.pyplot as plt

# Defining ODE
def f(y, t):
    return np.array([y[3], y[4], y[5], y[1]-y[0], y[2]+y[0]-2*y[1], y[1]-y[2]])

# Results from Runge Kuta Method
y, t = om.Runge_Kuta(f, dur = [0, 50], y = [[-1.8, 0.8, 1.0, 0, 0, 0]], num_step=100000)

plt.plot(y[:,0], label='Soln 1')
plt.plot(y[:,1], label='Soln 2')
plt.plot(y[:,2], label='Soln 3')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Runge Kuta Solution for Position')
plt.savefig('Runge_Kuta.png')
plt.show()

plt.plot(y[:,3], label='Soln 1')
plt.plot(y[:,4], label='Soln 2')
plt.plot(y[:,5], label='Soln 3')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Runge Kuta Solution for Velocity')
plt.savefig('Runge_Kuta_velocity.png')
plt.show()

# Defining ODE
def f(t, y):
    return np.array([y[3], y[4], y[5], y[1]-y[0], y[2]+y[0]-2*y[1], y[1]-y[2]])

# Resuts from Scipy Method
soln=si.integrate.solve_ivp(f, [0, 50], [-1.8, 0.8, 1.0, 0, 0, 0], dense_output=True)

t=np.linspace(0, 50, 1000)
y=soln.sol(t)
plt.plot(t, y[0], label='Soln 1')
plt.plot(t, y[1], label='Soln 2')
plt.plot(t, y[2], label='Soln 3')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Scipy Solution for Position')
plt.savefig('Scipy.png')
plt.show()


t=np.linspace(0, 50, 1000)
y=soln.sol(t)
plt.plot(t, y[3], label='Soln 1')
plt.plot(t, y[4], label='Soln 2')
plt.plot(t, y[5], label='Soln 3')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Scipy Solution for Velocity')
plt.savefig('Scipy_velocity.png')
plt.show()


# This method does not create physical solutions
x, u = om.Euler(f, np.array([0, 50]), np.array([-1.8, 0.8, 1.0, 0, 0, 0]), 10000)

plt.plot(x[:,0])
plt.plot(x[:,1])
plt.plot(x[:,2])
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Euler Solution for position')
plt.savefig('Euler_velocity.png')
plt.show()