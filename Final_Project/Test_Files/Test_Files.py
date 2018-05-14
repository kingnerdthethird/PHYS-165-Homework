import numpy as np, matplotlib.pyplot as plt

G = 6.674e-11
M_e = 5.9722e+24
p_o = 101.325
L = 0.0065
T_o = 288.15
M = 0.0289644
R = 8.31447
C_d = 0.47
y_s = np.sqrt((G*M_e)/9.80665)
rho_o = 1.225

g = (G*M_e)/(y_s**2)
print(g)

exponent = (g*M)/(R*L)
inside = (1 - ((L*0)/T_o))
p = p_o*(inside**exponent)
print(p)
T = T_o - L*0
rho = (p*M)/(R*T)
print(rho)