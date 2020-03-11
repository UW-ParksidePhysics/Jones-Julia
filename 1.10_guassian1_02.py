# Guassian problem
from math import *
m = 0
s = 2
x = 1

def G(m,s,x):
    f = (1/((sqrt(2*pi))*s))*exp((-1/2)*((x - m)/(s))**2)
    return f

print ("The real G is {}.".format(G(m,s,x)))