# Laura Ocampo, Isaac Pliskin, Luis Argueta, Zixi Zhang, Phillip Cho
# Physics 165 Lab 2
# The one with the random walks
from numpy.random import random as rng
import numpy as np
import matplotlib.pyplot as plt

def Random_Walk(steps):
    x = np.zeros(number_steps)
    y = np.zeros(number_steps)
    x_samples = rng(number_steps)
    y_samples = rng(number_steps)

    x_sum = 0
    y_sum = 0

    for i in range(1, number_steps):
        if x_samples[i] < 0.5:
            x[i] = x[i - 1] + 1
            x_sum += 1
        else:
            x[i] = x[i - 1] - 1
            x_sum -= 1

        if y_samples[i] < 0.5:
            y[i] = y[i - 1] + 1
            y_sum += 1
        else:
            y[i] = y[i - 1] - 1
            y_sum -= 1

    

    distance = np.sqrt(x_sum**2 + y_sum**2)

    return x, y, distance


number_steps = 1000

# Begin Assignment 1

# Part 1.a.
# One single random walk
plt.figure('Part 1.a.')

x1a, y1a, d1b = Random_Walk(number_steps)

print("Displacement for Part 1.a. is: ", d1b)

plt.plot(x1a, y1a, '--')
plt.plot(x1a[-1], y1a[-1], 'ro')
plt.axis('equal')
plt.title('Assignment 1 Part a')
plt.xlabel('x values')
plt.ylabel('y values')
plt.show(block=False)

# Part 1.b.
# Four walks
d1b = []
x1b = []
y1b = []
# f = plt.figure('Part 1.b.')
for i in range(0, 4):
    x, y, d = Random_Walk(1000)
    d1b.append(d)
    x1b.append(x)
    y1b.append(y)

f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
f.canvas.set_window_title('Part 1.b.') 
plt.title('Assignment 1 Part b')
plt.xlabel('x values')
plt.ylabel('y values')

ax1.plot(x1b[0], y1b[0], 'b--')
ax1.plot(x1b[0][-1], y1b[0][-1], 'ro')
ax1.set_title('Part 1.b. Walk 1')
ax1.set_xlabel('x values')
ax1.set_ylabel('y values')

ax2.plot(x1b[1], y1b[1], 'y--')
ax2.plot(x1b[1][-1], y1b[1][-1], 'ro')
ax2.set_title('Part 1.b. Walk 2')
ax2.set_xlabel('x values')
ax2.set_ylabel('y values')

ax3.plot(x1b[2], y1b[2], 'r--')
ax3.plot(x1b[2][-1], y1b[2][-1], 'bo')
ax3.set_title('Part 1.b. Walk 3')
ax3.set_xlabel('x values')
ax3.set_ylabel('y values')

ax4.plot(x1b[3], y1b[3], 'g--')
ax4.plot(x1b[3][-1], y1b[3][-1], 'ro')
ax4.set_title('Part 1.b. Walk 4')
ax4.set_xlabel('x values')
ax4.set_ylabel('y values')

print("The displacements for the four walks are: ", d1b)

plt.axis('equal')
plt.show(block=False)

# Begin Assignment 2

# Part 2.a
x_final = []
y_final = []
x2a = []
y2a = []
d2a = []
number_runs = 1000

for i in range(0, number_runs):
    x, y, d = Random_Walk(number_steps)
    x2a.append(x)
    y2a.append(y)
    d2a.append(d)

    x_final.append(x[-1])
    y_final.append(y[-1])

plt.figure('Part 2.a. Paths')
for i in range(0, number_runs):
    plt.plot(x2a[i], y2a[i])

plt.axis('equal')
plt.title('Paths for 1000 Random Walks')
plt.xlabel('x values')
plt.ylabel('y values')
plt.show(block=False)

plt.figure('Part 2.a. Final Positions')
plt.scatter(x_final, y_final, color='green')

plt.axis('equal')
plt.title('Final Positions for 1000 Random Walks')
plt.xlabel('final x values')
plt.ylabel('final y values')
plt.show(block=False)

# Part 2.b.
# Plot stuff as a histogram
# Or something

plt.figure('Part 2.b. First Histogram')
plt.hist(d2a)
plt.title('Histogram of Displacements for 1000 Walks')
plt.xlabel('Displacement')
plt.ylabel('Frequency')
plt.show(block=False)

# Part 2.c.
d2asquared = [i**2 for i in d2a]

plt.figure('Part 2.c. Second Histogram')
plt.hist(d2asquared)
plt.title('Histogram of Displacements Squared for 1000 Walks')
plt.xlabel('Displacement Squared')
plt.ylabel('Frequency')
plt.show(block=False)

# Part 2.d.

plt.figure('Part 2.d. semilogy')
plt.hist(d2asquared)
plt.yscale('log', nonposy='clip')
plt.title('Histogram with y axis as logarithmic')
plt.xlabel('Displacement Squared')
plt.ylabel('Frequency')
plt.show(block=False)

plt.figure('Part 2.d. semilogx')
plt.hist(d2asquared)
plt.xscale('log', nonposy='clip')
plt.title('Histogram with x axis as logarithmic')
plt.xlabel('Displacement Squared')
plt.ylabel('Frequency')
plt.show(block=False)

plt.figure('Part 2.d. loglog')
plt.hist(d2asquared)
plt.yscale('log', nonposy='clip')
plt.xscale('log', nonposy='clip')
plt.title('Histogram with x and y axis as logarithmic')
plt.xlabel('Displacement Squared')
plt.ylabel('Frequency')
plt.show(block=False)

# Part 2.e.
d2asquarededmean = np.mean(d2asquared)
print("The mean-squared displacement for 1000 steps is: ", d2asquarededmean)

# Part 2.f.
x_final_f = []
y_final_f = []
x2f = []
y2f = []
d2f = []
number_runs = 1000

for i in range(0, number_runs):
    x, y, d = Random_Walk(number_steps * 4)
    x2f.append(x)
    y2f.append(y)
    d2f.append(d)

    x_final_f.append(x[-1])
    y_final_f.append(y[-1])

plt.figure('Part 2.f. Paths')
for i in range(0, number_runs):
    plt.plot(x2f[i], y2f[i])

plt.axis('equal')
plt.title('Paths for 1000 Random Walks with 4000 Steps')
plt.xlabel('x values')
plt.ylabel('y values')
plt.show(block=False)

plt.figure('Part 2.f. Final Positions')
plt.scatter(x_final_f, y_final_f, color='green')

plt.axis('equal')
plt.title('Final Positions for 1000 Random Walks')
plt.xlabel('final x values')
plt.ylabel('final y values')
plt.show(block=False)

d2fsquared = [i**2 for i in d2f]
d2fsquaredmean = np.mean(d2fsquared)
print("The mean-squared displacement for 4000 steps is: ", d2fsquaredmean)

plt.show()