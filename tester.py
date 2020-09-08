import matplotlib.animation as animation
import matplotlib.pyplot as plt
from scipy.stats import maxwell
import numpy as np
import sympy as sp

#CONSTANTS
k = 1.38064852e-23          #Boltzmann's Constant

#PHYSICAL VARIABLES
T = 3*10**3                 #Temperature in Kelvin
L = 10**-6                  #Box Length in meters
N = 100 #(10**5)            #Number of particles
m = 3.3471153321472e-27     #Mass of individual particle in kg -------------------- Du er ikke 100% sikker -----
hull=0.25*L**2
P=0
Escape=0

#INITIAL CONDITIONS
sigma =   np.sqrt(k*T/m)    #The standard deviation of our particle velocities
my=0

x =  np.random.uniform(0,L, size = (int(N), 3))                     # Position vector, fill in uniform distribution in all 3 dimensions
v =  np.random.normal(my,sigma, size = (int(N), 3))                 # Velocity vector, fill in correct distribution
        

time = np.linspace(0,10**-9,1000)                       #Simulation Runtime in Seconds
steps = np.linspace(0,10**-12,1000)                     #Number of Steps Taken in Simulation
steps=1001
dt=10**-12                                              #Simulation Step Length in Seconds
P=np.random.uniform(0,N, size = (int(N), 1)) 
#ac=np.random.uniform(0,N, size = (int(N), 1)) 
#ve=np.random.uniform(0,N, size = (int(N), 1)) 
#xa=np.random.uniform(0,N, size = (int(N), 1))

for i in range(0,int(steps)):
    '''
    Simulerer partikkel bevegelse ved bruk av euler metoden.
    '''
    x += v*dt


    for j in range(int(N)):

        '''
        Partikklene kolliderer med vegg.
        '''
        
        if (x[j,0]>=L or x[j,0]<=0): #Snur hastigheten i x retning
            v[j,0] *= -1
            
        if (x[j,1]>=L or x[j,1]<=0): #Snur hastigheten i y retning
            v[j,1] *= -1

        if (x[j,2]>=L or x[j,2]<=0): #Snur hastigheten i z retning
            v[j,2] *= -1

        '''
        Partikklene treffer det firkantede hullet i bunnen.
        Hullets dimensjoner er 1/4*L og 3/4L i x og y retning.
        '''

        if x[j,2]<=0 and (x[j,0]<3/4*L and x[j,0]>1/4*L) and (x[j,1]<3/4*L and x[j,1]>1/4*L): #Hullet gir ny kordinat z=L.
            x[j,2] += L
            
            '''
            Vi finner antall utgående partikler og tapt bevegelsesmengde.
            '''
            Escape+=1    #Finner alle utgående partikler.
            P+=m*v[j,2]  #Finner bevegelsesmengde.

            


            FUELMASS=(Escape*m)  #Finner total masse til utgående partikler. Massetap tilsvarer drivstoff forbruket.

            '''
            Finn hastigheten til raketten basert pg drivstoff forbruket.
            '''

'''
Vi finner hastigheten ut ifra kraften til hver partikkel.
'''

F=P/(10**-9) #Kraften er lik bevegelsesmengde delt på tiden.

for j in range(int(N)):
    FUELMASS-=m

    #a=F[0]/FUELMASS
    print(FUELMASS)
    #a=F[j]/FUELMASS[j]
    #print(FUELMASS)
    
    

'''
Vi velger en superposisjon av 10**12 mindre rakettmotorer. ##############################################
'''

#Drivstoff mot hastighet.            


            #Kan ikke bruke Euler chromer.


#Lag et array som du kan bruke p[ utsiden.
#for i in range(len(time-1)):
#    a[i+1]=F/m
#    v[i+1]=v[i]+a[i+1]*dt
#    x[i+1]=x[i]+v[i+1]*dt

#    m-=Escape



            


            

            










#print(Escape*m)


#Tapt Bevegelsesmengde.
#Bevegelsesmengden g[r ut ifra z komponenten til hastigheten s[ raketten skytes rett oppover.
#tapt bevegelsesmengde.

#Drivstoff
#Drivstoff forbruk er bare Antall unslippede partikler (Escape) * massen. 
# Drivstoff per tidsenhet. Deler p[ 10**-9 for [ finne kg/s.

#Kraft
#Total kraft er F=P/v