#!/usr/bin/env python3

from cvxopt import matrix, solvers
import numpy as np
import matplotlib.pyplot as plt

from thermal_models import *
from mpc import *


# continuous_model = monozone_3R2C(1,2,3,4,5)
continuous_model = monozone_3R2C_with_External_perturbation(1,2,3,4,5)
Sampling_Time=0.1
discrete_model = continuous_model.to_discrete(Sampling_Time)

x0 = np.array([[10],[20]])
# u = np.array([0.1, 0.1 ,1,2 ,2,2,2,2,2])*10

# t, y, x = apply_control(discrete_model,x0,u)

# solve_mpc()

# a = np.arange(25).reshape(5,5)
# b = np.arange(5)
# c = np.arange(6).reshape(2,3)
# a = np.arange(60.).reshape(3,4,5)
# b = np.arange(24.).reshape(4,3,2)
# c = np.tensordot(a,b, axes=([1,0],[0,1]))
# c.shape
# print(a)
# print(b)
# print(c)
# print(np.einsum('ii',a))
# print(np.tensordot(a,b,([1,0])))
time_simulation_hours = 2

n = 5
y_c = np.repeat(10,n)

Y_x, Y_u = calculate_output_prediction_matrices(discrete_model,n)

print(to_LaTeX(Y_x))

# TODO(accacio): use tensordots
# Mmat = discrete_model.C@discrete_model.A
# for i in range(2,n+1):
#     Mmat=np.vstack((Mmat,discrete_model.C@np.power(discrete_model.A,i)))
# F,H = calculate_output_prediction_matrices(discrete_model,n)
# print(F)
# print(H)
#         _         _
#        | C * A^1  |
# Mmat = | C * A^2  |
#        | C * A^3  |
#        |    .     |
#        |    .     |
#        |    .     |
#        | C * A^n  |
#        |_        _|
# plt.plot(t, u, 'r', alpha=0.5, linewidth=1, label='Input (kW)')
# plt.plot(t, x[:,0], 'b', alpha=0.5, linewidth=1, label='Room Temperature (°C)')
# plt.plot(t, x[:,1], '#202020', alpha=0.5, linewidth=1, label='External Temperature (°C)')
# plt.legend(loc='best')
# plt.show()
