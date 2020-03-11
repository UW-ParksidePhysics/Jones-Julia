#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:47:10 2020

@author: julia
"""

l=[]
n = eval(input("What is the number of n :"))
a = eval(input("What is the first coordinate point: "))
b = eval(input("What is the last coordinate point: "))
i=0
for i in range (n):
    h = (b - a)/n
    x = a + i*h
    l.append(x)
    i += 1
print (l)
    
    
    