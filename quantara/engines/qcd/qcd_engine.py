# Built by Evan Ketchum — 2026-06-11T09:44:00Z
import math

class QCDEngine:
    """Medium-completeness QCDEngine: running coupling and beta function.

    Simple perturbative beta-function + running coupling wrapper.
    """
    def __init__(self, alpha_s=0.118, n_colors=3):
        self.alpha_s = float(alpha_s)
        self.Nc = int(n_colors)

    def beta_function(self, nf):
        # one-loop coefficient (perturbative)
        return (11 * self.Nc - 2 * nf) / (12 * math.pi)

    def running_coupling(self, q2, Lambda_QCD=0.2):
        # q2 and Lambda in GeV^2 units roughly; simple one-loop model
        b0 = self.beta_function(nf=3)
        return 4 * math.pi / (b0 * math.log(q2 / (Lambda_QCD ** 2) + 1e-12))

    def confinement_scale(self):
        return "non-perturbative regime"
