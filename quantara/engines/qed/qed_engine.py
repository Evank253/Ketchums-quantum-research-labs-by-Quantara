# Built by Evan Ketchum — 2026-06-11T09:44:00Z
from quantara.engines.qed.rg_flow import QEDRenormalizationGroup
from quantara.sim.monte_carlo import monte_carlo_loop

class QEDEngine:
    """Medium-completeness QEDEngine: pure physics interface, no I/O.

    Methods:
      - fine_structure()
      - perturbation_order(n)
      - scattering_amplitude(diagram)  # expects diagram.evaluate()
      - running_coupling(q2, mu0)

    This engine delegates numerical tasks to quantara.sim for Monte Carlo / integrators.
    """
    def __init__(self, alpha=1/137.035999084, mass_e=0.5109989461):
        self.alpha = float(alpha)
        self.m_e = float(mass_e)
        self._rg = QEDRenormalizationGroup(alpha0=self.alpha, m0=self.m_e)

    def fine_structure(self):
        return self.alpha

    def perturbation_order(self, n):
        import math
        return (self.alpha / math.pi) ** n

    def scattering_amplitude(self, diagram):
        # diagram is expected to implement evaluate() -> numeric amplitude
        return diagram.evaluate()

    def running_coupling(self, q2, mu0=1.0):
        # q2 is squared momentum scale; forward to RG implementation
        # provide a lightweight wrapper using the RG class's run_alpha-like API
        # our RG accepts mu and mu0; treat q2 and mu0 as scale proxies
        mu = float(q2)
        return self._rg.run_alpha(mu, mu0)

    def monte_carlo_vertex(self, n_samples=10000):
        # expose a simple simulation hook using sim.monte_carlo_loop
        return monte_carlo_loop(alpha=self.alpha, n_samples=n_samples)
