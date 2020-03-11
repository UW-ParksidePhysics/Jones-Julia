#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 14:43:58 2020

@author: julia
"""
n= eval(input("enter n:"))
sum=0
for i in range(n+1):
    sum=sum+i
    i += i+1
print(sum)