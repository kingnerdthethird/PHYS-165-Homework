#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 20:02:02 2018

@author: largueta
"""
import numpy as np, matplotlib.pyplot as plt
from scipy.integrate import odeint

def F(y, t, I):
    # this is the derivative of phi with respect to tau
    dydt = I - np.sin(y)
    return dydt

t = np.arange(0, 50, 0.1)


plt.figure()

# plot a lot cause they look so cool
for I in np.arange(-2, 2, 0.02):
    # I is the ratio of I/I_c
    y = odeint(F, I, t, args=(I,))
    plt.plot(t, y)
    # it looks so cooooooooool
    # even if it's wrong
    
plt.title('Plot of phi(t)')
plt.xlabel('t')
plt.ylabel('phi(t)')

plt.show(block=False)

# see the write up for the math behind this
def V(R, I, I_c):
    return R*np.sqrt(I*I_c - (I_c**2))

I = np.arange(0, 10, 0.1)
plt.figure()
for R in range(1, 6):
    for I_c in range(1, 6):
        y = V(R, I, I_c)
        plt.plot(I, y)

plt.title('Voltage vs Current')
plt.xlabel('current')
plt.ylabel('voltage')
plt.show()