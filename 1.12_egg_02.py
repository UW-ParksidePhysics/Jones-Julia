### To cook a perfect egg ###
from math import *
# Object definitions
rho = 1.038 # g/cm^3
c = 3.7 # J/g*K
K = 5.4*10**(-3) # W/cm*K
T_w = 100 # C
T_y = 70 # C
# Function code
def Egg(M,c,rho,K,T_w,T_y,T_o):
    t = ((M**(2/3)*(c*rho**(1/3)))/((K*pi**2)*((4/3)*pi)**(2/3)))*log((0.76)*((T_o - T_w)/(T_y - T_w)))
    return t
# Driver code
M = eval(input("Please input the mass of the egg in grams: "))
T_o = eval(input("Please input the temperature of the egg prior to boiling in Celcius: "))
EGG = Egg(M,c,rho,K,T_w,T_y,T_o)
print ("The time for the yolk to reach 70 C in seconds is {}.".format(EGG))
