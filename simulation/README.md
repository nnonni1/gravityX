# GravityX simulation reconstruction

This directory contains a reproducible reconstruction of the supplied comprehensive GravityX figure. Its original source is not present in Zenodo DOI `10.5281/zenodo.18435337`; this file must not be described as the original archived source.

The reconstruction preserves named equations and displayed reference values without presenting them as physical measurements. Assertions stop execution if primary outputs drift beyond the figure’s rounding tolerances.

## Requirements and run

- Python 3.11+
- NumPy 2.3.3
- Matplotlib 3.10.6

```bash
pip install -r simulation/requirements.txt
python simulation/gravityx_simulation.py
```

Expected output: `assets/simulation/gravityx-reconstructed-simulation.png`.

## Provenance boundary

- **Archived model:** 300 m, 48-hour RK4 source printed in Zenodo’s `The simulation.pdf`.
- **Comprehensive figure:** supplied eight-module image.
- **This script:** authorized reconstruction of that figure because its original plotting source is absent from the DOI.
