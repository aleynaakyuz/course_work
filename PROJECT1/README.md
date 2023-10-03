Dependincies:
python==3.11.4 
ipython==8.12.2
scipy==1.11.3 
numpy==1.25.2
matplotlib==3.7.2          
matplotlib-base==3.7.2          
matplotlib-inline==0.1.6

This program consists of 5 python and 2 ipynb
files. 

integral_methods.py: Consists of functions to 
numarically evaluate the integrals.

main_integrals.py: Calls integral_methods.py
and evaluates an integral.

limiting_condition.py: Calls integral_methods.py
and evaluates an integral in a limiting condition.

ode_methods.py: Consists of functions to 
numarically solve ODEs.

main_ode.py: Calls ode_methods.py and evalues the ODEs.
Visualies the solutions.

Time_integral.ipynb: Run time calculations of integral
evaluations. 

Time_ode.ipynb: Run time calculations of ODE
solutions.

Notes:

- Euler methods does not produce physical solutions.
- Time evaluations represetended in ipynb files since
%timeit method only works with iPython
