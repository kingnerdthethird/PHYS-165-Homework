# Laura Ocampo, Isaac Pliskin, Luis Argueta, Zixi Zhang, Phillip Cho
# Physics 165 Lab 2
# The one with the random walks
# WARNING: THIS DOES NOT RUN WELL ON LAPTOPS BECAUSE THEY ARE WIMPY LITTLE THINGS
# I DO NOT TAKE RESPONSIBILITY FOR YOUR LAPTOP GETTING VERY HOT

# This program generates various random walks.
# Assignment 1 deals with smaller amounts of random walks
# Assignment 2 deals with a lot of random walks
# I mean a stupid amount of random walks
# Seriously it is an unneccessary amount of random walks but it was fun to do
# Also the graphs were fun to look at so I made a lot of them
from numpy.random import random as rng # we want them random numbers
import numpy as np # for the math functions
import matplotlib.pyplot as plt # to make pretty pretty class

def Random_Walk(steps): # our function that does all the work
    # you could say this is the workhorse of the program
    # it takes the random walks for us so we don't have to and can stay inside, never to walk again
    # our random walk generates arrays of positions, not arrays of steps
    # this is important and means that we do not need to sum over slices of an array later to generate paths
    x = np.zeros(number_steps) # create a null array for x positions
    y = np.zeros(number_steps) # create a null array for y positions
    x_samples = rng(number_steps) # generate 1000 random floats between 0 and 1
    y_samples = rng(number_steps) # generate 1000 random floats between 0 and 1

    x_sum = 0 # set the final x position to zero
    # x_sum will be the sum of all movements in the x direction so that the end result is the final x value
    y_sum = 0 # set the final y position to zero
    # y_sum will be the sum of all movements in the y direction so that the end result is the final y value

    for i in range(1, number_steps): # we use a parameter for the range so we can change it easier
        if x_samples[i] < 0.5: # if x_samples[i] is heads, move +1 in x direction
            x[i] = x[i - 1] + 1 # move +1 in the x direction
            x_sum += 1 # I add one to the sum of x movements
        else: # if x_samples[i] is tails, move -1 in the x direction
            x[i] = x[i - 1] - 1 # move -1 in the x direction
            x_sum -= 1 # I subtract one from the sum of the x movements

        if y_samples[i] < 0.5: # if y_samples[i] is heads move +1 in the y direction
            y[i] = y[i - 1] + 1 # move +1 in the y direction
            y_sum += 1 # I add one to the sum of the y movements
        else: # if y_samples[i] is tails move -1 in the y direction
            y[i] = y[i - 1] - 1 # move -1 in the y direction
            y_sum -= 1 # I subtract one from the sum of the y movements

    

    distance = np.sqrt(x_sum**2 + y_sum**2) # find the displacement from the origin for the walk

    return x, y, distance # return the x positions, y positions, and displacement


number_steps = 1000 # this the number of steps to do for all random walks

# Begin Assignment 1

# Part 1.a.
# One single random walk
plt.figure('Part 1.a.') # create the new figure for part 1.a.
# This plot will be of one random walk

x1a, y1a, d1a = Random_Walk(number_steps) # generate one single random walk
# x1a is the x positions for part 1.a.
# y1a is the y positions for part 1.a.
# d1a is the displacement for part 1.a.
# Remember this is for one single random walk

print("Displacement for Part 1.a. is: ", d1a) # print out the displacement for the walk generated in part 1.a.

plt.plot(x1a, y1a, '--') # plot x1a vs y1a with dotted lines, for aesthetic fun
plt.plot(x1a[-1], y1a[-1], 'ro') # plot the final position for context
# doing this helps to orient your thinking about the walks
plt.axis('equal') # use equal axes in the name of equality
plt.title('Assignment 1 Part a') # christen the plot with a bad ass name that is both informative and concise
plt.xlabel('x values') # label axes because we are scientists
plt.ylabel('y values') # label axes because we are scientists
plt.show(block=False) # show the plot, but do not block the rest of the code from running

# Part 1.b.
# Four walks
d1b = [] # create an empty list for the displacements in part 1.b.
x1b = [] # create an empty list for the lists of x positions in part 1.b.
y1b = [] # create an empty list for the lists of y positions in part 1.b.
# you will notice that unlike in part 1.a., these are lists
# this is to be expected because we now have four walks so they will be stored together
# f = plt.figure('Part 1.b.')
for i in range(0, 4): # I got lazy and did not parameterize the range for this part
    # why do more work than you need to?
    x, y, d = Random_Walk(number_steps) # generate a random walk
    # x is the temporary list of the x positions for this random walk
    # y is the temporary list of the y positions for this random walk
    # d is the temporary list of the displacements for this random walk
    d1b.append(d) # append the temporary displacement to the end of d1b
    x1b.append(x) # append the temporary x positions to the end of x1b
    y1b.append(y) # append the temporary y positions to the end of y1b

