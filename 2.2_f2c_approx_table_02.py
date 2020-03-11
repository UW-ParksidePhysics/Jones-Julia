#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:20:37 2020

@author: julia
"""
print ('---------') #table heading
F= 0
dF=5 
while F<= 100: 
    C= F-32*(5/9)
    H=(F-30)/2
    print (F,C,H)
    F= F +dF
print('--------')