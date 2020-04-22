#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 18:04:36 2020

@author: julia
"""
#ch3p3
### Paul Rizzo helped out with this code; give credit to where credit is due ###
### Two algorithms to output the roots of an inputted quadratic equation ###

### Inbuilt function method
from numpy import roots

a = eval(input("What is a? "))
b = eval(input("What is b? "))
c = eval(input("What is c? "))

List = [a, b, c]
R = roots(List) # Roots is an inbuilt command of numpy

print (R)
print ()
print ()

### Scratch method

from numpy.lib.scimath import sqrt # imports the sqrt command from scimath to output complex numbers

D2 = (b**2) - (4*a*c)
if a == 0:
    print('a cannot be equal to zero for the defined function to be quadratic, shame on you')

if D2 >= 0:
    D = sqrt(D2)
    x1 = (-b - D) / (2 * a)
    x2 = (2 * c) / (-b - D)
    R = [x1, x2]
    print("test_roots_float")   # Returns roots as float
    print(R)

elif D2 < 0:
    D2 = -D2
    D = (sqrt(D2) / (2 * a))
    b2 = -b / (2 * a)
    print("test_roots_complex")   # Returns root as complex number
    print(b2, "+", D, "j"",", b2, "-", D, "j") # Displays two +- roots
