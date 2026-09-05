"""Authorized reconstruction of the supplied GravityX comprehensive figure.

The original plotting source is absent from the DOI. This reproducible model
uses the equations and displayed numerical references in the paper and figure.
"""

from pathlib import Path
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

G_EARTH = 9.81
HABITAT_RADIUS_M = 100.0
INDUCTION_CONSTANT_VS_PER_RAD = 1.265e6
CONVERSION_EFFICIENCY = 0.85
EQUIVALENT_RESISTANCE_OHM = 562_000.0
TRANSITION_MASS_KG = 356.0
TRANSITION_RECOVERY_EFFICIENCY = 0.70
RING_VELOCITY_M_S = 31.4
CFRP_REFERENCE_LIMIT_MPA = 800.0
DESIGN_RPM = 3.0
DESIGN_STRESS_MPA = 4.1
AVERAGE_DEMAND_KW = 120.0
PEAK_DEMAND_KW = 160.0
EXTERNAL_BASELINE_KW = 150.0


def angular_velocity(rpm):
    return np.asarray(rpm, dtype=float) * 2 * np.pi / 60


def gravity_g(rpm):
    return angular_velocity(rpm) ** 2 * HABITAT_RADIUS_M / G_EARTH


def emf_kv(rpm):
    return INDUCTION_CONSTANT_VS_PER_RAD * angular_velocity(rpm) / 1_000


def buffer_power_kw(rpm):
    emf_v = emf_kv(rpm) * 1_000
    return CONVERSION_EFFICIENCY * emf_v**2 / EQUIVALENT_RESISTANCE_OHM / 1_000


def recovered_transition_energy_kj(velocity_m_s=RING_VELOCITY_M_S):
    kinetic_j = 0.5 * TRANSITION_MASS_KG * np.asarray(velocity_m_s) ** 2
    return TRANSITION_RECOVERY_EFFICIENCY * kinetic_j / 1_000


def modeled_stress_mpa(rpm):
    """Scale from the final figure's stated 4.1 MPa design reference."""
    return DESIGN_STRESS_MPA * (np.asarray(rpm, dtype=float) / DESIGN_RPM) ** 2


def verified_outputs():
    buffer_3 = float(buffer_power_kw(3))
    return {
        "gravity_3rpm_g": float(gravity_g(3)),
        "emf_4rpm_kv": float(emf_kv(4)),
        "buffer_3rpm_kw": buffer_3,
        "transition_recovery_kj": float(recovered_transition_energy_kj()),
        "stress_3rpm_mpa": float(modeled_stress_mpa(3)),
        "safety_factor": CFRP_REFERENCE_LIMIT_MPA / float(modeled_stress_mpa(3)),
        "peak_demand_kw": PEAK_DEMAND_KW,
        "total_available_kw": buffer_3 + EXTERNAL_BASELINE_KW,
    }


def verify_reference_values(values):
    expected = {
        "gravity_3rpm_g": (1.01, 0.015),
        "emf_4rpm_kv": (530.0, 0.5),
        "buffer_3rpm_kw": (239.0, 0.5),
        "transition_recovery_kj": (123.0, 0.5),
        "stress_3rpm_mpa": (4.1, 0.01),
        "safety_factor": (195.0, 0.5),
        "peak_demand_kw": (160.0, 0.01),
        "total_available_kw": (389.0, 0.5),
    }
    for key, (target, tolerance) in expected.items():
        if abs(values[key] - target) > tolerance:
            raise AssertionError(f"{key}: {values[key]:.3f} != {target} ± {tolerance}")


