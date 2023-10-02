# Custom MATLAB Functions: null(), and svds()
# Haleh Soleimany, September 2023

import numpy as np

def null(a, rtol=1e-5):
    """Customing null function."""
    if a.size == 0:
        result = np.empty((0,0))
        return result
    else:
        u, s, v = np.linalg.svd(a)
        rank = (s > rtol*s[0]).sum() 
    return v[rank:].T.copy()

def svds(A, k):
    """Customing svds function."""
    if A.size == 0:
        W = np.empty((0,18))
        S = np.zeros((18,18))
        V = np.empty((0,18)).T
    else:
        [W,S,V] = np.linalg.svd(A)
        S = np.diag(S)
    return W, S, V