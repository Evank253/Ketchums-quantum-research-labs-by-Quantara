# quantara-physics-engine/core/tensors.py
# Built by Evan Ketchum — 2026-06-11T09:44:00Z
import numpy as np

def minkowski_metric():
    return np.diag([1.0, -1.0, -1.0, -1.0])
