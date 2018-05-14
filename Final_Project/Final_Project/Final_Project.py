import numpy as np, matplotlib.pyplot as plt

G = 6.674e-11
M_e = 5.9722e+24
p_o = 101325
L = 0.0065
T_o = 288.15
M = 0.0289644
R = 8.31447
C_d = 0.47
y_s = np.sqrt((G*M_e)/9.80665)
rho_o = 1.225

# def P(g, h):
#     exponent = (g*M)/(R*L)
#     inside = (1 - ((L*h)/T_o))
#     temp = inside**exponent
#     p = p_o*(temp)
#     T = T_o - L*h
#     rho = (p*M)/(R*T)
#     return rho

def F(y_o, v_o, a_o, m, r, dt):
    A = np.pi*(r**2)

    V = (4/3)*np.pi*(r**3)
    density = m/V
    print('r = ', r, 'density = ', density)

    a = a_o
    v = v_o
    y = y_o
    h = y_s + y

    t = 0
    times = []
    velocities = []
    positions = []
    accelerations = []

    while y >= 0:
        times.append(t)
        velocities.append(v)
        positions.append(y)
        h = y + y_s
        g = (G*M_e)/(h**2)
        # rho = P(g,y)
        a = g - C_d*(rho_o/m)*A*(v**2)*dt
        accelerations.append(a)
        y = y - v*dt
        v = v+a*dt
        t = t + dt
    print('g = ', g)
    E = (1/2)*m*(v**2)

    return positions, velocities, accelerations, times, E, density

ys = []
vs = []
az = []
ts = []
Es = []

iteration = 0
for m in range(10, 260, 10):
    iteration += 1
    drho = (22587 - 534)/25
    print('mass is: ', m)
    for rho in np.arange(drho, 22587+drho, drho):
        iteration += 1
        print('density is: ', rho)
        for y_o in range(1000, 26000, 1000):
            iteration += 1
            percent = iteration / 15625
            print('iteration: ', iteration, ' which is ', percent*100, '% done.')
            r = ((3*m)/(rho*np.pi))**(1/3)
            print('starting height is: ', y_o)
            y, v, a, t, E, d= F(y_o, 0, 0, m, r, 0.01)
            ys.append([t, y])
            vs.append([t, v])
            az.append([t, a])
            Es.append([rho, m, y_o, E])
            print('m = ', m, ' E = ', E)

plt.figure('Densities')
for E in Es:
    plt.plot(E[0], E[3], marker='o')
energy = 2257000
plt.axhline(energy)
plt.grid()
plt.title('Energy vs Density')
plt.xlabel('Density (kg/m^3)')
plt.ylabel('Energy (J)')
plt.savefig('Densities.png', dpi=350)

plt.figure('Masses')
for E in Es:
    plt.plot(E[1], E[3], marker='o')
energy = 2257000
plt.axhline(energy)
plt.grid()
plt.title('Energy vs Mass')
plt.xlabel('Mass (kg)')
plt.ylabel('Energy, (J)')
plt.savefig('Masses.png', dpi=350)

plt.figure('Heights')
for E in Es:
    plt.plot(E[2], E[3], marker='o')
energy = 2257000
plt.axhline(energy)
plt.grid()
plt.title('Energy vs Starting Height')
plt.xlabel('Starting Height (m)')
plt.ylabel('Energy, (J)')
plt.savefig('Heights.png', dpi=350)

plt.figure('Positions')
for y in ys:
    plt.plot(y[0], y[1])
plt.grid()
plt.title('Position vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.savefig('Positions.png', dpi=350)

plt.figure('Velocities')
for v in vs:
    plt.plot(v[0], v[1])
plt.grid()
plt.title('Velocity vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.savefig('Velocities.png', dpi=350)

plt.figure('Accelerations')
for a in az:
    plt.plot(a[0], a[1])
plt.grid()
plt.title('Acceleration vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s^2)')
plt.savefig('Accelerations.png', dpi=350)

rho_w = 1000
H = 2257000
Vs = []

for E in Es:
    m = E[3] * H
    V = m/rho_w
    Vs.append([E[1], V])

plt.figure('Volumes')
for V in Vs:
    plt.plot(V[0], V[1], marker='o')

volume = 23600000000000/rho_w
plt.axhline(volume)

plt.grid()
plt.title('Object Mass vs. Lake Volume')
plt.xlabel('Object Mass (kg)')
plt.ylabel('Lake Volume (m^3)')
plt.savefig('Volumes.png', dpi=350)

plt.show()