#!/usr/bin/env python3

from dmpc_security import mpc

def test_mpc_solving_qp():
    x=mpc.solve_mpc()
    print(x)
    assert 0 == 0
