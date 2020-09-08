
import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
k=1.38*10**-23
T=3000
N=10**5
mp=1.6817*10**-27
m=2*mp

v=np.linspace(5*10**3,30*10**3,100)

v = sy.Symbol('v')
F = (m/(2*sy.pi*k*T)**(3/2))*sy.exp(-(1/2)*(m*v**2)/(k*T))
a=sy.integrate(F,(v,5*10^3,30*10**3))
plt.xlabel('Velocity of the particles')
plt.ylabel('Probability density')
print(a)

#Integral

#a=346307.835926943*pi**(-1.0)

#Vi får hastighetsdistribusjonen mellom 5*10**3,30*10**3.

#Fra -inf til inf kan du forvente 1 som tilsvarer alle partiklene.

#Når vi ganger med med N får vi.

#a*N=34630783592.6943*pi**(-1.0)

#Da får vi forventet antall partikler som har hastighet mellom 5*10**3,30*10**3.


