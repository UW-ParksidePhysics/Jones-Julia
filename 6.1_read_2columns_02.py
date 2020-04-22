#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 09:53:16 2020

@author: julia
"""

import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

infile = open('xy.dat', 'r')
for line in infile:
    coords = line.split()
    x.append(float(coords[0]))
    y.append(float(coords[1]))
infile.close()

x, y = np.array(x), np.array(y)

print ('Minimum x value = {:.4f}'.format(x.min()))
print ('Maximum x value = {:.4f}'.format(x.max()))
print ('Minimum y value = {:.4f}'.format(y.min()))
print ('Maximum y value = {:.4f}'.format(y.max()))

plt.plot(x, y, color='#053061', linewidth=1.5)
plt.xlabel('x')
plt.ylabel('y')
plt.show()