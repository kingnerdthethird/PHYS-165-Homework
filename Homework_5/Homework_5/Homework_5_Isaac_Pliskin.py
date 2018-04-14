# Homework 5 for PHYS165 by Isaac Pliskin
# Due Monday, March 26th, 2018

import numpy as np, matplotlib.pyplot as plt # to draw stuff and do the maths
from scipy.integrate import odeint # for integrgating stuff 

from simple_oscillator import F # for testing stuff

t_min = 0 # minimum t value
t_max = 25 # maximum t value
# Most of the transients die out by now but if I go further then it looks ugly
dt = 0.1 # time step value

t = np.arange(t_min, t_max + dt, dt) # create a range of t values for all parts below

init_conditions = [(1., 0.), (0., 1.)] # initial conditions for all parts

# Testing stuff
plt.figure("Testing Stuff for Funsies") # create a figure to test stuff

for y0 in init_conditions: # should run twice
    y = odeint(F, y0, t) # this just intgrates the values
    plt.plot(t, y[:, 0], linewidth = 2) # plot y

skip = 5 # skip 5 points
t_test = t[::skip] # create a testing time interval

plt.plot(t_test, np.cos(t_test), 'bo') # plot random test points for y(0) = 1
plt.plot(t_test, np.sin(t_test), 'go') # plot random test points for y(0) = 0

# stuff to label the graph:
michael_scott = plt.gca()
michael_scott.set_title("Undriven with w = 1", fontsize = 24)
michael_scott.set_xlabel("t values")
michael_scott.set_ylabel("y values")

plt.show(block=False) # show graph but continue code

# Part a. 
plt.figure("Part a") # figure for different frequency stuff 

def G(y, t): # function for different frequencies
    # I couldn't figure out how to do this in a different file and vary w
    # If I hadn't done it on a bumpy plane ride at 6AM I probably could have figured it out
    dy = [0, 0] # create a list of zeros
    dy[0] = y[1] # the first value of the derivative is the second value of the position
    dy[1] = -(w**2)*y[0] # this comes from D2y-w^2y=0
    return dy # return dy

for y0 in init_conditions: # should run twice
    for w in range(1, 4): # should run thrice (will plot six things)
        y = odeint(G, y0, t) # integrate G over t
        plt.plot(t, y[:, 0], linewidth = 2) # plot y

for w in range(1, 4): # will run three times, giving six graphs
    plt.plot(t_test, np.cos(t_test * w), 'bo') # plot for y(0) = 1
    plt.plot(t_test, np.sin(t_test * w) / w, 'go') # plot for y'(0) = 1 (hence the /w)

# aesthetic stuff
michael_scott = plt.gca()
michael_scott.set_title("Undriven with w = 1, 2, 3", fontsize = 24)
michael_scott.set_xlabel("t values")
michael_scott.set_ylabel("y values")

plt.show(block=False) # show graph continue code

# Part b.
dt = 0.01 # time step value
# I increase the time step so that it will look nicer

t = np.arange(t_min, t_max + dt, dt) # recreate a range of t values for all parts below with new dt

init_conditions = [(1., 0.), (0., 1.)] # initial conditions for all parts
plt.figure("Part b") # graph for driven oscillators

a = 5 # amplitude, randomly chosen
w_o = 7 # natural frequency

def H(y, t): # fucntion to do driven stuff
    # see the definition for G for why this isn't in a different file
    dy = [0, 0] # empty list
    dy[0] = y[1] # steal a value
    dy[1] = -(w_o**2)*y[0]-a*np.sin(w*t) # comes from y'' + (w_o)^2 y = asin(wt)
    return dy # return dy

for y0 in init_conditions: # should run twice
    for w in np.arange(w_o - 2, w_o + 4, 2): # should run thrice, giving six graphs
        y = odeint(H, y0, t) # integrate
        plt.plot(t, y[:, 0], linewidth = 2) # plot

# make it all look professional
# test points are not plotted cause python didn't like to do it
# You can see when w = w_o the plot increases forever
michael_scott = plt.gca()
michael_scott.set_title("Driven with w = w_o - 2, w_o, w_o + 2", fontsize = 24)
michael_scott.set_xlabel("t values")
michael_scott.set_ylabel("y values")

plt.show(block=False) # show graph, continue code

# Part c.
plt.figure("Part c") # graph for amplitude vs frequency

def x_o(w): # function for amplitude
    # x_o = ((w_o^2)*a)/[((w_o^2)-(w^2))^2 + (r^2)(w^2)]^1/2
    # however, it is undamped so r = 0 and
    # x_o = ((w_o^2)*a)/((w_o^2)-(w^2))
    x = ((w_o**2) * a) / ((w_o**2) - (w**2)) # do the above stuff
    return x # return amplitudes

for w in np.arange(1, 25, 1): # will run 20 times, skipping 3 because if w_o = w, you get divide by zero
    if w != w_o: # make sure it isn't at resonance
        plt.scatter(w, x_o(w)) # plot points

plt.axvline(w_o, linestyle='--') # plot an asymptote at the natural frequency
# fancy stuff
michael_scott = plt.gca()
michael_scott.set_title("Amplitude vs. Drive Frequency (w =/= w_o because of divide by zero)", fontsize = 24)
michael_scott.set_xlabel("drive frequency values")
michael_scott.set_ylabel("amplitude values")

plt.show() # final show