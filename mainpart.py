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
import scipy.io as sp

import control
import matplotlib.pyplot
from dataanalyzer import load,cal_mass, time_to_index
from state_space import state_space2
from Calc_ISA import T
from Variables import * 
import matplotlib.pyplot as plt 

#Create state space system for symmetric and asymmetric case
sys_sym, sys_asym = state_space2(CZ0,CXq,CZadot,Cnbdot,Clr,Clda,muc,c,V,CZa,Cmadot,KY2,CXu,CXa,CZq,
                                 CZu,CX0,Cmu,Cma,Cmq,CXde,CZde,Cmde,CYbdot,b,
                                 mub,KX2,KXZ,KZ2,CYb,CL,CYp,CYr,Clb,Clp,Cnb,
                                 Cnp,Cnr,CYda,Cldr,Cnda,Cndr,CYdr)
#control.matlab.damp(sys_asym)
#outputs of symetrical case : 0 velocity 1 angle of attack 2 pitch angle 3 pitch rate 
#outputs of asymetrical case: 0 slip     1 roll            3 roll rate   4 yaw rate


##############################################################################
##############   Symetric graphs presentation       ##########################
##############################################################################

##Control inputs to symetrical case of phugoid (step on elevator)
#
#plt.clf()
#inpu = np.concatenate((np.ones(1)*-0.005,np.zeros(99999))) 
#l = control.forced_response(sys_sym, T=np.arange(0,1000,0.01), U=inpu)
#
###Phugoid
#plt.clf()
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.xlabel("Time (s)")
#plt.ylabel("Velocity difference (m/s)")
#plt.plot(l[0],l[1][0])
#plt.savefig("V_t_phugoid")
#
#
#plt.clf()
##plt.ylim(-0.5*10**-3,0.5*10**-3)
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.xlabel("Time (s)")
#plt.ylabel("Angle of attack (rad)")
#plt.plot(l[0],l[1][1])
#plt.savefig("AOA_t_phugoid")
#
#plt.clf()
##plt.ylim(-0.8*10**-2,0.8*10**-2)
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.xlabel("Time (s)")
#plt.ylabel("Pitch angle (rad)")
#plt.plot(l[0],l[1][2])
#plt.savefig("theta_t_phugoid")
#
#plt.clf()
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.xlabel("Time (s)")
#plt.ylabel("Pitch rate (rad/s)")
##plt.ylim(-1*10**-3,1*10**-3)
#plt.plot(l[0],l[1][3])
#plt.savefig("q_t_phugoid")
#
#
#
###Control inputs to symetrical case of short period 
#inpu = np.concatenate((np.zeros(1),np.ones(99999)*-0.005)) 
#l = control.forced_response(sys_sym, T=np.arange(0,1000,0.01), U=inpu)
#
#plt.clf()
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.xlabel("Time (s)")
#plt.xlim(0,10)
#plt.ylabel("Pitch rate (rad/s)")
#plt.plot(l[0],l[1][3])
#plt.savefig("q_t_short_period")
#
#
#
#
#
################################################################################
#
#
#
#
#
#
#
#plt.clf()
#inpu = np.concatenate((np.ones(1)*-0.005,np.zeros(99999))) 
#l = control.forced_response(sys_sym, T=np.arange(0,1000,0.01), U=inpu)
#
#plt.clf()
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.xlabel("Time (s)")
#plt.ylabel("Velocity difference (m/s)")
#plt.plot(l[0],l[1][0])
#plt.show()
#plt.savefig("V_t_phugoid")
#
#
#plt.clf()
##plt.ylim(-0.5*10**-3,0.5*10**-3)
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.xlabel("Time (s)")
#plt.ylabel("Angle of attack (rad)")
#plt.plot(l[0],l[1][1])
#plt.savefig("AOA_t_phugoid")
#
#plt.clf()
##plt.ylim(-0.8*10**-2,0.8*10**-2)
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.xlabel("Time (s)")
#plt.ylabel("Pitch angle (rad)")
#plt.plot(l[0],l[1][2])
#plt.savefig("theta_t_phugoid")
#
#plt.clf
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.xlabel("Time (s)")
#plt.ylabel("Pitch rate (rad/s)")
##plt.ylim(-1*10**-3,1*10**-3)
#plt.plot(l[0],l[1][3])
#plt.savefig("q_t_phugoid")
#
#
#
###Control inputs to symetrical case of short period 
#inpu = np.concatenate((np.zeros(1),np.ones(99999)*-0.005)) 
#l = control.forced_response(sys_sym, T=np.arange(0,1000,0.01), U=inpu)
#
#plt.clf()
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.xlabel("Time (s)")
#plt.xlim(0,10)
#plt.ylabel("Pitch rate (rad/s)")
#plt.plot(l[0],l[1][3])
#plt.savefig("q_t_short_period")



