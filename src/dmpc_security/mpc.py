#!/usr/bin/env python3

import numpy as np
from scipy import signal
from .utils import *
from dmpc_security import qp

# Gains Q and R for $\sum_{j=1}^n \|v\|^2_{Q}+\|u\|^2_{R}$
# TODO(accacio): get values from control objective v

def solve_mpc():

    # Get prediction matrices
    # P = 2*matrix([ [2, .5], [.5, 1] ])
    # q = matrix([1.0, 1.0])
    # G = matrix([[-1.0,0.0],[0.0,-1.0]])
    # h = matrix([0.0,0.0])
    # A = matrix([1.0, 1.0], (1,2))
    # b = matrix(1.0)

    Q = np.array([[1., -1.],
                  [-1., 2.]])
    p = np.array([0.0, 0.0])
    result = qp.solve(Q,p)

    return result.primal


# TODO(accacio): use tensordots to calculate F and H
# NOTE: implementation of { A, B, C } .* { D, E , F } = { A*D, B*E, C*F}
#  and { A, B, C } .^ { d, e , f } = { A^d, B^e, C^f}
def calculate_output_prediction_matrices(model,n):
    """Calculate output Prediction matrices such Y=Y_x*x0+Y_u*U
          ┏          ┓
          ┃ C * A^1  ┃
 Y_x =    ┃ C * A^2  ┃
          ┃ C * A^3  ┃
          ┃    .     ┃
          ┃    .     ┃
          ┃    .     ┃
          ┃ C * A^n  ┃
          ┗          ┛

         ┏                                   ┓
         ┃ CA^(0)B        0      …      0    ┃
 Y_u =   ┃ CA^(1)B     CA^(0)B   …      0    ┃
         ┃    .         .               .    ┃
         ┃    .          .              .    ┃
         ┃    .           .             .    ┃
         ┃ CA^(n-1)B  CA^(n-2)B  …   CA^(0)B ┃
         ┃                                   ┃
 or      ┗                                   ┛
 Y_u =  lowertriangle of toeplitz matrix created from
                    ┏               ┓T
                    ┃               ┃
                    ┃  C * A^0 * B  ┃
                    ┃  C * A^1 * B  ┃
                    ┃  C * A^2 * B  ┃
                    ┃       .       ┃
                    ┃       .       ┃
                    ┃       .       ┃
                    ┃ C * A^n-1 * B ┃
                    ┗               ┛
"""

    ny, nx = np.shape(model.C)
    nc = np.shape(model.B)[1]

    Y_x = np.array([]).reshape(0,nx)
    Y_u = np.array([]).reshape(0,n*nc)
    for i in range(n):
        line = np.array([]).reshape(ny,0)
        for j in range(n):
            if (j<i+1):
                line = np.hstack((line,model.C@np.power(model.A,i-j)@model.B))
            else:
                line = np.hstack((line,np.zeros((ny,nc))))
        Y_u = np.vstack((Y_u,line))
        Y_x = np.vstack((Y_x,model.C@np.power(model.A,i+1)))

    return Y_x, Y_u

def calculate_state_prediction_matrices(model,n):
    """Calculate state Prediction matrices such X=X_x*x0+X_x*U
          ┏       ┓
          ┃  A^1  ┃
 X_x =    ┃  A^2  ┃
          ┃  A^3  ┃
          ┃   .   ┃
          ┃   .   ┃
          ┃   .   ┃
          ┃  A^n  ┃
          ┗       ┛

         ┏                                  ┓
         ┃ A^(0)B        0      …      0    ┃
 X_u =   ┃ A^(1)B     CA^(0)B   …      0    ┃
         ┃    .         .               .   ┃
         ┃    .          .              .   ┃
         ┃    .           .             .   ┃
         ┃ A^(n-1)B  CA^(n-2)B  …   CA^(0)B ┃
         ┃                                  ┃
 or      ┗                                  ┛
 X_u =  lowertriangle of toeplitz matrix created from
                    ┏           ┓T
                    ┃           ┃
                    ┃  A^0 * B  ┃
                    ┃  A^1 * B  ┃
                    ┃  A^2 * B  ┃
                    ┃       .   ┃
                    ┃       .   ┃
                    ┃       .   ┃
                    ┃ A^n-1 * B ┃
                    ┗           ┛
"""

    nx, _ = np.shape(model.A)
    nc = np.shape(model.B)[1]

    X_x = np.array([]).reshape(0,nx)
    X_u = np.array([]).reshape(0,n*nc)
    for i in range(n):
        line = np.array([]).reshape(nx,0)
        for j in range(n):
            if (j<i+1):
                line = np.hstack((line,np.power(model.A,i-j)@model.B))
            else:
                line = np.hstack((line,np.zeros((nx,nc))))
        X_u = np.vstack((X_u,line))
        X_x = np.vstack((X_x,model.C@np.power(model.A,i+1)))

    return X_x, X_u
