import numpy as np, matplotlib.pyplot as plt

# constants for the simulation
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
rho_w = 1000
H = 2257000
volume = 23600000000000/rho_w

def P(g, h):
    # this function finds the density of air as a function of height
    # see the pdf file for the equation
    exponent = (g*M)/(R*L)
    inside = (1 - ((L*h)/T_o))
    temp = inside**exponent
    p = p_o*(temp)
    T = T_o - L*h
    rho = (p*M)/(R*T)
    return rho

def F(y_o, v_o, a_o, m, r, dt):
    # this function uses basic integration methods to integrate the functions.
    
    # here I calculate the needed constants of the object
    # I also recalculate the density of the object because I had some problems with this earlier
    A = np.pi*(r**2)

    V = (4/3)*np.pi*(r**3)
    density = m/V
    print('r = ', r, 'density = ', density)

    # retrieve the intial conditions
    a = a_o
    v = v_o
    y = y_o
    h = y_s + y

    # set up the lists needed for the integration
    t = 0
    times = []
    velocities = []
    positions = []
    accelerations = []

    while y >= 0:
        # this does basic integration
        # it runs until the object makes contact with the lake
        times.append(t)
        velocities.append(v)
        positions.append(y)
        h = y + y_s
        g = (G*M_e)/(h**2)
        rho = P(g,y)
        # to add variable air pressure, switch rho_o to rho
        a = g - C_d*(rho_o/m)*A*(v**2)*dt
        accelerations.append(a)
        y = y - v*dt
        v = v+a*dt
        t = t + dt
    print('g = ', g)
    # energy is pretty simple to calculate
    E = (1/2)*m*(v**2)

    # I return a lot of information
    return positions, velocities, accelerations, times, E, density

# these are the lists for the plots
# I had to use az since as is taken and it makes me feel ridiculous
ys = []
vs = []
az = []
ts = []
Es = []

for m in range(10, 110, 10):
    # there are ten values of mass used
    drho = (22587 - 534)/10
    print('mass is: ', m)
    for rho in np.arange(drho, 22587+drho, drho):
        # there are ten values of density used
        print('density is: ', rho)
        for y_o in range(1000, 28500, 2500):
            # there are ten values of y_o used
            # r is used to calculate the radius of a sphere with density and mass given above. 
            r = ((3*m)/(4*rho*np.pi))**(1/3)
            print('starting height is: ', y_o)
            y, v, a, t, E, d= F(y_o, 0, 0, m, r, 0.01)
            ys.append([t, y])
            vs.append([t, v])
            az.append([t, a])
            Es.append([rho, m, y_o, E])
            print('m = ', m, ' E = ', E)

# below I plot all the information.
# I believe most of it is self explanatory
plt.figure('Densities')
for E in Es:
    plt.plot(E[0], E[3], marker='o')
plt.axhline(H)
plt.grid()
plt.title('Energy vs Density')
plt.xlabel('Density (kg/m^3)')
plt.ylabel('Energy (J)')
plt.savefig('Densities.png', dpi=350)

plt.figure('Masses')
for E in Es:
    plt.plot(E[1], E[3], marker='o')
plt.axhline(H)
plt.grid()
plt.title('Energy vs Mass')
plt.xlabel('Mass (kg)')
plt.ylabel('Energy, (J)')
plt.savefig('Masses.png', dpi=350)

plt.figure('Heights')
for E in Es:
    plt.plot(E[2], E[3], marker='o')
plt.axhline(H)
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


Vs = []

# here I calculate the volumes of lakes vaporized.
for E in Es:
    m = E[3] * H
    V = m/rho_w
    Vs.append([E[1], V])

plt.figure('Volumes')
for V in Vs:
    plt.plot(V[0], V[1], marker='o')
plt.axhline(volume)
plt.grid()
plt.title('Object Mass vs. Lake Volume')
plt.xlabel('Object Mass (kg)')
plt.ylabel('Lake Volume (m^3)')
plt.savefig('Volumes.png', dpi=350)

plt.show()