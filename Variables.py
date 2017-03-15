# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:34:37 2017

@author: Chris
"""
from math import pi
from Cit_par import *
#Conversion variables
ft_to_m   = 0.3048 
lbs_to_kg = 0.45359237
C_to_K    = 273.15
knots_to_ms = 0.514444444
deg_to_rad = pi/180.


#Standart Variables
gamma = 1.4
rho0      = 1.225
p0        = 101325
T0         = 288.15
R          = 287

#Reduced Variables
Ws         = 60500 #used in appendix B 
mfs        = 0.048

#Variables that need to be calcualted
V  = V0 
initial_mass = 50000 / g
Tcs = 1
Tc  = 1