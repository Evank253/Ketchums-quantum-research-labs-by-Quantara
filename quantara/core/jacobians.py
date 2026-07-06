# Pure finite-difference Jacobian utilities (pure math)
import numpy as np

def fd_jacobian(f, y, t, eps=1e-8, *args, **kwargs):
    y = np.asarray(y)
    n = y.size
    f0 = np.asarray(f(y, t, *args, **kwargs))
    J = np.zeros((n, n))
    for i in range(n):
        y_pert = y.copy()
        h = eps * max(1.0, abs(y[i]))
        y_pert[i] += h
        fi = np.asarray(f(y_pert, t, *args, **kwargs))
        J[:, i] = (fi - f0) / h
    return J
