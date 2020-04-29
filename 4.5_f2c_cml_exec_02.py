#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:16:10 2020

@author: julia
"""
#program with try except

import sys
try:
    F = float(sys.argv[1])
except IndexError:
    print ('You failed to provide a temperature in Fahrenheit '\
        'as input on the command line')
    sys.exit(1)  # abort
C = 5. / 9 * (F - 32)
print ("{:.f} Fahrenheit = {:.f} Celsius".format(F, C))