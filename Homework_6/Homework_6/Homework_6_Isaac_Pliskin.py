# Homework 6 Physics 165 by Isaac Pliskin
import numpy as np
from cmath import exp, pi
from scipy.fftpack import fft
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
import csv
import scipy.ndimage as sim

def DFT(y):
    # DFT : discrete Fourier Tranform
    N = len(y)
    c = np.zeros(N//2+1, complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*exp(-2j*pi*k*n/N)
            # for real symmetric y, use c[k] = y[n]*cos(2*pi*k*n/N)

    return c

# Problem 1.a.
number_points = 1024
T = 1./1000.
x = np.linspace(0., number_points*T, number_points) # x values for y
y = np.sin(50.*2.*np.pi*x) + np.sin(100.*2.*np.pi*x) # y

# do a discrete fourier transform and time it
dft_initial = time.time()
ydft = DFT(y)
dft_time = time.time() - dft_initial

# do a fast fourier transform and time it
# I keep getting 0 seconds. However, if I add in a for loop that I know will take a long time, it is no longer 0
# Therefore, I must conclude that the fast fourier transform method is real fast
fft_initial = time.time()
yfft = fft(y)
fft_time = time.time() - fft_initial

# this is the x values for the fourier transform
xfft = np.linspace(0., 1./(2.*T), number_points//2)

# plot the results of the fast fourier transform
plt.figure('Fast Fourier Transform Method')
plt.plot(xfft, 2./number_points*np.abs(yfft[0:number_points//2]))
plt.grid()
plt.title('Fast Fourier Transform Method')
plt.xlabel('frequency')
plt.ylabel('amplitude')
plt.show(block=False)

# plot the results of the discrete fourier transform
plt.figure('Discrete Fourier Transform Method')
plt.plot(xfft, 2./number_points*np.abs(ydft[0:number_points//2]))
plt.grid()
plt.title('Discrete Fourier Transform Method')
plt.xlabel('frequency')
plt.ylabel('amplitude')
plt.show(block=False)

# Problem 1.b. 
# analysis of the differences
print("I can't really tell much difference looking at the graphs.") 
print("The Discrete Transform Method took ", dft_time, " seconds.")
print("The Fast Fourier Transform Method took ", fft_time, " seconds.")
print("The difference was: ", dft_time - fft_time, " seconds.")

# I wanted to cover all my bases
if dft_time > fft_time:
    print("The Discrete Fast Fourier Transform Method was slower by ", dft_time - fft_time, " seconds.")
elif fft_time > dft_time:
    print("The Fast Fourier Transform Method was slower by ", fft_time - dft_time, " seconds.")
elif fft_time == dft_time:
    print("They took the same amount of time.")

print("Other than that, there does not seem to be much of a difference.")

# Problem 1.c.
# set up the basic plot
t = np.arange(0, 50)
plt.figure('Function to be Windowed')
plt.plot(x, y)
plt.show(block=False)

# create and apply the hanning window, then find a fourier transform
window = np.hanning(50)
windowed_fft = fft(y[0:50] * window)

# plot the function with and without the hanning window applied
plt.figure('Hanning Window Comparison')
plt.plot(t, window*y[0:50])
plt.plot(t, y[0:50])
plt.title('y with Hanning Window vs y without')
plt.xlabel('t')
plt.ylabel('y')
plt.show(block=False)

# plot the fourier transform of the function with a hanning window
plt.figure('Hanning Window')
plt.grid()
plt.plot(xfft[0:50], 2./100*np.abs(windowed_fft[0:100//2]))
plt.title('Hanning Window Frequencies for y')
plt.xlabel('frequency')
plt.ylabel('amplitude')
plt.show(block=False)

# create and apply the blackman window, then find a fourier transform
new_window = np.blackman(50)
new_windowed_fft = fft(y[0:50] * new_window)

# plot the function with and without the blackman window applied
plt.figure('Blackman Window Comparison')
plt.plot(t, new_window*y[0:50])
plt.plot(t, y[0:50])
plt.title('y with Blackman Window vs y without')
plt.xlabel('t')
plt.ylabel('y')
plt.show(block=False)

# plot the fourier transform of the blackman windowed function
plt.figure('Blackman Window')
plt.grid()
plt.plot(xfft[0:50], 2./100*np.abs(new_windowed_fft[0:100//2]))
plt.title('Blackman Window Frequencies for y')
plt.xlabel('frequency')
plt.ylabel('amplitude')
plt.show(block=False)

# Problem 2.a.
data = np.loadtxt("Fibers.csv", delimiter=',') # get the image
# shift the values so they are between 0 and 255 and then switch to uint8
minimum_value = np.min(data)
data -= minimum_value
maximum_value = np.max(data)
alpha = 255 / maximum_value
data *= alpha
data = data.astype('uint8')

# plot the image
plt.figure('Shifted Image')
plt.imshow(data, cmap = plt.cm.gist_gray)
plt.title('Shifted Image')
plt.show(block=False)

# Problem 2.b.
# set up gauss filter
v = np.arange(-25, 26)
X, Y = np.meshgrid(v, v)
gauss_filter = np.exp(-0.5*(X**2/2 + Y**2/45))

# plot gauss filter
fig = plt.figure('Gaussian Filter')
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, gauss_filter)
plt.title('Gaussian Filter')
plt.show(block=False)

# Problem 2.c.
# set up combined filter
laplace_filter = np.array([ [0, -1, 0], [-1, 4, -1], [0, -1, 0] ])
combined_filter = sim.convolve(gauss_filter, laplace_filter)

# plot combined filter
fig = plt.figure('Combined Filter')
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, combined_filter)
plt.title('Combined Filter')
plt.show(block=False)

print('The Laplace filter adds in negative elements to the Gaussian filter.')

# Problem 2.d.
# apply combined filter
new_data = sim.convolve(data, combined_filter)

# plot image
plt.figure('Photo with Combined Filter')
plt.imshow(new_data, cmap = plt.cm.gist_gray)
plt.title('New Photo with Combined Filters')
plt.show(block=False)
print('The image seems to have a little bit too high contrast, but the fix provided by Dr. Williams doesn\'t seem to work so I think this is fine')

plt.show()