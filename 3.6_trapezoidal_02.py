#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:12:12 2020

@author: julia
"""

#ch3p6

### Paul Rizzo helped out with this code; give credit to where credit is due ###
### Program to evaluate integrals via the trapezoidal rule

### Part a ###
def trapezint1(f, a, b, actual_area): # Trapezoidal rule function
    A = ((b - a) / 2) * (f(a) + f(b)) 
    print("Area under the curve =", A)
    error = abs(A) - abs(actual_area) # Code to ouput error within trapezoidal rule approximation
    print("Error =", error)
    return trapezint1


### Part b ###
from math import *


def f(x):
    f = cos(x)
    return f

a = 0; b = pi # Positional arguement (initial condition) 
actual_area = 0 # Calculated analytically
trapezint1(f, a, b, actual_area) # Calls the function with the given positional arguements


def g(x):
    g = sin(x)
    return g

a = 0; b = pi
actual_area = 2
trapezint1(g, a, b, actual_area)


def h(x):
    h = sin(x)
    return h

a = 0; b = (pi / 2)
actual_area = 1
trapezint1(h, a, b, actual_area)
print()


### Part c ###
def trapezint2(f, a, b, actual_area): # Improved trapezoidal rule via splitting trapezoid
    c = b / 2
    A = ((c - a) / 2) * (f(a) + f(c)) + ((b - c) / 2) * (f(c) + f(b))
    print("Area under the curve =", A)
    error = abs(A) - abs(actual_area)
    print("Error =", error)
    return trapezint2


def f(x):
    f = cos(x)
    return f

a = 0; b = pi
actual_area = 0
trapezint2(f, a, b, actual_area)



def g(x):
    g = sin(x)
    return g

a = 0; b = pi
actual_area = 2
trapezint2(g, a, b, actual_area)



def h(x):
    h = sin(x)
    return h


a = 0; b = (pi / 2)
actual_area = 1
trapezint2(h, a, b, actual_area)
print()


### Part d ### 
def trapezint(f, a, b, n, actual_area): # Improved trapezoidal rule by splitting the trapezoid n times
    x = a; A = 0; i = 0; h = (b - a) / n #Slice!

    while i <= n:
        del_a = (f(a + (i * h)) + f(a + (i + 1) * h)) * (h / 2)
        A += del_a
        x += h
        i += 1
    print("Area under the curve =", A)
    error = abs(A) - actual_area
    print("Error =", error)
    return trapezint


### Part e ###
def test_trapezint(): # A defined function that calls a series of other "arguement" functions
    def f(x):
        f = cos(x)
        return f

    a = 0; b = pi
    actual_area = 0
    trapezint(f, a, b, 10, actual_area)



    def g(x):
        g = sin(x)
        return g

    a = 0; b = pi
    actual_area = 2
    trapezint(g, a, b, 10, actual_area)



    def h(x):
        h = sin(x)
        return h

    a = 0; b = (pi / 2)
    actual_area = 1
    trapezint(h, a, b, 10, actual_area)
    return test_trapezint


test_trapezint()
© 2020 GitHub, Inc.
