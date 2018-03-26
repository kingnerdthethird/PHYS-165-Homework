# Homework 5 for PHYS165 by Isaac Pliskin
# Due Monday, March 26th, 2018

import numpy as np, matplotlib.pyplot as plt
from scipy.integrate import odeint

from simple_oscillator import F

t_min = 0
t_max = 10
dt = 0.1

t = np.arange(t_min, t_max + dt, dt)

init_conditions = [(1., 0.), (0., 1.)]

# Testing stuff
plt.figure()

for y0 in init_conditions:
    y = odeint(F, y0, t)
    plt.plot(t, y[:, 0], linewidth = 2)

skip = 5
t_test = t[::skip]

plt.plot(t_test, np.cos(t_test), 'bo')
plt.plot(t_test, np.sin(t_test), 'go')

michael_scott = plt.gca()
michael_scott.set_title("Undriven with w = 1", fontsize = 24)
michael_scott.set_xlabel("t values")
michael_scott.set_ylabel("y values")

plt.show(block=False)

# Part a. 
plt.figure()

def G(y, t):
    dy = [0, 0]
    dy[0] = y[1]
    dy[1] = -(w**2)*y[0]
    return dy

for y0 in init_conditions:
    for w in range(1, 4):
        y = odeint(G, y0, t)
        plt.plot(t, y[:, 0], linewidth = 2)

skip = 5
t_test = t[::skip]

for w in range(1, 4):
    plt.plot(t_test, np.cos(t_test * w), 'bo')
    plt.plot(t_test, np.sin(t_test * w) / w, 'go')

michael_scott = plt.gca()
michael_scott.set_title("Undriven with w = 1, 2, 3", fontsize = 24)
michael_scott.set_xlabel("t values")
michael_scott.set_ylabel("y values")

plt.show(block=False)

# Part b.
plt.figure()

a = 5
w_o = 3

def H(y, t):
    dy = [0, 0]
    dy[0] = y[1]
    dy[1] = -(w_o**2)*y[0]-a*np.sin(w*t)
    return dy

for y0 in init_conditions:
    for w in np.arange(1, 7, 2):
        y = odeint(H, y0, t)
        plt.plot(t, y[:, 0], linewidth = 2)

michael_scott = plt.gca()
michael_scott.set_title("Driven with w = 1, 3, 5", fontsize = 24)
michael_scott.set_xlabel("t values")
michael_scott.set_ylabel("y values")

plt.show(block=False)

# Part c.
plt.figure()
def x_o(w):
    x = ((w_o**2) * a) / ((w_o**2) - (w**2))
    return x

for w in np.arange(1, 25, 2):
    if w != 3:
        plt.scatter(w, x_o(w))

michael_scott = plt.gca()
michael_scott.set_title("Amplitude vs. Drive Frequency (w =/= 3 because of divide by zero)", fontsize = 24)
michael_scott.set_xlabel("drive frequency values")
michael_scott.set_ylabel("amplitude values")

plt.show()