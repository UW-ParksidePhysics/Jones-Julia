#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:14:24 2020

@author: julia
"""

### Program to extract Temperature from data file.
infile = open('temperature_data.dat', 'r')

# Data extraction code
z = []
for line in infile:
    z1 = line.split()
    z.append(z1)
infile.close()
z = z[3][2]
z = float(z)

# Function code
def T(z):
    T = (5 / 9) * (z - 32)
    return T

# Driver code
print("Temperature in Celsius degrees =", T(F))