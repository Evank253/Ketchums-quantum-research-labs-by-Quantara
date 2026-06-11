# Built by Evan Ketchum — 2026-06-11T09:44:00Z
import numpy as np
from quantara.engines.qed.rg_flow import QEDRenormalizationGroup
from quantara.engines.qed.lattice_qft import LatticeQFT
from quantara.engines.cosmology.scalar_class_bridge import ScalarFieldEFTBridge


def test_qed_run_alpha_positive():
    q = QEDRenormalizationGroup(alpha0=1/137, m0=0.511)
    val = q.run_alpha(100, 0.511)
    assert val > 0


def test_lattice_run_shape():
    lat = LatticeQFT(N=6, a=1.0)
    phi = lat.run(steps=10)
    assert phi.shape == (6, 6)


def test_scalar_bridge_eos():
    model = ScalarFieldEFTBridge(w0=-1.0, wa=0.1)
    w = model.equation_of_state(0.5)
    assert isinstance(w, float)