###############################################################################
###############   Asymetric graphs presentation      ##########################
###############################################################################
#
#
###Aperiodic roll : impulse input on ailleron 
#inpu=[]
#inpu.append(  np.concatenate((np.ones(100)*-0.025,np.zeros(99900)) ) )   #aillerion input
#inpu.append(  np.concatenate((np.ones(1)*0,np.zeros(99999)))  ) #rudder input
#l = control.forced_response(sys_asym, T=np.arange(0,1000,0.01), U=inpu)
#
#plt.clf()
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.xlabel("Time (s)")
#plt.ylabel("Roll rate (rad/s)")
#plt.ylim(-1*10**-2,0.07)
#plt.xlim(0,15)
#plt.plot(l[0],l[1][2])
#plt.savefig("p_t_aperiodic")
#
###Dutch roll : inital yaw angle
#inpu=[]
#inpu.append(  np.concatenate((np.zeros(100)*-0.025,np.zeros(99900)) ) )   
#inpu.append(  np.concatenate((np.zeros(1)*0,np.zeros(99999)))  ) 
#l = control.forced_response(sys_asym, T=np.arange(0,1000,0.01), U=inpu,X0=[pi/4,0,0,0])
#
#plt.clf()
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.xlabel("Time (s)")
#plt.ylabel("Sideslip angle (rad)")
#plt.ylim(-0.5,0.9)
#plt.xlim(0,15)
#plt.plot(l[0],l[1][0])
#plt.savefig("sideslip_dutch_roll")
#
#plt.clf()
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.xlabel("Time (s)")
#plt.ylabel("Roll angle (rad)")
#plt.ylim(-0.5,0.9)
#plt.xlim(0,15)
#plt.plot(l[0],l[1][1])
#plt.savefig("roll_dutch_roll")
#
###Spiral : set inital roll angle
#inpu = []
#inpu.append(  np.concatenate((np.zeros(100)*0.0,np.zeros(99900)) ) )   #aillerion input
#inpu.append(  np.concatenate((np.zeros(1)*0,np.zeros(99999)))  ) #rudder input
#l = control.forced_response(sys_asym, T=np.arange(0,1000,0.01), U=inpu, X0=[0,pi/4,0,0])
#
#plt.clf()
#plt.ticklabel_format(style="sci",axis="y",scilimits=(0,0))
#plt.xlabel("Time (s)")
#plt.ylabel("Roll angle (rad)")
#plt.ylim(0.7,1)
#plt.xlim(0,15)
#plt.plot(l[0],l[1][1])
#plt.savefig("roll_angle_spiral")

#

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
data.append(["Pressure",p0*(1+lambd*data[37][1]*ft_to_m/T0)**(-g/lambd/R)]) #static pressure at each instant 
data.append(["Density",np.divide(data[51][1],R)/(data[35][1]+C_to_K)])     #density at each instant
data.append(["Equivalent Air Speed",data[42][1]*knots_to_ms*np.sqrt(data[52][1]/rho0)])   #EAS at each instant 
data.append(["Lift Coefficient",np.multiply(2*g,data[50][1])/(data[52][1]*np.multiply(np.square(data[53][1]), S))])     #Lift coefficient at each isntant 
#data.append(["Drag Coefficient",CD0 + np.square(data[54][1])/(np.pi*e*A)])  #drag coefficient at each instant 
#To plot elevator deflection with airspeed
data.append(["Reduced equivalent airspeed", np.multiply(data[53][1], np.divide(Ws,np.multiply(data[50][1],g))  )    ])
data.append(["Reduced elevator deflection", np.multiply(data[17][1],deg_to_rad) -  Cmtc/Cmde * (Tcs - Tc)])

