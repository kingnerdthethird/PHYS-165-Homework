import scipy.ndimage as sim
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy.misc
import copy

# Assignment 1
# For Assignment 1, see the write up

# Assignment 2
import scipy.ndimage as sim
from numpy import genfromtxt


impulse = np.zeros( (51, 51) )
impulse [25, 25] = 1.0 
myfilter = np.ones( (3, 3) ) / 9
response = sim.convolve(impulse, myfilter)
plt.figure()
plt.set_cmap('gray')
plt.imshow(response)
plt.title('Dot Filter Test')

plt.show(block=False)

cat = plt.imread('bwCat.tif')

plt.figure('Original Cat Photo')
plt.imshow(cat)
plt.title('Original Cat Photo')
plt.show(block=False)

# Part a
print(cat)
cat_1 = sim.convolve(cat, myfilter, mode='constant')

plt.figure('Cat Photo Using Convolve With Filter 1')
plt.imshow(cat_1)
plt.title('Cat Photo Using Convolve With Filter 1')
plt.show(block=False)
# the image is now more pixelated

cat_1_b = sim.uniform_filter(cat, mode='constant')
plt.figure('Cat Photo Using Uniform Filter')
plt.imshow(cat_1_b)
plt.title('Cat Photo Using Uniform Filter')
plt.show(block=False)
# still pixelated

# Part b
filter_2 = np.ones ( (15, 15) ) / 9
cat_2 = sim.convolve(cat, filter_2, mode='constant')
print(cat_2)
plt.figure('Cat Photo Using 15x15 Filter with 1/9 everywhere')
plt.imshow(cat_2)
plt.title('Cat Photo Using 15x15 Filter with 1/9 everywhere')
plt.show(block=False)
# this no longer looks like a cat, I think, but I'm no expert

# Part c

# Assignment 3
gauss_filter = genfromtxt('gaussfilter.csv', delimiter=',')
print(gauss_filter)
cat_3_g = sim.convolve(cat, gauss_filter)
plt.figure('Cat Photo Using Gaussian Filter')
plt.imshow(cat_3_g)
plt.title('Cat Photo Using Gaussian Filter')
plt.show(block=False)
# it now looks like when I try to take a photo of my cat, Mouse.

cat_3 = sim.gaussian_filter(cat, sigma=5)
plt.figure('Cat Photo Using Built In Gauss Filter')
plt.imshow(cat_3)
plt.title('Cat Photo Using Built In Gauss Filter')
plt.show(block=False)

gauss_dot = sim.convolve(impulse, gauss_filter)
plt.figure('Original Dot')
plt.imshow(response)
plt.title('Original Dot')
plt.show(block=False)

plt.figure('Gauss Dot')
plt.imshow(gauss_dot)
plt.title('Gauss Dot')
plt.show(block=False)
# Now it is a fuzzy dot

# Part c
new_cat_1 = scipy.misc.imresize(cat, 0.15, interp='cubic')

x_1, y_1 = np.mgrid[0:new_cat_1.shape[0], 0:new_cat_1.shape[1]]
fig = plt.figure('3D Original Cat')
ax = fig.gca(projection='3d')
ax.plot_surface(x_1, y_1, new_cat_1, rstride=1, cstride=1, cmap=plt.cm.gray, linewidth=0)
plt.title('3D Original Cat')
plt.show(block=False)

new_cat_2 = scipy.misc.imresize(cat_2, 0.15, interp='cubic')

x_2, y_2 = np.mgrid[0:new_cat_2.shape[0], 0:new_cat_2.shape[1]]
fig = plt.figure('3D Cat with 15x15 Square Filter with 1/9 Everywhere')
ax = fig.gca(projection='3d')
ax.plot_surface(x_2, y_2, new_cat_2, rstride=1, cstride=1, cmap=plt.cm.gray, linewidth=0)
plt.title('3D Cat with 15x15 Square Filter with 1/9 Everywhere')
plt.show(block=False)

new_cat_3 = scipy.misc.imresize(cat_3_g, 0.15, interp='cubic')

x_3, y_3 = np.mgrid[0:new_cat_3.shape[0], 0:new_cat_3.shape[1]]
fig = plt.figure('3D Cat with Gaussian Filter')
ax = fig.gca(projection='3d')
ax.plot_surface(x_3, y_3, new_cat_3, rstride=1, cstride=1, cmap=plt.cm.gray, linewidth=0)
plt.title('3D Cat with Gaussian Filter')
plt.show(block=False)