def build_figure(output_path):
    rpm_points = np.arange(1, 6)
    rpm_curve = np.linspace(0.5, 5, 240)
    hours = np.linspace(0, 48, 481)
    demand = AVERAGE_DEMAND_KW + 40 * np.sin(2 * np.pi * hours / 24)
    buffer_3 = float(buffer_power_kw(3))

    fig = plt.figure(figsize=(18, 15), constrained_layout=True)
    grid = fig.add_gridspec(3, 3, height_ratios=[1, 1, 1.15])
    axes = [fig.add_subplot(grid[i, j]) for i in range(2) for j in range(3)]
    balance = fig.add_subplot(grid[2, :2])
    efficiency = fig.add_subplot(grid[2, 2])
    fig.suptitle(
        "GravityX — Comprehensive Simulation Reconstruction\n"
        "Artificial Gravity + Hybrid Electromagnetic Energy Buffer",
        fontsize=16,
        fontweight="bold",
    )

    gravity = gravity_g(rpm_points)
    axes[0].bar(rpm_points, gravity, color=["#4C78A8", "#F2A541", "#59A14F", "#4C78A8", "#4C78A8"])
    axes[0].axhline(1, ls="--", color="#4C6A7A", label="1 g target")
    axes[0].set(title="1 — Modeled Artificial Gravity", xlabel="RPM", ylabel="Gravity (g)")
    for x, y in zip(rpm_points, gravity):
        axes[0].text(x, y + 0.04, f"{y:.2f}g", ha="center", fontweight="bold")
    axes[0].legend()

    axes[1].plot(rpm_curve, emf_kv(rpm_curve), lw=2.5)
    axes[1].scatter([2, 3, 4], emf_kv([2, 3, 4]), color="#D62728", zorder=3)
    axes[1].axvline(3, ls="--", color="#59A14F")
    axes[1].set(title="2 — Induced EMF (ε = kω)", xlabel="RPM", ylabel="EMF (kV)")

    axes[2].plot(rpm_curve, buffer_power_kw(rpm_curve), color="#2E7D32", lw=2.5)
    axes[2].scatter([2, 3, 4], buffer_power_kw([2, 3, 4]), color="#1976D2", zorder=3)
    axes[2].axhline(PEAK_DEMAND_KW, ls="--", color="#D62728", label="Peak 160 kW")
    axes[2].axhline(AVERAGE_DEMAND_KW, ls="--", color="#F28E2B", label="Average 120 kW")
    axes[2].set(title="3 — EM Buffer Power", xlabel="RPM", ylabel="Power (kW)")
    axes[2].legend()

    velocity = np.linspace(0, RING_VELOCITY_M_S, 240)
    total_ke = 0.5 * TRANSITION_MASS_KG * velocity**2 / 1_000
    recovered = recovered_transition_energy_kj(velocity)
    axes[3].plot(velocity, total_ke, label="Total kinetic energy")
    axes[3].plot(velocity, recovered, color="#2E7D32", label="Recovered 70%")
    axes[3].fill_between(velocity, recovered, total_ke, alpha=0.2, color="#D62728", label="Loss 30%")
    axes[3].axvline(RING_VELOCITY_M_S, ls="--", color="#4C6A7A")
    axes[3].set(title="4 — Transition Energy Recovery", xlabel="Velocity (m/s)", ylabel="Energy (kJ)")
    axes[3].legend()

    axes[4].plot(rpm_curve, modeled_stress_mpa(rpm_curve), color="#D62728", lw=2.5, label="Modeled stress")
    axes[4].axhline(CFRP_REFERENCE_LIMIT_MPA, ls="--", color="#D62728", label="CFRP reference 800 MPa")
    axes[4].scatter([3], [DESIGN_STRESS_MPA], color="#2E7D32", s=80, zorder=3)
    axes[4].set(title="5 — Structural Reference Model", xlabel="RPM", ylabel="Stress (MPa)")
    axes[4].legend()

    labels = ["Peak\nDemand", "EM Buffer\n(3 RPM)", "External\nBaseline", "Total\nAvailable"]
    budget = [PEAK_DEMAND_KW, buffer_3, EXTERNAL_BASELINE_KW, buffer_3 + EXTERNAL_BASELINE_KW]
    axes[5].bar(labels, budget, color=["#D04A4A", "#3B7DC4", "#EF6C22", "#4D944D"])
    axes[5].set(title="6 — Hybrid Architecture Budget", ylabel="Power (kW)")
    for i, value in enumerate(budget):
        axes[5].text(i, value + 6, f"{value:.0f} kW", ha="center", fontweight="bold")

    balance.plot(hours, demand, color="#1A1A1A", ls="--", label="Modeled demand")
    balance.fill_between(hours, 0, demand, color="#7FA37B", alpha=0.25, label="Demand served")
    balance.axhline(buffer_3, ls=":", color="#2E7D32", label="EM buffer at 3 RPM")
    balance.set(title="7 — 48-Hour Hybrid Power Balance", xlabel="Time (hours)", ylabel="Power (kW)")
    balance.legend()

    efficiency.pie(
        [85, 9, 3.5, 2.5],
        labels=["Useful output", "Resistive", "Hysteresis", "Eddy current"],
        autopct="%1.1f%%",
        colors=["#2E7D32", "#D62728", "#F28E2B", "#8E44AD"],
    )
    efficiency.set_title("8 — EM Conversion Breakdown")

    for axis in axes + [balance]:
        axis.grid(alpha=0.25)

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def main():
    values = verified_outputs()
    verify_reference_values(values)
    output = Path(__file__).resolve().parents[1] / "assets" / "simulation" / "gravityx-reconstructed-simulation.png"
    build_figure(output)
    for key, value in values.items():
        print(f"{key}={value:.3f}")
    print(f"figure={output}")


if __name__ == "__main__":
    main()
