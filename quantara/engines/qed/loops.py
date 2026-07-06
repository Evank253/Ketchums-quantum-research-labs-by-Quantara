# Built by Evan Ketchum — 2026-06-11T09:44:00Z
import numpy as np

class QEDLoopIntegrator:
    def __init__(self, alpha):
        self.alpha = alpha

    def vertex_integrand(self, k, p):
        # treat k, p as 1D vectors; use dot-products for squared norms
        k = np.asarray(k)
        p = np.asarray(p)
        denom1 = np.dot(k, k) + 1e-12
        denom2 = np.dot(k + p, k + p) + 1e-12
        return 1.0 / denom1 * 1.0 / denom2

    def monte_carlo_loop(self, n_samples=10000):
        # sample 4-vector gaussian shapes; ensure p is 4-vector
        samples = np.random.normal(size=(n_samples, 4))
        vals = []
        p = np.array([1.0, 0.0, 0.0, 0.0])
        for k in samples:
            vals.append(self.vertex_integrand(k, p))
        return self.alpha * float(np.mean(vals))

    def anomalous_moment(self):
        loop = self.monte_carlo_loop()
        return loop / (2 * np.pi)