##############   Validation     ##################################
##############################################################################

##############Phugoid######################################################
index = time_to_index(1,05,15)

sys_sym, sys_asym = state_space2( (-data[50][1][index] * g * cos(data[22][1][index]*deg_to_rad) / (0.5 * data[52][1][index] * (data[42][1][index]*knots_to_ms) ** 2 * S)),CXq,CZadot,Cnbdot,Clr,Clda,data[50][1][index] / (data[52][1][index] * S * c),c,data[42][1][index]*knots_to_ms,CZa,Cmadot,KY2,CXu,CXa,CZq,
                                 CZu,data[50][1][index]*g * sin(data[22][1][index]*deg_to_rad) / (0.5 * data[52][1][index] * (data[42][1][index]*knots_to_ms) ** 2 * S),Cmu,Cma,Cmq,CXde,CZde,Cmde,CYbdot,b,
                                 data[50][1][index] / (data[52][1][index] * S * b) ,KX2,KXZ,KZ2,CYb,data[54][1][index] ,CYp,CYr,Clb,Clp,Cnb,
                                 Cnp,Cnr,CYda,Cldr,Cnda,Cndr,CYdr)
plt.clf()
#Experimental
plt.plot(np.divide(range(len(data[27][1][index:index+1220])),10.)        
                    , (data[42][1][index:index+1220] - data[42][1][index])*knots_to_ms
                    , label="Experimental")
#Numerical
inpu = data[17][1][index:index+1220]*deg_to_rad
l = control.forced_response(sys_sym, T=np.arange(0,len(inpu))/10., U=-inpu,X0=[0,data[0][1][index]*deg_to_rad,data[22][1][index]*deg_to_rad,data[27][1][index]*deg_to_rad])
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xlabel("Time (s)")
plt.xlim(0,122)
plt.ylabel("Velocity Difference (m/s)")
plt.plot(l[0],l[1][0],label="Numerical")
plt.legend()
plt.savefig("phugoid_validation_1")


a = (data[42][1][index:index+1220] - data[42][1][index])*knots_to_ms
period = (np.where(a==np.min(a[0:200]))[0] - np.where(a==np.min(a[300:600]))[0] )*0.1*-1
print "The period of the phugoid motion is equal to", period[0],"s"
max1 = np.max(a[100:400])
max2 = np.max(a[500:700])
max3 = np.max(a[900:1100])
x = [np.where([a==max1])[1][0],np.where([a==max2])[1][0],np.where([a==max3])[1][0]]
y=[max1,max2,max3]
z = np.polyfit(x,y,5)
x = np.linspace(0,1200,1200)
y = z[0]*x**5+z[1]*x**4+z[2]*x**3+z[3]*x**2+z[4]*x**1+z[5]*x**0
plt.plot(x,y)
#
#

