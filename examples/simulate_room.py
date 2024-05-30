#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

from dmpc_security.thermal_models import *
from dmpc_security.utils import *


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
monozone_continuous = monozone_3R2C(0.01,2.5,0.5,8,5)
monozone_discrete = monozone_continuous.to_discrete(1,method='zoh')
# Cs=[8 7 9 6];       % c walls
# Cres=[5 4 4.5 4.7]; % c inside air
# Rf=[5 6 4 5];       % r inside air and outside air (windows)
# Ri=[2.5 2.3 2 2.2]; % r inside air inside walls
# Ro=[0.5 1 0.8 0.9];

x0 = np.array(((3),(2)))
u = np.asarray([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

tout,yout, xf = simulate_system(monozone_discrete,x0,u)
xf=np.array(xf)
print(xf.transpose())

## Plot results
plt.plot(tout,xf)
plt.legend(("Inside Air","Inside Wall"))
plt.show()
