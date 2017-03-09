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

def load(a):
    data = sp.io.loadmat(a)
    flightdata = data["flightdata"][0][0]
    data = []
    for i in range(len(flightdata)):
        value       = flightdata[i][0][0][2][0][0][0]
        measurement = flightdata[i][0][0][0][:,0] 
        data.append([value,measurement])   
    return data                                             
