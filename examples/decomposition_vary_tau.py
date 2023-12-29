#!/usr/bin/env python3

from cvxopt import matrix, solvers
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

from dmpc_security.thermal_models import *
from dmpc_security.mpc import *
import dmpc_security.utils as ut

## Simulation parameters
Te=.25;            #= Sampling
Np=2;              #= Prediction horizon
a=10;              #= for rho=1/(a+b*negot)
b=0.1;             #=
simK = 10;         #= Simulation horizon
negotP = 100;      #= max # of iteration for each negotiation
err_theta=1e-4;    #= err to test theta convergence in each negotiation
# rand('seed',2);

#= System definition
A=np.array((0.8,0.6,0.4))
B=np.array((0.3,0.5,0.6))
C=np.zeros((1,1))
D=np.zeros((1,1))

sys = [signal.StateSpace(A[i],B[i],C,D,dt=Te) \
       for i in range(np.size(A))]

#= Initial state
# x0 = np.atleast_3d(((3,),(2,),(1,)))
x0 = np.array(((3,),(2,),(1,))).transpose()

#= Setpoint/References
wt = np.array(((x0[0][0]*1.07,), \
               (x0[0][1]*1.10,), \
               (x0[0][2]*1.05,), \
               )).transpose()
wt_final = np.array((wt[0][0]*1.05, \
                     wt[0][1]*1.05, \
                     wt[0][2]*1.05, \
                     ))
wt_change_time = np.array((simK/2,
                           simK,
                           simK,
                           simK,
                           ))

#= Global constraint
Umax=4; #= max value

#= Input bounds
u_min=-np.inf;
u_max=Umax;
