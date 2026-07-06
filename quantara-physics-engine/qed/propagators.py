# quantara-physics-engine/qed/propagators.py
# Built by Evan Ketchum — 2026-06-11T09:44:00Z

def fermion_prop(p, m):
    return 1j / (p**2 - m**2 + 1e-12)
