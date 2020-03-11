#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:32:13 2020

@author: julia
"""


n=eval(input("enter n:"))
odd=[]
i = 1
while i <= n:
    if (i % 2 != 0):
        odd.append(i)
    i += 1
print(odd)
        
    