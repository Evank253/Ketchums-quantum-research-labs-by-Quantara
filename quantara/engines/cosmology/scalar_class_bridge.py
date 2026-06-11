# Built by Evan Ketchum — 2026-06-11T09:44:00Z
"""
Minimal scalar-field EFT bridge used by the CLI and tests.
Provides a small equation_of_state(a) = w0 + wa*(1-a).
"""
from typing import Any

class ScalarFieldEFTBridge:
    def __init__(self, w0: float = -1.0, wa: float = 0.0, lambda_param: float = 1.0):
        self.w0 = w0
        self.wa = wa
        self.lambda_param = lambda_param

    def equation_of_state(self, a: float) -> float:
        """Return simple CPL-like equation of state w(a)=w0+wa*(1-a)."""
        return float(self.w0 + self.wa * (1.0 - a))
