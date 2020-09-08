
import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
k=1.38*10**-23
T=3000
N=10**5
mp=1.6817*10**-27
m=2*mp

v=np.linspace(0*10**4,3*10**4,100)

def P(vx):
    'MB'
    return (m/(2*np.pi*k*T)**(3/2))*np.exp(-(1/2)*(m*vx**2)/(k*T))

a=P(v)

plt.plot(v,a)
plt.xlabel('Velocity of the particles')
plt.ylabel('Probability density')
plt.show()

#Plottet er helt likt for v>0, det er ikke negativt.
#Absolutt hastighets distribusjon gir |v| absoluttverdien.

#v inneholder vx,vy og vz.
#v kan beskrives med maxwell boltzmann distribusjonen, mens vx må beskrives med Gauss distribusjonen.
#Grafen er ikke symmetrisk.
