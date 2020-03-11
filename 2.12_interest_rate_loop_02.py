from math import *
initial_amount = 100
p = 5. # Interest rate
amount = initial_amount
years = 0
while amount <= 1.5*initial_amount:
    amount += pi/100*amount
    years += 1
print (years)