f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row') # creating a plot with four subplots
# each walk will be plotted on the same figure, but in separate subplots
# the subplots will have the same axes so one or more might go off the plots
f.canvas.set_window_title('Part 1.b.') # because python is annoying you have to do this complicated thing to set the title
# anyways, the title is what appears in the title bar of the window
plt.title('Assignment 1 Part b') # this is the title of the plot as a whole
# I forget if this actually shows up or if I have done goofed and it does not
plt.xlabel('x values') # we label the axes to be taken seriously
plt.ylabel('y values') # see above

# The following block (bloc?) of code is to plot the first walk in the upper left corner
ax1.plot(x1b[0], y1b[0], 'b--') # this is the actual plot of the first walk, in a nice blue, with dashed lines 
ax1.plot(x1b[0][-1], y1b[0][-1], 'ro') # the final poisition is plotted with a red dot for contrast
ax1.set_title('Part 1.b. Walk 1') # always title your graphs
ax1.set_xlabel('x values') # always label the x axis
ax1.set_ylabel('y values') # always label the y axis

# The following chunk of code is to plot the second walk in the upper right corner
ax2.plot(x1b[1], y1b[1], 'y--') # this is where I plot the second walk with an ugly yellow dashed line
ax2.plot(x1b[1][-1], y1b[1][-1], 'ro') # plot the final position with a dot so it sticks out
ax2.set_title('Part 1.b. Walk 2') # very creative title 10/10 
ax2.set_xlabel('x values') # x axis label
ax2.set_ylabel('y values') # y axis label

# the following chunk of code plots the third random walk in the bottom left corner
ax3.plot(x1b[2], y1b[2], 'r--') # I am not a fan of the color red but it looks fine, I guess
ax3.plot(x1b[2][-1], y1b[2][-1], 'bo') # I have to use a blue dot to make it stick out
ax3.set_title('Part 1.b. Walk 3') # title the graph 
ax3.set_xlabel('x values') # x axis label 
ax3.set_ylabel('y values') # y label for y axis

# the following lines of code plot the fourth and final walk for this part of the lab
ax4.plot(x1b[3], y1b[3], 'g--') # green is best color and always save the best for last
ax4.plot(x1b[3][-1], y1b[3][-1], 'ro') # red dot for contrast so you can see the final position
ax4.set_title('Part 1.b. Walk 4') # title of the graph
ax4.set_xlabel('x values') # label for the horizontal x axis of the random walk graph
ax4.set_ylabel('y values') # see above but subsitute vertical for horizontal

print("The displacements for the four walks are: ", d1b) # print out the list of final displacements for the four walks

plt.axis('equal') # equality
plt.show(block=False) # show the graph but continue the code

# Begin Assignment 2
# this is the part of the code that will hurt your computer
# I do not suggest running the code many times in a row or else your laptop will get a little toasty*
# *Isaac is not responsible for computers that become too toasty
# What are we, computer scientists? No. We don't know how to perfectly optimize this code so that it doesn't heat your computer up
# Sorry

# Part 2.a
# 1000 random walks with 1000 steps a piece
x_final = [] # list of final x positions
y_final = [] # list of final y positions
x2a = [] # list of x positions for all walks in part 2.a.
y2a = [] # list of y positions for all walks in part 2.a.
d2a = [] # list of displacement values for all walks in part 2.a.
number_runs = 1000 # the number of runs is parameterized so that we can test the code without destroying our computers

for i in range(0, number_runs): # range should be 0 to 999 in final code
    # i.e. final code will have 1000 iterations
    x, y, d = Random_Walk(number_steps) # generate a random walk and set temporary values to the outputs
    x2a.append(x) # append the temporary list of x positions to the end of x2a
    y2a.append(y) # append the temporary list of y positions to the end of y2a
    d2a.append(d) # append the temporary displacement to the end of d2a

    x_final.append(x[-1]) # append the temporary final x position to the end of x_final
    y_final.append(y[-1]) # append the temporary final y position to the end of y_final

plt.figure('Part 2.a. Paths') # create a new figure for the plot of the paths
# this plot looks amazing 
for i in range(0, number_runs): # number of runs is same as above
    plt.plot(x2a[i], y2a[i]) # add the plot of each individual path to the plot
    # I don't know if there is a better way to do this without a for loop

plt.axis('equal') # equality
plt.title('Paths for 1000 Random Walks') # title the plot for reader's convienence (I dunno how to spell)
plt.xlabel('x values') # label the x axis
plt.ylabel('y values') # label the y axis
plt.show(block=False) # show the plot but continue the code

plt.figure('Part 2.a. Final Positions') # create a new figure for the scatter plot of final x vs y positions
plt.scatter(x_final, y_final, color='green') # green is best color. this is a scatter plot of the final positions

plt.axis('equal') # always use equal axes
plt.title('Final Positions for 1000 Random Walks') # title the graph
plt.xlabel('final x values') # label the x axis
plt.ylabel('final y values') # label the y axis
plt.show(block=False) # show the plot but do not block the code

# Part 2.b.
# Plot stuff as a histogram
# Or something

plt.figure('Part 2.b. First Histogram') # create a figure for the first histogram
plt.hist(d2a) # this is pretty simple
plt.title('Histogram of Displacements for 1000 Walks') # title the histogram
plt.xlabel('Displacement') # label the x axis
plt.ylabel('Frequency') # label the y axis
plt.show(block=False) # show the plot but allow the rest of the code to run

