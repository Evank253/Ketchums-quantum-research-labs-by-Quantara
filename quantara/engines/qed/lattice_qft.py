# Built by Evan Ketchum — 2026-06-11T09:44:00Z
import numpy as np

class LatticeQFT:
    """Simple 2D lattice scalar field theory simulator."""
    
    def __init__(self, N: int = 12, a: float = 1.0, m: float = 1.0, lam: float = 0.1):
        """
        Initialize lattice.
        N: lattice size (N x N)
        a: lattice spacing
        m: mass parameter
        lam: coupling constant
        """
        self.N = N
        self.a = a
        self.m = m
        self.lam = lam
        self.phi = np.random.normal(0, 0.1, size=(N, N))
    
    def run(self, steps: int = 2000, dt: float = 0.01) -> np.ndarray:
        """
        Run molecular dynamics evolution.
        Returns: final field configuration as N x N array.
        """
        for _ in range(steps):
            # Simple leap-frog: compute gradient and update
            dphi = self._compute_gradient(self.phi)
            self.phi -= dt * dphi
        return self.phi
    
    def _compute_gradient(self, phi: np.ndarray) -> np.ndarray:
        """Compute gradient of action (Euler-Lagrange equation)."""
        N = self.N
        grad = np.zeros_like(phi)
        
        # Kinetic + mass term
        grad = self.m**2 * phi
        
        # Laplacian (nearest neighbor)
        for i in range(N):
            for j in range(N):
                neighbors = (
                    phi[(i+1) % N, j] + phi[(i-1) % N, j] +
                    phi[i, (j+1) % N] + phi[i, (j-1) % N]
                )
                grad[i, j] -= 2 * neighbors / (self.a**2)
        
        # Quartic interaction term
        grad += self.lam * phi**3
        
        return grad
    
    def action(self, phi: np.ndarray) -> float:
        """Compute lattice action S[phi]."""
        N = self.N
        s = 0.0
        
        # Kinetic term
        for i in range(N):
            for j in range(N):
                neighbors = (
                    phi[(i+1) % N, j] + phi[(i-1) % N, j] +
                    phi[i, (j+1) % N] + phi[i, (j-1) % N]
                )
                s += 0.5 * (phi[i, j] - neighbors / 4)**2 / self.a**2
        
        # Mass term
        s += 0.5 * self.m**2 * np.sum(phi**2)
        
        # Quartic interaction
        s += (self.lam / 4) * np.sum(phi**4)
        
        return float(s)