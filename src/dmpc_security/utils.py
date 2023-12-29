#!/usr/bin/env python3

import numpy as np

# inspired from https://stackoverflow.com/a/17131750/9781176
# TODO(accacio): choose if small etc
def smallmatrix(a):
    """Returns a LaTeX smallmatrix
    :a: numpy array
    :returns: LaTeX bmatrix as a string
    """
    if len(a.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    lines = str(a).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{smallmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv +=  [r'\end{smallmatrix}']
    return '\n'.join(rv)
def latex_matrix(a):
    """Returns a LaTeX smallmatrix
    :a: numpy array
    :returns: LaTeX bmatrix as a string
    """
    lines = str(a).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{matrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv +=  [r'\end{matrix}']
    return '\n'.join(rv)

def to_LaTeX(variable):
    return latex_matrix(variable)