#
#sys_sym, sys_asym = state_space2( (-1.2*data[50][1][index] * g * cos(data[22][1][index]*deg_to_rad) / (0.5 * data[52][1][index] * (data[42][1][index]*knots_to_ms) ** 2 * S)),CXq,CZadot,Cnbdot,Clr,Clda,data[50][1][index] / (data[52][1][index] * S * c),c,data[42][1][index]*knots_to_ms,CZa,Cmadot,KY2,CXu,CXa,CZq,
#                                 1.5*CZu,data[50][1][index]*g * sin(data[22][1][index]*deg_to_rad) / (0.5 * data[52][1][index] * (data[42][1][index]*knots_to_ms) ** 2 * S),Cmu,Cma,Cmq,CXde,CZde,Cmde,CYbdot,b,
#                                 data[50][1][index] / (data[52][1][index] * S * b) ,KX2,KXZ,KZ2,CYb,data[54][1][index] ,CYp,CYr,Clb,Clp,Cnb,
#                                 Cnp,Cnr,CYda,Cldr,Cnda,Cndr,CYdr)
#plt.clf()
##Experimental
#plt.plot(np.divide(range(len(data[27][1][index:index+1220])),10.)        
#                    , (data[42][1][index:index+1220] - data[42][1][index])*knots_to_ms
#                    , label="Experimental")
##Numerical
#inpu = data[17][1][index:index+1220]*deg_to_rad
#l = control.forced_response(sys_sym, T=np.arange(0,len(inpu))/10., U=-inpu,X0=[0,data[0][1][index]*deg_to_rad,data[22][1][index]*deg_to_rad,data[27][1][index]*deg_to_rad])
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.xlabel("Time (s)")
#plt.xlim(0,122)
#plt.ylabel("Velocity Difference (m/s)")
#plt.plot(l[0],l[1][0],label="Numerical")
#plt.legend()
#plt.savefig("phugoid_validation_2")

#Short period#################################################
index = time_to_index(1,03,47)
#sys_sym, sys_asym = state_space2( (-data[50][1][index] * g * cos(data[22][1][index]*deg_to_rad) / (0.5 * data[52][1][index] * (data[42][1][index]*knots_to_ms) ** 2 * S)),CXq,CZadot,Cnbdot,Clr,Clda,data[50][1][index] / (data[52][1][index] * S * c),c,data[42][1][index]*knots_to_ms,CZa,Cmadot,KY2,CXu,CXa,CZq,
#                                 CZu,data[50][1][index]*g * sin(data[22][1][index]*deg_to_rad) / (0.5 * data[52][1][index] * (data[42][1][index]*knots_to_ms) ** 2 * S),Cmu,Cma,Cmq,CXde,CZde,Cmde,CYbdot,b,
#                                 data[50][1][index] / (data[52][1][index] * S * b) ,KX2,KXZ,KZ2,CYb,data[54][1][index] ,CYp,CYr,Clb,Clp,Cnb,
#                                 Cnp,Cnr,CYda,Cldr,Cnda,Cndr,CYdr)
#plt.clf()
#
##Experimental
#plt.plot(np.divide(range(len(data[27][1][index:index+90])),10.)        
#                    , np.multiply(data[27][1][index:index+90],deg_to_rad) 
#                    , label="Experimental")
##Numerical
#inpu = data[17][1][index:index+90]*deg_to_rad 
#l = control.forced_response(sys_sym, T=np.arange(0,len(inpu))/10., U=inpu,X0=[0,data[0][1][index]*deg_to_rad,data[22][1][index]*deg_to_rad,data[27][1][index]*deg_to_rad])
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.xlabel("Time (s)")
#plt.xlim(0,10)
#plt.ylabel("Pitch rate (rad/s)")
#plt.plot(l[0],l[1][3],label="Numerical")
#plt.legend()
#plt.savefig("short_period_validation")



####Aperiodic roll#########################################
#index = time_to_index(1,10,46)
#
#sys_sym, sys_asym = state_space2( (-data[50][1][index] * g * cos(data[22][1][index]*deg_to_rad) / (0.5 * data[52][1][index] * (data[53][1][index]*knots_to_ms) ** 2 * S)),CXq,CZadot,Cnbdot,Clr,Clda,data[50][1][index] / (data[52][1][index] * S * c),c,data[53][1][index]*knots_to_ms,CZa,Cmadot,KY2,CXu,CXa,CZq,
#                                 CZu,data[50][1][index]*g * sin(data[22][1][index]*deg_to_rad) / (0.5 * data[52][1][index] * (data[53][1][index]*knots_to_ms) ** 2 * S),Cmu,Cma,Cmq,CXde,CZde,Cmde,CYbdot,b,
#                                 data[50][1][index] / (data[52][1][index] * S * b) ,KX2,KXZ,KZ2,CYb,data[54][1][index] ,CYp,CYr,Clb,Clp,Cnb,
#                                 Cnp,Cnr,CYda,Cldr,Cnda,Cndr,CYdr)
#inpu=[]
#inpu.append( data[16][1][index+53:index+500] * deg_to_rad )   #aillerion input
#inpu.append( data[18][1][index+53:index+500]  * deg_to_rad)   #rudder input
#l = control.forced_response(sys_asym, T=np.arange(0,len(inpu[0]))/10., U=inpu,X0 = [0,data[21][1][index]*deg_to_rad,data[26][1][index]*deg_to_rad,data[28][1][index]*deg_to_rad])
#
#plt.clf()
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.xlabel("Time (s)")
#plt.ylabel("Roll rate (rad/s)")
#plt.plot(l[0],l[1][2],label="Numerical")
#plt.savefig("p_t_aperiodic")
#plt.plot(    np.divide( range(len(data[26][1][index+53:index+500])),10. )  ,      data[26][1][index+53:index+500] *deg_to_rad ,label="Experimental"  )
#plt.legend()
##plt.savefig("aperiodic_validation")
#

