#rand_movie.py
#Simulates a 2D Random Walk
import matplotlib.pyplot as plt
from matplotlib import animation
from numpy.random import random as rand
#Set number of steps for each random walk
num_steps = 100
#Create an empty ﬁgure of the desired size
plt.close('all')    #Clear everything you have from prior runs
bound = 20          
ﬁg = plt.ﬁgure()  #Must have ﬁgure object for movie
ax = plt.axes(xlim=(-bound, bound), ylim=(-bound, bound)) 
#Create empty line and point objects with no data
#They will be updated during weach frame of the animation
(my_line), = ax.plot([], [], lw=2)           #Line to show path
(my_point), = ax.plot([], [], 'ro', ms=9)    #Dot to show current position
#Generate the random walk data
x_steps = 2 * (rand(num_steps) < 0.5) - 1   #Generate randoms steps +/-1
y_steps = 2 * (rand(num_steps) < 0.5) - 1
x_coordinate = x_steps.cumsum()            #Sum steps to get position
y_coordinate = y_steps.cumsum()
#This function will generate each frame of the animation.
#It adds all of the data through frame n to line
#and it moves a point to the nth position of the walk
def get_step(n, x, y, this_line, this_point):
    this_line.set_data(x[:n+1], y[:n+1])
    this_point.set_data(x[n], y[n])
    
#Call the animator and create the movie
my_movie = animation.FuncAnimation(ﬁg, get_step, frames=num_steps, \
                                   fargs=(x_coordinate, y_coordinate, my_line, my_point))
#projectile.py
#Simulates Projectile Motion
import matplotlib.pyplot as plt
from matplotlib import animation
ﬁg=plt.ﬁgure()
ax1=ﬁg.add_subplot(111)
#ax2=ﬁg.add_subplot(211,projection='3d')
#ax3=ﬁg.add_subplot(1,1,1)
dt=0
vx=25
vy=20
x=0

y=10
def animate(i):
    global dt
    global vx
    global vy
    global x
    global y
    vy=-9.8*dt+vy
    x=vx*dt+x
    y=vy*dt+y
    dt=dt+0.005
    ax1.set_xlim([-1, 100])
    ax1.set_ylim([0, 50])
    ax1.scatter(x,y,s=70,c="r")
    
ani=animation.FuncAnimation(ﬁg,animate,interval=20)
plt.show()
#emwave.py
#ElectroMagnetic Wave Simulation
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
ax1=ﬁg.add_subplot(111,projection='3d')
#ax2=ﬁg.add_subplot(211,projection='3d')
#ax3=ﬁg.add_subplot(1,1,1)
x=np.linspace(0,5,200)
dt=0
yy=[]
zz=[]

def animate(i):
    zero=np.zeros(200)
    #dont change these two line
    global dt
    global x
    yy=np.cos(-x+dt)
    zz=np.cos(-x+dt)
    dt=dt+0.05
    ax1.clear()
    ax1.set_xlim([-1, 10])
    ax1.set_ylim([-1.2, 1.2])
    ax1.plot(x,yy,zero,c="r")
    ax1.plot(x,zero,zz,c="b")
ani=animation.FuncAnimation(ﬁg,animate,interval=100)
plt.show()

#coupled_masses.py
#Simulation of Coupled Masses connected by a spring
import matplotlib.pyplot as plt
from matplotlib import animation
m1=1.5
m2=1
k=0.8
dt=0.1
x1=0.1
v1=0.1
x2=0.7
v2=0
y=0
ﬁg=plt.ﬁgure()
ax1=ﬁg.add_subplot(1,1,1)
ax2=ﬁg.add_subplot(1,1,1)

def animate(i):
    global m1
    global m2
    global k
    global dt
    global x1
    global v1
    global x2
    global v2
    global y
    f1=-k*(x1-0.3)+(k*((x2-x1)-0.4))
    f2=-k*(x2-0.7)+(-k*((x2-x1)-0.4))
    v1=v1+(f1/m1)*dt
    v2=v2+(f2/m2)*dt
    x1=x1+v1*dt
    x2=x2+v2*dt
    ax1.clear()
    ax1.set_xlim(0,1.0)
    ax1.set_ylim(-0.1,0.11)
    ax1.scatter(x1,y,s=60)
    ax2.scatter(x2,y,s=60)
    
ani=animation.FuncAnimation(ﬁg,animate,interval=0.1)
plt.show()