x_4, y_4 = np.mgrid[0:myfilter.shape[0], 0:myfilter.shape[1]]
fig = plt.figure('Small Square Filter')
ax = fig.gca(projection='3d')
ax.plot_surface(x_4, y_4, myfilter, rstride=1, cstride=1, cmap=plt.cm.gray, linewidth=0)
plt.title('Small Square Filter')
plt.show(block=False)

x_5, y_5 = np.mgrid[0:filter_2.shape[0], 0:filter_2.shape[1]]
fig = plt.figure('Large Square Filter')
ax = fig.gca(projection='3d')
ax.plot_surface(x_5, y_5, filter_2, rstride=1, cstride=1, cmap=plt.cm.gray, linewidth=0)
plt.title('Large Square Filter')
plt.show(block=False)

x_6, y_6 = np.mgrid[0:gauss_filter.shape[0], 0:gauss_filter.shape[1]]
fig = plt.figure('Gaussian Filter')
ax = fig.gca(projection='3d')
ax.plot_surface(x_6, y_6, gauss_filter, rstride=1, cstride=1, cmap=plt.cm.gray, linewidth=0)
plt.title('Gaussian Filter')
plt.show(block=False)

# You can see some very big differences here
# The square filter makes all the values smaller, but doesn't change the maximum
# The Gaussian seems to keep the shape but lower the maximum

# Assignment 4
print(cat)
print(cat_1)
random_cat = copy.deepcopy(cat)
for i in range(0, random_cat.shape[0]):
    for j in range(0, random_cat.shape[1]):
        random_cat[i][j] *= np.random.rand()

print(random_cat)
plt.figure('Noisy Random Cat')
plt.imshow(random_cat)
plt.title('Noisy Random Cat')
plt.show(block=False)

clean_cat = copy.deepcopy(random_cat)
minimum_value = np.amin(clean_cat)
maximum_value = np.amax(clean_cat)
coefficient = 255/maximum_value

print(minimum_value)
print(maximum_value)
print(coefficient)

for i in range(0, clean_cat.shape[0]):
    for j in range(0, clean_cat.shape[1]):
        clean_cat[i][j] -= minimum_value
        clean_cat[i][j] *= coefficient
        clean_cat[i][j] = clean_cat[i][j].astype('uint8')

print(random_cat)
print(clean_cat)
plt.figure('Clean Random Cat')
plt.imshow(clean_cat)
plt.title('Clean Random Cat')
plt.show(block=False)

# Part b
clean_cat_1 = sim.convolve(clean_cat, myfilter)
clean_cat_2 = sim.convolve(clean_cat, filter_2)
clean_cat_3 = sim.convolve(clean_cat, gauss_filter)

plt.figure('Clean Random Cat Small Filter')
plt.imshow(clean_cat_1)
plt.title('Clean Random Cat Small Filter')
plt.show(block=False)

plt.figure('Clean Random Cat Large Filter')
plt.imshow(clean_cat_2)
plt.title('Clean Random Cat Large Filter')
plt.show(block=False)

plt.figure('Clean Random Cat Gauss Filter')
plt.imshow(clean_cat_3)
plt.title('Clean Random Cat Gauss Filter')
plt.show(block=False)

# these don't really seem to clean up the image at all.
index_1 = clean_cat_1.shape[0]//10
index_2 = clean_cat_1.shape[1]//10
zoomed_in_cat_1 = clean_cat_1[0:index_1][0:index_2]
plt.figure('Zoomed In Clean Random Cat Small Filter')
plt.imshow(zoomed_in_cat_1)
plt.title('Zoomed In Clean Random Cat Small Filter')
plt.show(block=False)

index_3 = clean_cat_2.shape[0]//10
index_4 = clean_cat_2.shape[1]//10
zoomed_in_cat_2 = clean_cat_2[0:index_3][0:index_4]
plt.figure('Zoomed In Clean Random Cat Large Filter')
plt.imshow(zoomed_in_cat_2)
plt.title('Zoomed In Clean Random Cat Large Filter')
plt.show(block=False)

index_5 = clean_cat_3.shape[0]//10
index_6 = clean_cat_3.shape[1]//10
zoomed_in_cat_3 = clean_cat_3[0:index_5][0:index_6]
plt.figure('Zoomed In Clean Random Cat Gauss Filter')
plt.imshow(zoomed_in_cat_3)
plt.title('Zoomed In Clean Random Cat Gauss Filter')
plt.show(block=False)

plt.show()