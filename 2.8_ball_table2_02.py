#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 15:07:10 2020

@author: julia
"""
l_t=[]
l_y=[]
a = 0
g = 9.81
n = eval(input("What is the number of iterations?"))
v_o = eval(input("What is the initial velocity?"))
b = 2*v_o/g
i = 0
for i in range (n+1):
    h = (b - a)/n
    t = a + i*h
    y = v_o*t - (1/2)*g*t**2
    l_t.append(t)
    l_y.append(y)
    i += 1
for y, t in zip(l_y,l_t):
    print (y, t)