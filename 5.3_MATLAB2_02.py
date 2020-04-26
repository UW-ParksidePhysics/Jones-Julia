from math import sqrt, exp, pi
from numpy import linspace
import matplotlib.pyplot as mp

x = linspace(0, 10, 200)


def y1(x):
    y1 = (1 / (0.5 * sqrt(2 * pi))) * 2.71828 ** ((-1 / 2) * ((x - 5) / 0.5) ** 2)
    return y1


def y2(x):
    y2 = (1 / (1.0 * sqrt(2 * pi))) * 2.71828 ** ((-1 / 2) * ((x - 5) / 1.0) ** 2)
    return y2


def y3(x):
    y3 = (1 / (1.5 * sqrt(2 * pi))) * 2.71828 ** ((-1 / 2) * ((x - 5) / 1.5) ** 2)
    return y3


mp.plot(x, y1(x), label='σ = 0.5')
mp.plot(x, y2(x), label='σ = 1.0')
mp.plot(x, y3(x), label='σ = 1.5')

mp.xlabel('0 <= x <= 10')
mp.ylabel('Φ(x-5,σ)')
mp.legend()
mp.title('Problem 2')
mp.axis([0, 10, 0, 1])
mp.show()
