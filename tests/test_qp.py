#!/usr/bin/env python3

import numpy as np

from dmpc_security import qp

def test_qp_using_np_array():
    Q = np.array([[1., -1.],
                  [-1., 2.]])
    p = np.array([0.0, 0.0])
    result = qp.solve(Q,p)
    assert result.primal[0] == 0
    assert result.primal[1] == 0
