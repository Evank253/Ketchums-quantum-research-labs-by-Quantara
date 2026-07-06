# Update tests to import engines from new paths
# Built by Evan Ketchum — 2026-06-11T09:44:00Z
import numpy as np
from quantara.engines.qed.qed_engine import QEDEngine
from quantara.engines.qcd.qcd_engine import QCDEngine
from quantara.sim.monte_carlo import monte_carlo_loop


def test_qed_engine_runs():
    e = QEDEngine()
    assert e.fine_structure() > 0
    v = e.monte_carlo_vertex(n_samples=100)
    assert isinstance(v, float)


def test_qcd_engine_runs():
    q = QCDEngine()
    assert q.Nc == 3
    assert callable(q.beta_function)


def test_monte_carlo_stub():
    val = monte_carlo_loop(alpha=1/137, n_samples=100)
    assert isinstance(val, float)