#
##Dutch roll#############################################
#index = time_to_index(1,07,51)
#
#sys_sym, sys_asym = state_space2( (-data[50][1][index] * g * cos(data[22][1][index]*deg_to_rad) / (0.5 * data[52][1][index] * (data[42][1][index]*knots_to_ms) ** 2 * S)),CXq,CZadot,Cnbdot,Clr,Clda,data[50][1][index] / (data[52][1][index] * S * c),c,V,CZa,Cmadot,KY2,CXu,CXa,CZq,
#                                 CZu,data[50][1][index]*g * sin(data[22][1][index]*deg_to_rad) / (0.5 * data[52][1][index] * (data[42][1][index]*knots_to_ms) ** 2 * S),Cmu,Cma,Cmq,CXde,CZde,Cmde,CYbdot,b,
#                                 data[50][1][index] / (data[52][1][index] * S * b) ,KX2,KXZ,KZ2,CYb,data[54][1][index] ,CYp,CYr,Clb,Clp,Cnb,
#                                 Cnp,Cnr,CYda,Cldr,Cnda,Cndr,CYdr)
#
#plt.clf()
#plt.plot(    np.divide( range(len(data[21][1][index:index+500])),10. )  ,      data[26][1][index:index+500] *deg_to_rad ,label="Experimental"  )
#
#
#inpu=[]
#inpu.append( data[16][1][index:index+500] * deg_to_rad )   #aillerion input
#inpu.append( data[18][1][index:index+500]  * deg_to_rad)   #rudder input 
#l = control.forced_response(sys_asym, T=np.arange(0,len(inpu[0]))/10., U=inpu,X0 = [0,data[21][1][index]*deg_to_rad,data[26][1][index]*deg_to_rad,data[28][1][index]*deg_to_rad])
#
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.xlabel("Time (s)")
#plt.ylabel("Roll rate (rad/s)")
#plt.ylim(-0.5,0.9)
#plt.plot(l[0],l[1][2],label = "Numerical")
#plt.legend()
#plt.savefig("dutch_roll_validation_1")



#
#plt.clf()
#plt.plot(    np.divide( range(len(data[21][1][index:index+500])),10. )  ,      data[21][1][index:index+500] *deg_to_rad ,label="Experimental"  )
#
#inpu=[]
#inpu.append( data[16][1][index:index+500] * deg_to_rad )   #aillerion input
#inpu.append( data[18][1][index:index+500]  * deg_to_rad)   #rudder input 
#l = control.forced_response(sys_asym, T=np.arange(0,len(inpu[0]))/10., U=inpu,X0 = [0,data[21][1][index]*deg_to_rad,data[26][1][index]*deg_to_rad,data[28][1][index]*deg_to_rad])
#
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.xlabel("Time (s)")
#plt.ylabel("Roll angle (rad)")
#plt.xlim(0,100)
##plt.ylim(-0.5,0.9)
#plt.plot(l[0],l[1][1],label = "Numerical")
#plt.legend()
#plt.savefig("dutch_roll_validation_2")

