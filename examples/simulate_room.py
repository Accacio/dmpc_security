#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

from dmpc_security.thermal_models import *
from dmpc_security.utils import *


## Simulation parameters
Te=.25;            #= Sampling

## System definition
monozone_continuous = monozone_3R2C(5,2.5,0.5,8,5)
monozone_discrete = monozone_continuous.to_discrete(Te,method='zoh')

## Applying control
x0 = np.array(((25),(25)))
u = np.asarray([1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

tout,yout, xf = simulate_system(monozone_discrete,x0,u)
xf=np.array(xf)
print(xf.transpose())

## Plot results
plt.plot(tout,xf)
plt.legend(("Inside Air","Inside Wall"))
plt.show()