# Part 2.c.
d2asquared = [i**2 for i in d2a] # I really like that I can do this in python
# I create a list of all the displacements, squared 
# the fact that I can have the for loop in the brackets is cool
# with that said, python is frustrating

plt.figure('Part 2.c. Second Histogram') # create a new figure for the squared displacements
plt.hist(d2asquared) # this is really simple
plt.title('Histogram of Displacements Squared for 1000 Walks') # title the graph
plt.xlabel('Displacement Squared') # label the x axis
plt.ylabel('Frequency') # label the y axis
plt.show(block=False) # show the graph but do not block the rest of the code

# Part 2.d.
# plotting the histogram with logarithmic axes
# some of them look cool, some look dumb
# I blame python

plt.figure('Part 2.d. semilogy') # create a figure for a histogram with logarithmic y axis
plt.hist(d2asquared) # this is rather simple
plt.yscale('log', nonposy='clip') # we set the y axis to be logarithmic in scale
# it took me an embarrassingly long time for me to figure that out
plt.title('Histogram with y axis as logarithmic') # title the plot
plt.xlabel('Displacement Squared') # label the x axis 
plt.ylabel('Frequency') # label the y axis
plt.show(block=False) # show the plot but do not block the rest of the code

plt.figure('Part 2.d. semilogx') # create a new figure for a histogram with logarithmic x axis
# not gonna lie, this one looks dumb
plt.hist(d2asquared) # plot it
plt.xscale('log', nonposy='clip') # set the x axis to have a scale of logarithmic
plt.title('Histogram with x axis as logarithmic') # title the graph
plt.xlabel('Displacement Squared') # label the x axis
plt.ylabel('Frequency') # label the y axis
plt.show(block=False) # show the plot but allow other code to run

plt.figure('Part 2.d. loglog') # new figure for histogram with entirely logarithmic axes
# this one looks really stupid and you can ignore it
plt.hist(d2asquared) # create histogram
plt.yscale('log', nonposy='clip') # set y axis to be logarithmically scaled
plt.xscale('log', nonposy='clip') # set x axis to be logarithmically scaled
plt.title('Histogram with x and y axis as logarithmic') # title the histogram
plt.xlabel('Displacement Squared') # label the x axis
plt.ylabel('Frequency') # label the y axis
plt.show(block=False) # show plot and continue to rest of code

# Part 2.e.
d2asquarededmean = np.mean(d2asquared) # find the mean-squared displacement of d2asquared
print("The mean-squared displacement for 1000 steps is: ", d2asquarededmean) # print the mean-squared displacement for 1000 walks
# usually this is around 2000

# Part 2.f.
# here we generate and plot 1000 4000 step walks
# curiously, these have final positions and displacements similar to 1000 step walks

x_final_f = [] # final x position list for part 2.f.
y_final_f = [] # final y position list for part 2.f
x2f = [] # list of x positions for part 2.f.
y2f = [] # list of y positions for part 2.f.
d2f = [] # list of displacement values for part 2.f.
number_runs = 1000 # number of runs for part 2.f.

for i in range(0, number_runs): # see above
    x, y, d = Random_Walk(number_steps * 4) # we want 4000 step walks, thus the 4*
    x2f.append(x) # append the temporary x positions list to the end of x2f
    y2f.append(y) # append the temporary y positions list to the end of y2f
    d2f.append(d) # append the temporary displacement value to the end of d2f

    x_final_f.append(x[-1]) # append the temporary final x position to the end of x_final_f
    y_final_f.append(y[-1]) # append the temporary final y position to the end of y_final_f

plt.figure('Part 2.f. Paths') # create a new figure for the paths of the 4000 step walks
for i in range(0, number_runs): # range for the walks run
    plt.plot(x2f[i], y2f[i]) # add each individual plot to the figure

plt.axis('equal') # axes equal cause why not
plt.title('Paths for 1000 Random Walks with 4000 Steps') # title the graph 
plt.xlabel('x values') # label the x axis
plt.ylabel('y values') # label the y axis
plt.show(block=False) # show plot but do not block

plt.figure('Part 2.f. Final Positions') # figure for the final positions of the 4000 step random walks
plt.scatter(x_final_f, y_final_f, color='green') # create a beautiful scatter plot of the final positions with the best color

plt.axis('equal') # axes equal as always
plt.title('Final Positions for 1000 Random Walks') # title the graph
plt.xlabel('final x values') # label the x axis
plt.ylabel('final y values') # label the y axis
plt.show(block=False) # show the plot but no blocking

d2fsquared = [i**2 for i in d2f] # this is still very cool to me
d2fsquaredmean = np.mean(d2fsquared) # find the mean-squared displacement 
print("The mean-squared displacement for 4000 steps is: ", d2fsquaredmean) # print the mean squared displacement for the 4000 step walks
# usually this is around 2000
# I find it very cool that these are so similar to the 1000 step walks
# although, to be fair, we could have messed up
# always a possibility

plt.show() # final plot show to show all the plots


# line 300 yay