###Spiral###################################################
#index = time_to_index(1,12,54)
#print data[50][1][index] / (data[52][1][index] * S * b)
#
#
#sys_sym, sys_asym = state_space2( (-data[50][1][index] * g * cos(data[22][1][index]*deg_to_rad) / (0.5 * data[52][1][index] * (data[42][1][index]*knots_to_ms) ** 2 * S)),CXq,CZadot,Cnbdot,Clr,Clda,data[50][1][index] / (data[52][1][index] * S * c),c,V,CZa,Cmadot,KY2,CXu,CXa,CZq,
#                                 CZu,data[50][1][index]*g * sin(data[22][1][index]*deg_to_rad) / (0.5 * data[52][1][index] * (data[42][1][index]*knots_to_ms) ** 2 * S),Cmu,Cma,Cmq,CXde,CZde,Cmde,CYbdot,b,
#                                 data[50][1][index] / (data[52][1][index] * S * b) ,KX2,KXZ,KZ2,CYb,data[54][1][index] ,CYp,CYr,Clb,Clp,Cnb,
#                                 Cnp,Cnr,CYda,Cldr,Cnda,Cndr,CYdr)
#plt.clf()
#plt.plot(    np.divide( range(len(data[21][1][index:index+500])),10. )  ,      data[21][1][index:index+500]*deg_to_rad  ,label="Experimental"  )
#
#inpu=[]
#inpu.append( data[16][1][index:index+500] * deg_to_rad )   #aillerion input
#inpu.append( data[18][1][index:index+500]  * deg_to_rad)   #rudder input 
#l = control.forced_response(sys_asym, T=np.arange(0,len(inpu[0]))/10., U=inpu,X0 = [0,data[21][1][index]*deg_to_rad,data[26][1][index]*deg_to_rad,data[28][1][index]*deg_to_rad])
#
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.xlabel("Time (s)")
#plt.ylabel("Roll angle (rad)")
#plt.plot(l[0],l[1][1],label = "Numerical")
#plt.legend()
#plt.savefig("spiral_validation_1")
#plt.xlim(0,50)
#
#
#sys_sym, sys_asym = state_space2( (-data[50][1][index] * g * cos(data[22][1][index]*deg_to_rad) / (0.5 * data[52][1][index] * (data[42][1][index]*knots_to_ms) ** 2 * S)),CXq,CZadot,Cnbdot,Clr,Clda,data[50][1][index] / (data[52][1][index] * S * c),c,V,CZa,Cmadot,KY2,CXu,CXa,CZq,
#                                 CZu,data[50][1][index]*g * sin(data[22][1][index]*deg_to_rad) / (0.5 * data[52][1][index] * (data[42][1][index]*knots_to_ms) ** 2 * S),Cmu,Cma,Cmq,CXde,CZde,Cmde,CYbdot,b,
#                                 data[50][1][index] / (data[52][1][index] * S * b) ,KX2,KXZ,KZ2,CYb,data[54][1][index] ,CYp,CYr,Clb,Clp,Cnb,
#                                 Cnp,Cnr,CYda,Cldr,Cnda,-0.47*Cndr,CYdr)
#plt.clf()
#plt.plot(    np.divide( range(len(data[21][1][index:index+500])),10. )  ,      data[21][1][index:index+500]*deg_to_rad  ,label="Experimental"  )
#
#inpu=[]
#inpu.append( data[16][1][index:index+500] * deg_to_rad )   #aillerion input
#inpu.append( data[18][1][index:index+500]  * deg_to_rad)   #rudder input 
#l = control.forced_response(sys_asym, T=np.arange(0,len(inpu[0]))/10., U=inpu,X0 = [0,data[21][1][index]*deg_to_rad,data[26][1][index]*deg_to_rad,data[28][1][index]*deg_to_rad])
#
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.xlabel("Time (s)")
#plt.ylabel("Roll angle (rad)")
#plt.plot(l[0],l[1][1],label = "Numerical")
#plt.legend()
#plt.savefig("spiral_validation_2")
#plt.xlim(0,50)



###############################################################################

