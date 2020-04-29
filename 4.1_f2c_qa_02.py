#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:13:04 2020

@author: julia
"""

### Program to convert Farenheit to Celcius
F = int(input("Temperature in Fahrenheit? "))

# Function code
def T(F):
    T = (5/9)*(F-32)
    return T

# Driver code
print("Temperature in Celsius degrees =", T(F))