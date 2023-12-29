#!/usr/bin/env python3

from dmpc_security import qp
from cvxopt import matrix

Q = 2*matrix([ [2, .5], [.5, 1] ])
p = matrix([1.0, 1.0])
G = matrix([[-1.0,0.0],[0.0,-1.0]])
h = matrix([0.0,0.0])
A = matrix([1.0, 1.0], (1,2))
b = matrix(1.0)
result = qp.solve(Q,p,G,h,A,b)


print(result)
