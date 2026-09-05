# Simulation methodology and provenance

## Provenance

Zenodo DOI [10.5281/zenodo.18435337](https://doi.org/10.5281/zenodo.18435337) contains one published version and two PDFs. `The simulation.pdf` prints a 300 m, 48-hour RK4 model but not the source of the supplied eight-module figure. `simulation/gravityx_simulation.py` is therefore an authorized reconstruction, not recovered original source.

## Input → model → output

| Input/reference assumption | Equation/model | Output |
|---|---|---|
| Radius 100 m; RPM | `ω=2π·RPM/60`; `a=ω²r`; `g_ratio=a/9.81` | 3 RPM ≈ 1.006 g |
| Induction constant 1.265×10⁶ V·s/rad | `ε=kω` (calibrated `BLv` relationship) | 4 RPM ≈ 529.88 kV |
| 85% conversion; resistance 562 kΩ | `P_buffer=ηε²/R_eq` | 2/3/4 RPM ≈ 106/239/425 kW |
| Mass 356 kg; speed 31.4 m/s; recovery 70% | `E_recovered=0.70×½mv²` | ≈ 122.85 kJ |
| Figure reference 4.1 MPa at 3 RPM | Quadratic scaling normalized at stated point | 4.1 MPa at 3 RPM |
| CFRP reference 800 MPa | `SF=800/4.1` | ≈ 195.1× reference ratio |
| Demand 120±40 kW | 24-hour sinusoid over 48 hours | 80–160 kW |
| 3 RPM buffer + 150 kW baseline | `P_available=P_buffer+P_external` | ≈ 389 kW |

## Limitations

The stress curve is normalized to the figure’s stated point because the figure does not expose spoke geometry, mass distribution, joints, fatigue, or dynamic load cases. The ratio against 800 MPa is a model reference, not a certified structural safety factor.

The equivalent electrical resistance is the parameter associated with the final figure’s 85%-conversion buffer series. The paper also reports broader transient power ranges. Those ranges and this reconstructed series are different model presentations, not independent physical measurements.

No result represents full-scale human testing, flight qualification, or mission telemetry.
