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

#Conversion variables
ft_to_m   = 0.3048 
lbs_to_kg = 0.45359237
C_to_K    = 273.15
knots_to_ms = 0.514444444
deg_to_rad = pi/180.

#Standart Variables
lambda_air = 1.4
rho0      = 1.225
p0        = 101325
T0         = 288.15
R          = 287


#Variables that need to be calcualted
V  = V0 
initial_mass = 50000 / g

#Create state space system for symmetric and asymmetric case
sys_sym, sys_asym = state_space2(Clr,Clda,muc,c,V,CZa,Cmadot,KY2,CXu,CXa,CZq,
                                 CZu,CX0,Cmu,Cma,Cmq,CXde,CZde,Cmde,CYbdot,b,
                                 mub,KX2,KXZ,KZ2,CYb,CL,CYp,CYr,Clb,Clp,Cnb,
                                 Cnp,Cnr,CYda,Cldr,Cnda,Cndr,CYdr)

#Read Fligh test data
data = load("Flight_data.mat")  #see dataanalyzer function for definition of indexes

#Calculation of useful variables
data.append(["Mass",cal_mass(initial_mass,data,data[20][1])])   #weight at each instant 
data.append(["Pressure",p0*(1+lambda_air*data[37][1]*ft_to_m/T0)**(-g0/lambda_air/R)]) #static pressure at each instant 
data.append(["Density",data[50][1]/R/(data[35][1]+C_to_K)])     #density at each instant
data.append(["Equivalent Air Speed",data[42][1]*knots_to_ms*np.sqrt(data[51][1]/rho0)])   #EAS at each instant 
#Below calculation for CL True as CL is a function of Weight etc? 
data.append(["Lift Coefficient",np.multiply(2*g,data[49][1])/(data[51][1]*np.multiply(np.square(data[52][1]), S)) ])     #Lift coefficient at each isntant 

