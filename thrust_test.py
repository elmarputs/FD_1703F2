# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:08:02 2017

@author: Chris
"""
from mainpart import *

#Test thrust file 
tempdiff = []
for i in range(len(data[37][1])):
    tempdiff.append(data[35][1][i] + C_to_K - T(data[37][1][i]*ft_to_m))
print data
data.append(["ISA Temperature difference", np.array(tempdiff)])
matlab = {}
matlab["Pressure Altitude"] = data[37][1]
matlab["Mach"] = data[40][1]
matlab["ISA Temperature Difference"] = data[58][1]
matlab["Left engine"] = data[3][1]
matlab["Right engine"] = data[4][1]
sp.io.savemat("matlab.dat",matlab)
data = sp.io.loadmat("matlab.dat",matlab)
print data