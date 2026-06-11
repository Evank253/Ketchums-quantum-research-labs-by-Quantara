# Built by Evan Ketchum — 2026-06-11T09:44:00Z
import argparse
from quantara.engines.qed.qed_engine import QEDEngine
from quantara.engines.qcd.qcd_engine import QCDEngine

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("engine", choices=["qed", "qcd"], help="engine to run")
    parser.add_argument("--task", default="run")
    args = parser.parse_args()

    if args.engine == "qed":
        e = QEDEngine()
        print("alpha (fine structure):", e.fine_structure())
        print("MC sample (vertex):", e.monte_carlo_vertex(n_samples=1000))
    elif args.engine == "qcd":
        q = QCDEngine()
        print("alpha_s (sample):", q.alpha_s)
        print("beta fn (nf=3):", q.beta_function(3))

if __name__ == "__main__":
    main()
