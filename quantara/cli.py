# Built by Evan Ketchum — 2026-06-11T09:44:00Z

import argparse
from quantara.engines.qed.rg_flow import QEDRenormalizationGroup
from quantara.engines.qed.lattice_qft import LatticeQFT
from quantara.engines.cosmology.scalar_class_bridge import ScalarFieldEFTBridge

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("engine")
    parser.add_argument("--task", default="run")
    args = parser.parse_args()

    if args.engine == "qed_rg":
        qed = QEDRenormalizationGroup(alpha0=1/137, m0=0.511)
        print("alpha(mu=100 GeV):", qed.run_alpha(100, 0.511))
        print("a_e (2-loop):", qed.two_loop_g_minus_2(1/137))
    elif args.engine == "lattice":
        lat = LatticeQFT(N=12)
        phi = lat.run(steps=2000)
        print("lattice energy:", lat.action(phi))
    elif args.engine == "cosmo":
        model = ScalarFieldEFTBridge(w0=-1.0, wa=0.1, lambda_param=50)
        print("w(a=0.5):", model.equation_of_state(0.5))
    else:
        print("Unknown engine")
# Lightweight CLI shim left at original location to preserve scripts that call it.
# Delegates to quantara.cli.main; this file is a MOVE wrapper and not a physics layer.
from quantara.cli.main import main

if __name__ == "__main__":
    main()
