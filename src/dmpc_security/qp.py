# [[file:../../docs/dmpc_security/qp.org::*CODE][CODE:1]]
#!/usr/bin/env python3
# CODE:1 ends here

# [[file:../../docs/dmpc_security/qp.org::*CODE][CODE:2]]
from cvxopt import matrix
from cvxopt import solvers
from numpy import array,ndarray
from dataclasses import dataclass
# CODE:2 ends here

# [[file:../../docs/dmpc_security/qp.org::*CODE][CODE:3]]
__all__ = ["QP_result","solve"]
# CODE:3 ends here

# [[file:../../docs/dmpc_security/qp.org::*CODE][CODE:4]]
@dataclass
class QP_result:
    primal: ndarray
    dual: ndarray
    lagrangian_eq: ndarray
    lagrangian_ineq: ndarray

def solve(Q,p,G=None,h=None,A=None,b=None):
# CODE:4 ends here

# [[file:../../docs/dmpc_security/qp.org::*CODE][CODE:5]]
    Q = matrix(Q) if Q is not None else None
    p = matrix(p) if p is not None else None
    G = matrix(G) if G is not None else None
    h = matrix(h) if h is not None else None
    A = matrix(A) if A is not None else None
    b = matrix(b) if b is not None else None
# CODE:5 ends here

# [[file:../../docs/dmpc_security/qp.org::*CODE][CODE:6]]
    solvers.options['show_progress'] = False

    sol=solvers.qp(Q, p, G, h, A, b)
# CODE:6 ends here

# [[file:../../docs/dmpc_security/qp.org::*CODE][CODE:7]]
    primal = array(sol['x'])
    dual = array(sol['y'])
    lagrangian_eq = array(sol['y'])
    lagrangian_ineq = array(sol['z'])
    return QP_result(primal,dual,lagrangian_eq,lagrangian_ineq)
# CODE:7 ends here
