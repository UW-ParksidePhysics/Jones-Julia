  
### Program to calculate the orbit and instaneous velocity of Pizza Planet
import numpy as np
import matplotlib.pyplot as plt

### Function code
def orbit(t, a, b, w):
    return a * np.cos(w * t), b * np.sin(w * t)


def velocity(t, a, b, w):
    return w * np.sqrt((a * np.sin(w * t)) ** 2 + (b * np.cos(w * t)) ** 2)


def PizzaPlanet(a, b, w, n):
    tlist = np.linspace(0, 2 * np.pi / w, n) # Creates an array of t
    xorbit, yorbit = orbit(tlist, a, b, w) # Formats tlist in ORBIT function to create orbit line
    counter = 0
    for t in tlist:
        x, y = orbit(t, a, b, w)
        plt.plot(xorbit, yorbit, '--', color='#67001f', linewidth=2) # Creates orbit line
        plt.plot(x, y, 'bo', markerfacecolor='#2166ac',
                 markeredgecolor='#053061', markeredgewidth=2, markersize=20) # Creates the planet
        plt.xlim([xorbit.min() * 1.5, xorbit.max() * 1.5]) # x-axis limits
        plt.ylim([yorbit.min() * 1.5, yorbit.max() * 1.5]) # y-axis limits
        plt.xlabel('x') # Axis label
        plt.ylabel('y') # Axis label
        plt.title('Instantaneous velocity = {:.4f}'.format(velocity(t, a, b, w))) # Plot title
        plt.savefig('tmp_{:0>4}.png'.format(counter)) # Saves snapshots of plots
        counter += 1

### Driver code
PizzaPlanet(10, 10, 20, 30)
