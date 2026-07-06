# Built by Evan Ketchum — 2026-06-11T09:44:00Z
import numpy as np

class QEDRenormalizationGroup:
    """QED renormalization group flow solver."""
    
    def __init__(self, alpha0: float = 1/137, m0: float = 0.511):
        """Initialize with fine structure constant and electron mass (MeV)."""
        self.alpha0 = alpha0
        self.m0 = m0
    
    def run_alpha(self, mu: float, m: float) -> float:
        """
        Run coupling constant to energy scale mu using 1-loop beta function.
        mu: energy scale (GeV)
        m: mass scale (GeV)
        Returns: alpha(mu)
        """
        # 1-loop QED beta: d(alpha)/d(ln mu) = alpha^2 / (3*pi) * N_f
        # Simplified: alpha(mu) ≈ alpha0 / (1 - (alpha0/3pi) * ln(mu/m))
        beta_coeff = self.alpha0 / (3 * np.pi)
        scale_ratio = np.log(max(mu, m) / max(m, 1e-6))
        denom = 1.0 - beta_coeff * scale_ratio
        if denom <= 0:
            return self.alpha0  # Landau pole protection
        return self.alpha0 / denom
    
    def two_loop_g_minus_2(self, alpha: float) -> float:
        """
        Compute 2-loop contribution to electron g-2 (Schwinger term).
        Returns: a_e = (g-2)/2 in units where alpha/pi is the coupling.
        """
        # Leading: a_e^(1) = alpha/pi
        # 2-loop: a_e^(2) ≈ (alpha/pi)^2 * (C2 - pi^2/3)
        leading = alpha / np.pi
        c2 = 1.25  # rough numerical coefficient
        two_loop = (alpha / np.pi)**2 * (c2 - np.pi**2 / 3)
        return leading + two_loop