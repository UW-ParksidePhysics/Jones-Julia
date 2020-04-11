#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 16:15:35 2020

@author: julia
"""
#ch3p18
### Paul Rizzo helped out with this code; give credit to where credit is due ###

### Program to calculate derivatives ###

### Part a ###
def diff(f, x, h): # Improved version of the fundamental theorem of calculus; calculates the derivative
    d = ((f(x+h) - f(x-h)) / (2*h))
    return d


### Part c ###
def application(f, x, h, exact_derivative):
    derivative = diff(f, x, h)
    error = exact_derivative - derivative
    print()
    print("Approximate Derivative =", derivative)
    print("Exact Derivative =", exact_derivative)
    print("Error=", derivative, "-", exact_derivative, "=", error)
    return


from math import *

    # Function code
def f(x):
    f = exp(x)
    return f

def g(x):
    g = exp(-2 * (x**2))
    return g

def h(x):
    h = cos(x)
    return h

def i(x):
    i = log(x)
    return i

    # Driver code
application(f, 0, 0.01, 1)
application(g, 0, 0.01, 0)
application(h, (2 * pi), 0.01, 0)
application(i, 1, 0.01, 1)

### Part b ###

def a(x):
    a = 4*x**4
    return a

application(a,0,0.01,0)