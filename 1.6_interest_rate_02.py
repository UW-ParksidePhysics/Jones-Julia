# Interest rate
n = 3
A = 1000 
p = 5

def I(n,A,p):
    i = A*(1 + p/100)**n
    return i

print ("The amount of Euros after {} years for {} euros at an interest rate of {} is {} Euros.".format(n,A,p,I(n,A,p)))