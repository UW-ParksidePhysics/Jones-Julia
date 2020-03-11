# Kick
from math import *
# Objects
a = 0.11 #m
m = 0.43 #kg
C_D = 0.2 #constant
rho = 1.2 #kg/m^3
g = 9.81 #m/s^2
F_g = g*m #N
A  = pi*a**2 #m^2
V_1 = (120)*(1000)*(1/3600) #m/s
V_2 = (10)*(1000)*(1/3600) #m/s
F_d_1 = (1/2)*(C_D)*(rho)*(A)*(V_1)**2 #N
F_d_2 = (1/2)*(C_D)*(rho)*(A)*(V_2)**2 #N
R_1 = (F_d_1)/(F_g)
R_2 = (F_d_2)/(F_g)
print ("The drag force at 120 km/h is: ",F_d_1)
print ("The drag force at 10 km/h is: ",F_d_2)
print ("The ratio of drag and gravitational force at 120 km/h is: ",R_1)
print ("The ratio of drag and gravitational force at 10 km/h is: ",R_2)