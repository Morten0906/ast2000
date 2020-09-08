
import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
k=1.38*10**-23
T=3000
N=10**5
mp=1.6817*10**-27
m=2*mp


v = sy.Symbol('v')
F = v*(m/(2*sy.pi*k*T)**(3/2))*sy.exp(-(1/2)*(m*v**2)/(k*T))*4*sy.pi*v**2
a=sy.integrate(F,(v,0,np.inf))
print(a)

#Integrasjon av en skalar.
#a=1.71106553724661e+17*pi**(-0.5)

