#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 17:54:22 2020

@author: julia
"""
#ch3p34

### Paul Rizzo helped out with this code; give credit to where credit is due ###
### The Wikipedia article on the Seive had an amazing gif that you should check out ###
### Program to calculate prime numbers up to a certain numner, N

### Function code ###
prime_numbers = []
print ("To find prime numbers up to the number N, enter N")
N = int(input("N=?"))

for i in range(2, N + 1):
    prime_numbers.append(i) # Appends the list "prime_numbers" with a full list of integers up to N

w = 2 # Sift the 2!
while w < len(prime_numbers): # w is an element position of the "prime_numbers" list
    element = prime_numbers[w] # calls w-th element
    if element % 2: # Tests the remainder of the modulo
        0 # Blank statement; nothing will happen
    else:
        prime_numbers.pop(w) # Removes an element from the list "prime_numbers"
    w += 1 # Loop!
    
w = 3 # Sift the 3!
while w < len(prime_numbers):
    element = prime_numbers[w]
    if element % 3:
        0
    else:
        prime_numbers.pop(w)
    w += 1

w = 5 # Sift the 5!
while w < len(prime_numbers):
    element = prime_numbers[w]
    if element % 5:
        0
    else:
        prime_numbers.pop(w)
    w += 1

w = 7 # Sift the 7!
while w < len(prime_numbers):
    element = prime_numbers[w]
    if element % 7:
        0
    else:
        prime_numbers.pop(w)
    w += 1

### Driver code ###
print(prime_numbers)
