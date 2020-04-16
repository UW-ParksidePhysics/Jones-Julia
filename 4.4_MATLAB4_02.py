from numpy import zeros, linalg, linspace, sqrt, sin, pi, sum
import matplotlib.pyplot as mp
import numpy as np

npoints = int(input('What npoints? '))
var = max(10, npoints)
A = zeros([var, var])

n = 0
while n <= var-1:
    A[n, n] = 2
    n = n + 1

n = 0
while n <= var-2:
    A[n, n + 1] = 1
    A[n + 1, n] = 1
    n = n + 1


H = (1 / (2 * (1 / (var - 1)) ** 2)) * A
dx = var/(var+1)

(V, D) = linalg.eig(H)
B = D[:, [-1]]
C = sqrt(sum(B**2)*dx) # Normalization constant
E = B/C
x = linspace(1/(var+1), var/(var+1), var)


def y(x):
    y = sqrt(2) * sin(pi * x)
    return y


mp.plot(x, E)  # Blue Graph
mp.plot(x, y(x))  # Orange Graph
mp.show()