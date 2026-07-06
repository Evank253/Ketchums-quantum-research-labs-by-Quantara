# Built by Evan Ketchum — 2026-06-11T09:44:00Z
import numpy as np

def monte_carlo_loop(alpha=1/137, n_samples=10000):
    """Simple Monte Carlo integrator stub used by engines.

    Returns an alpha-scaled mean of a toy integrand for smoke testing.
    """
    samples = np.random.normal(size=(n_samples, 4))
    p = np.array([1.0, 0.0, 0.0, 0.0])
    vals = []
    for k in samples:
        denom1 = np.dot(k, k) + 1e-12
        denom2 = np.dot(k + p, k + p) + 1e-12
        vals.append(1.0 / denom1 / denom2)
    return float(alpha) * float(np.mean(vals))
