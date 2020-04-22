#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 09:57:06 2020

@author: julia
"""

import numpy as np
import matplotlib.pyplot as plt

def velocity(a, dt):
    n = len(a)
    v = np.zeros(n)
    for k in range(1, n):
        v[k] = v[k-1] + (a[k-1] + a[k])/2
    v *= dt
    return v


acc = np.loadtxt('acc.dat')
dt = 0.1
vel = velocity(acc, dt)
time = np.array([i * dt for i in range(0, len(acc))])

plt.plot(time, acc, color='#053061', linewidth=1.5)
plt.plot(time, vel, color='#67001f', linewidth=1.5)
plt.xlabel('Time')
plt.legend(['Acceleration', 'Velocity'], loc=2)
plt.title('Time dependence of object acceleration and velocity')
plt.show()