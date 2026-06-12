# Quantara — Modular multi-scale physics simulation kernel

This repository contains the Quantara scaffolding: QED, cosmology, and HPC stubs for rapid prototyping.

Quickstart:
- Install dependencies: pip install numpy pytest
- Run CLI examples:
  - python -m quantara.cli qed_rg
  - python -m quantara.cli lattice
  - python -m quantara.cli cosmo

Each physics engine is organized under quantara-physics-engine/ with a standard layout for core utilities, QED, QCD, electroweak, gravity, models, simulation helpers, symbolic utilities, engines, tests, and notebooks.

Built by Evan Ketchum — 2026-06-11T09:44:00Z