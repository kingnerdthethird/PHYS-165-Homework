import numpy as np, matplotlib.pyplot as plt # to draw stuff and do the maths
from scipy.integrate import odeint # for integrgating stuff

def phi_prime(t, I):
    return (I - np.sin(t))

t_min = -np.pi # minimum t value
t_max = np.pi # maximum t value
# Most of the transients die out by now but if I go further then it looks ugly
dt = 0.1 # time step value

t = np.arange(t_min, t_max + dt, dt) # create a range of t values for all parts below

y = odeint(phi_prime, )