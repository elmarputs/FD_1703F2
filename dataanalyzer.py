# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 15:13:54 2017

@author: Chris
"""

import scipy as sp

#gives a list with data where the following indexes correspond to 
#0 Angle of attack
#1 Deflection of elevator trim
#2 Force on elevator control wheel
#3 Engine 1: Fuel mass flow
#4 Engine 2: Fuel mass flow
#5 Engine 1: Inter Turbine Temperature (ITT)
#6 Engine 2: Inter turbine temperature (ITT)
#7 Engine 1: Oil pressure
#8 Engine 2: Oil pressure
#9 Deflection of the control column (Se or DCOC)
#10 Engine 1: Fan speed (N1)
#11 Engine 1: Turbine speed (N2)
#12 Engine 2: Fan speed (N1)
#13 Engine 2: Turbine speed (N2)
#14 c
#15 c
#16 Deflection of aileron
#17 Deflection of elevator
#18 Deflection of rudder
#19 UTC Date DD:MM:YY
#20 UTC Seconds
#21 Roll Angle
#22 Pitch Angle
#23 <no description>
#24 GNSS Latitude
#25 GNSS Longitude
#26 Body Roll Rate
#27 Body Pitch Rate
#28 Body Yaw Rate
#29 Body Long Accel
#30 Body Lat Accel
#31 Body Norm Accel
#32 Along Heading Accel
#33 Cross Heading Accel
#34 Vertical Accel
#35 Static Air Temperature
#36 Total Air Temperature
#37 Pressure Altitude (1013.25 mB)
#38 Baro Corrected Altitude #1
#39 <no description>
#40 Mach
#41 Computed Airspeed
#42 True Airspeed
#43 Altitude Rate
#44 Measurement Running
#45 Number of Measurements Ready
#46 Status of graph
#47 Active Screen
#48 T
#49 RAM corrected total temperature
#50 Mass  
#51 Static Pressure
#52 Density
#53 Equivalent airspeed
#54 Lift coefficient
#55 Drag coefficient
#56 reduced equivalent airspeed
#57 reduced elevator deflection 



def load(a):
    data = sp.io.loadmat(a)
    flightdata = data["flightdata"][0][0]
    data = []
    for i in range(len(flightdata)):
        value       = flightdata[i][0][0][2][0][0][0]
        measurement = flightdata[i][0][0][0][:,0] 
        unit        = flightdata[i][0][0][1][0][0]
        data.append([value,measurement,unit])   
    return data   
    
def cal_mass(initial_mass,data,time):
    l = []
    lbs_to_kg = 0.45359237
    mass = initial_mass
    for i in range(len(data[0][1])):
        if i<>(len(data[0][1])-1):
            mass = mass - (data[3][1][i] + data[4][1][i])*lbs_to_kg/3600*(time[i+1]-time[i])
        else: 
            mass = mass - (data[3][1][i] + data[4][1][i])*lbs_to_kg/3600*(time[i]-time[i-1])
        l.append(mass)
    return l 
    
def time_to_index(h,m,s):
    seconds = h*60*60+m*60+s
    return seconds*10

    


                                          
