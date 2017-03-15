# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 14:42:24 2017

@author: Chris
"""


#PROBLEMS 
#Program doesnt work in Python consol but works in ipython consol
#
#
#
from Cit_par import *
import numpy as np
import scipy as sp
import control
import matplotlib.pyplot
from dataanalyzer import load,cal_mass 
from state_space import state_space2
from Calc_ISA import T

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

#Create state space system for symmetric and asymmetric case
sys_sym, sys_asym = state_space2(Clr,Clda,muc,c,V,CZa,Cmadot,KY2,CXu,CXa,CZq,
                                 CZu,CX0,Cmu,Cma,Cmq,CXde,CZde,Cmde,CYbdot,b,
                                 mub,KX2,KXZ,KZ2,CYb,CL,CYp,CYr,Clb,Clp,Cnb,
                                 Cnp,Cnr,CYda,Cldr,Cnda,Cndr,CYdr)
                                 
#Calculate eigenvalues of system sym and asym 
print "Symetric system values:"
control.matlab.damp(sys_sym)
print
print "Asymetric system values:"
control.matlab.damp(sys_asym)

#Read Fligh test data
data = load("Flight_data.mat")  #see dataanalyzer function for definition of indexes

#Questions
#Check whether right temperature has been used static data[35], total data[36] or total corrected data[49] 
#Below calculation for CL True as CL is a function of Weight etc? 

#Still need to be calculated 
Tcs = 1
Tc  = 1


#Calculation of useful variables
#Correct measured temperature for RAM 
data.append(["RAM corrected total Temperature",  np.divide(data[36][1], np.multiply( 1+(gamma-1)/2 , np.square(data[40][1])       )          )])   
data.append(["Mass",cal_mass(initial_mass,data,data[20][1])])   #weight at each instant 
data.append(["Pressure",p0*(1+gamma*data[37][1]*ft_to_m/T0)**(-g/gamma/R)]) #static pressure at each instant 
data.append(["Density",np.divide(data[51][1],R)/(data[35][1]+C_to_K)])     #density at each instant
data.append(["Equivalent Air Speed",data[42][1]*knots_to_ms*np.sqrt(data[52][1]/rho0)])   #EAS at each instant 
data.append(["Lift Coefficient",np.multiply(2*g,data[50][1])/(data[52][1]*np.multiply(np.square(data[53][1]), S))])     #Lift coefficient at each isntant 
data.append(["Drag Coefficient",CD0 + np.square(data[54][1])/(np.pi*e*A)])  #drag coefficient at each instant 
data.append(["Reduced equivalent airspeed", np.multiply(data[53][1], np.divide(Ws,np.multiply(data[50][1],g))  )    ])
data.append(["Reduced elevator deflection", np.multiply(data[17][1],deg_to_rad) -  Cmtc/Cmde * (Tcs - Tc)])






























##Test thrust file 
#tempdiff = []
#for i in range(len(data[37][1])):
#    tempdiff.append(data[35][1][i] + C_to_K - T(data[37][1][i]*ft_to_m))
#data.append(["ISA Temperature difference", np.array(tempdiff)])
#matlab = {}
#matlab["Pressure Altitude"] = data[37][1]
#matlab["Mach"] = data[40][1]
#matlab["ISA Temperature Difference"] = data[58][1]
#matlab["Left engine"] = data[3][1]
#matlab["Right engine"] = data[4][1]
#sp.io.savemat("matlab.dat",matlab)


