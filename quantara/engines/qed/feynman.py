# Built by Evan Ketchum — 2026-06-11T09:44:00Z
import numpy as np

class QEDFeynmanRules:
    def fermion_propagator(self, p, m):
        # Scalar stub: numerator uses (p^2 + m) as a simple placeholder.
        p = np.asarray(p)
        denom = np.dot(p, p) - m**2 + 1e-12
        return 1j * (np.dot(p, p) + m) / denom

    def photon_propagator(self, k):
        k = np.asarray(k)
        return -1j / (np.dot(k, k) + 1e-12)

    def vertex(self, e):
        return -1j * e
