import numpy as np
import matplotlib.pyplot as plt

k=1.38*10**-23
T=3000
#N=10**5
mp=1.6817*10**-27
m=2*mp

velocity=np.linspace(-2.5*10**4,2.5*10**4,100)

def P(vx):
    'MB'
    return (m/(2*np.pi*k*T)**(3/2))*np.exp(-(1/2)*(m*vx**2)/(k*T))

a=P(velocity)
plt.plot(velocity,a)
plt.xlabel('Velocity [m/s]')
plt.ylabel('Probability density')
plt.show()


#Forklar kurven. Kurven beskriver den tilfeldige hastighetsdistribusjen for alle partiklene.
#Den gjennomsnittlige hastigheten i gassen er opprettholdt, selv om nesten alle partikklene f[r
#en tilfeldig hastighet som skiller seg ut fra resten av partiklene.
#X-aksen beskriver hvor stor hastighet i negativ og positiv retning, Y-aksen beskriven antall partikkler.

