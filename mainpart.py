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
from Variables import * 
import matplotlib.pyplot as plt 

#Create state space system for symmetric and asymmetric case
sys_sym, sys_asym = state_space2(CZ0,CXq,CZadot,Cnbdot,Clr,Clda,muc,c,V,CZa,Cmadot,KY2,CXu,CXa,CZq,
                                 CZu,CX0,Cmu,Cma,Cmq,CXde,CZde,Cmde,CYbdot,b,
                                 mub,KX2,KXZ,KZ2,CYb,CL,CYp,CYr,Clb,Clp,Cnb,
                                 Cnp,Cnr,CYda,Cldr,Cnda,Cndr,CYdr)
#outputs of symetrical case : 0 velocity 1 angle of attack 2 pitch angle 3 pitch rate 
#outputs of asymetrical case: 


##############################################################################
##############   Symetric graphs presentation       ##########################
##############################################################################

##Control inputs to symetrical case of phugoid (step on elevator)

plt.clf()
inpu = np.concatenate((np.ones(1)*-0.005,np.zeros(99999))) 
l = control.forced_response(sys_sym, T=np.arange(0,1000,0.01), U=inpu)

plt.clf()
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xlabel("Time (s)")
plt.ylabel("Velocity difference (m/s)")
plt.plot(l[0],l[1][0])
plt.savefig("V_t_phugoid")


plt.clf()
#plt.ylim(-0.5*10**-3,0.5*10**-3)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xlabel("Time (s)")
plt.ylabel("Angle of attack (rad)")
plt.plot(l[0],l[1][1])
plt.savefig("AOA_t_phugoid")

plt.clf()
#plt.ylim(-0.8*10**-2,0.8*10**-2)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xlabel("Time (s)")
plt.ylabel("Pitch angle (rad)")
plt.plot(l[0],l[1][2])
plt.savefig("theta_t_phugoid")

plt.clf()
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xlabel("Time (s)")
plt.ylabel("Pitch rate (rad/s)")
#plt.ylim(-1*10**-3,1*10**-3)
plt.plot(l[0],l[1][3])
plt.savefig("q_t_phugoid")



##Control inputs to symetrical case of short period 
inpu = np.concatenate((np.zeros(1),np.ones(99999)*-0.005)) 
l = control.forced_response(sys_sym, T=np.arange(0,1000,0.01), U=inpu)

plt.clf()
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xlabel("Time (s)")
plt.xlim(0,10)
plt.ylabel("Pitch rate (rad/s)")
plt.plot(l[0],l[1][3])
plt.savefig("q_t_short_period")





###############################################################################






##############################################################################
##############   Asymetric graphs presentation      ##########################
##############################################################################


##Aperiodic roll
inpu=[]
inpu.append(  np.concatenate((np.ones(100)*-0.025,np.zeros(99900)) ) )   #aillerion input
inpu.append(  np.concatenate((np.ones(1)*0,np.zeros(99999)))  ) #rudder input
l = control.forced_response(sys_asym, T=np.arange(0,1000,0.01), U=inpu)

plt.clf()
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xlabel("Time (s)")
plt.ylabel("Roll rate (rad/s)")
plt.ylim(-1*10**-2,0.07)
plt.xlim(0,15)
plt.plot(l[0],l[1][2])
plt.savefig("p_t_aperiodic")

##Dutch roll
inpu=[]
inpu.append(  np.concatenate((np.zeros(100)*-0.025,np.zeros(99900)) ) )   #aillerion input
inpu.append(  np.concatenate((np.zeros(1)*0,np.zeros(99999)))  ) #rudder input
l = control.forced_response(sys_asym, T=np.arange(0,1000,0.01), U=inpu,X0=[pi/4,0,0,0])

plt.clf()
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xlabel("Time (s)")
plt.ylabel("Sideslip angle (rad)")
plt.ylim(-0.5,0.9)
plt.xlim(0,15)
plt.plot(l[0],l[1][0])
plt.savefig("sideslip_dutch_roll")

plt.clf()
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xlabel("Time (s)")
plt.ylabel("Roll angle (rad)")
plt.ylim(-0.5,0.9)
plt.xlim(0,15)
plt.plot(l[0],l[1][1])
plt.savefig("roll_dutch_roll")




###############################################################################


##############################################################################
##############   Flight Test Data Analysis  ##################################
##############################################################################

#Read Fligh test data
data = load("Flight_data.mat")  #see dataanalyzer function for definition of indexes

#Questions
#Check whether right temperature has been used static data[35], total data[36] or total corrected data[49] 
#Below calculation for CL True as CL is a function of Weight etc? 


#Calculation of useful variables
#Correct measured temperature for RAM 
data.append(["RAM corrected total Temperature",  np.divide(data[36][1], np.multiply( 1+(gamma-1)/2 , np.square(data[40][1])       )          )])   
data.append(["Mass",cal_mass(initial_mass,data,data[20][1])])   #weight at each instant 
data.append(["Pressure",p0*(1+gamma*data[37][1]*ft_to_m/T0)**(-g/gamma/R)]) #static pressure at each instant 
data.append(["Density",np.divide(data[51][1],R)/(data[35][1]+C_to_K)])     #density at each instant
data.append(["Equivalent Air Speed",data[42][1]*knots_to_ms*np.sqrt(data[52][1]/rho0)])   #EAS at each instant 
data.append(["Lift Coefficient",np.multiply(2*g,data[50][1])/(data[52][1]*np.multiply(np.square(data[53][1]), S))])     #Lift coefficient at each isntant 
#data.append(["Drag Coefficient",CD0 + np.square(data[54][1])/(np.pi*e*A)])  #drag coefficient at each instant 
#To plot elevator deflection with airspeed
data.append(["Reduced equivalent airspeed", np.multiply(data[53][1], np.divide(Ws,np.multiply(data[50][1],g))  )    ])
data.append(["Reduced elevator deflection", np.multiply(data[17][1],deg_to_rad) -  Cmtc/Cmde * (Tcs - Tc)])





###############################################################################

