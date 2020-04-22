#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 09:54:38 2020

@author: julia
"""

import numpy as np
import matplotlib.pyplot as plt

def load(densityfile):
    infile = open(densityfile, 'r')
    data = {'temperature': [], 'density': []}

    for line in infile:
        if not(line.isspace()) and line.lstrip()[0] != '#':   # blank line or comment
            values = line.split()
            data['temperature'].append(float(values[0]))
            data['density'].append(float(values[1]))
    data['temperature'] = np.array(data['temperature'])
    data['density'] = np.array(data['density'])
    infile.close()
    return data


def plot_data(x, y, substance):
    plt.plot(x, y, 'o',
             markerfacecolor='#2166ac',
             markeredgecolor='#053061',
             markersize=8,
             markeredgewidth=1.5)
    plt.xlabel('Temperature')
    plt.ylabel('Density')
    plt.title('Temperature dependence of {} density'.format(substance))
    # set axis ranges appropriately
    x_range = x.max() - x.min()
    y_range = y.max() - y.min()
    plt.xlim([x.min() - 0.1 * x_range, x.max() + 0.1 * x_range])
    plt.ylim([y.min() - 0.1 * y_range, y.max() + 0.1 * y_range])
    plt.show()


data = load('density_air.dat')
plot_data(data['temperature'], data['density'], 'air')
data = load('density_water.dat')
plot_data(data['temperature'], data['density'], 'water')