# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 08:45:47 2015

@author: Chris
"""

import math
loop="yes"
def T(h):
    if h<=11000:
        T1=288.15-0.0065*h
    else:
        T1=T(11000)
    return T1
    
def rho(h):
    if h<=11000:
        rho1=1.225*(T(h)/288.15)**(9.81/(0.0065*287))
    else: 
        rho1=rho(11000)*math.e**((9.81/(0.0065*T(11000)))*(h-11000))
    return rho1
                
def p(h):
    p1=101325*math.e**(-9.81/287/T(h)*(h))
    return p1
