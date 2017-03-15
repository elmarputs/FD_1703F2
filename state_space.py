# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 14:12:26 2017

@author: Chris
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 10:47:01 2017

@author: Chris
"""

import numpy as np
import control
 


def state_space2(Clr,Clda,muc,c,V,CZa,Cmadot,KY2,CXu,CXa,CZq,CZu,CX0,Cmu,Cma,Cmq,CXde,CZde,Cmde,CYbdot,b,mub,KX2,KXZ,KZ2,CYb,Cl,CYp,CYr,Clb,Clp,Cnb,Cnp,Cnr,CYda,Cldr,Cnda,Cndr,CYdr):
    #SYMETRIC FLIGHT CONDITIONS
    
    CS1 = np.matrix( [[-2*muc*c/V/V,0,0,0],    [0,(CZa-2*muc)*c/V,0,0],[0,0,-c/V,0],[0,Cmadot*c/V,0,-2*muc*KY2*c*c/V/V] ])
    CS2 = np.matrix([ [CXu/V,CXa,CZq,CXu*c/V ],[CZu/V, CZa, -CX0 , c/V*(CZq+2*muc) ], [ 0,0,0,c/V ], [ Cmu/V,Cma,0,Cmq*c/V ]])
    CS3 = np.matrix( [[CXde],[CZde],[0],[Cmde]])
    
    A_s = -CS1**(-1)*CS2
    B_s = -CS1**(-1)*CS3
    C_s = np.matrix([ [1,0,0,0 ],[0,1,0,0 ], [ 0,0,1,0 ], [ 0,0,0,1 ]])
    D_s = np.matrix( [[0],[0],[0],[0]])
    
    sys_sym = control.StateSpace(A_s,B_s,C_s,D_s)
    
    
    #ASYMMETRIC FLIGHT CONDITIONS
    CA1 = np.matrix( [[(CYbdot-2*mub)*b/V,0,0,0],    [0,-b/2/V,0,0],[0,0,-4*mub*KX2*b*b/2/V/V,4*mub*KXZ*b*b/2/V/V],[Cnb*b/V,0,4*mub*KXZ*b*b/2/V/V,-4*mub*KZ2*b*b/2/V/V] ])
    CA2 = np.matrix([ [CYb,Cl,CYp*b/V/2,(CYr-4*mub)*b/2/V ],[0, 0, b/V/2 , 0 ], [ Clb,0,Clp*b/2/V,Clr*b/2/V ], [ Cnb,0,Cnp*b/2/V,Cnr*b/2/V ]])
    CA3 = np.matrix( [[CYda,CYdr],[0,0],[Clda,Cldr],[Cnda,Cndr]])
    
    A_a = -CA1**(-1)*CA2
    B_a = -CA1**(-1)*CA3
    C_a = np.matrix([ [1,0,0,0 ],[0,1,0,0 ], [ 0,0,1,0 ], [ 0,0,0,1 ]])
    D_a = np.matrix( [[0,0],[0,0],[0,0],[0,0]])
    
    sys_asym = control.StateSpace(A_a,B_a,C_a,D_a)
    
    return sys_sym, sys_asym
    
    
