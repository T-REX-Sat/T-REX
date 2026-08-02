from __future__ import annotations

import math
from .constants import BOLTZMANN, JY


def hex_area(circumradius_m: float) -> float:
    """Area of a regular hexagon from its circumradius."""
    if circumradius_m <= 0:
        raise ValueError("circumradius_m must be positive")
    return 3.0 * math.sqrt(3.0) * circumradius_m**2 / 2.0


def sefd_jy(system_temperature_k: float, aperture_efficiency: float, area_m2: float) -> float:
    """System Equivalent Flux Density in Jy: 2 k_B Tsys / (eta A)."""
    if system_temperature_k <= 0 or area_m2 <= 0:
        raise ValueError("temperature and area must be positive")
    if not 0 < aperture_efficiency <= 1:
        raise ValueError("aperture_efficiency must be in (0, 1]")
    return 2.0 * BOLTZMANN * system_temperature_k / (aperture_efficiency * area_m2) / JY


def baseline_thermal_noise_jy(
    sefd1_jy: float,
    sefd2_jy: float,
    bandwidth_hz: float,
    integration_s: float,
    efficiency: float = 0.88,
) -> float:
    """One-sigma thermal noise for a two-element interferometric baseline."""
    vals = (sefd1_jy, sefd2_jy, bandwidth_hz, integration_s, efficiency)
    if any(v <= 0 for v in vals):
        raise ValueError("all inputs must be positive")
    return math.sqrt(sefd1_jy * sefd2_jy) / (
        efficiency * math.sqrt(2.0 * bandwidth_hz * integration_s)
    )


def integration_time_s(
    source_flux_jy: float,
    snr: float,
    sefd1_jy: float,
    sefd2_jy: float,
    bandwidth_hz: float,
    efficiency: float = 0.88,
) -> float:
    """Integration time for a target SNR on a two-element baseline."""
    vals = (source_flux_jy, snr, sefd1_jy, sefd2_jy, bandwidth_hz, efficiency)
    if any(v <= 0 for v in vals):
        raise ValueError("all inputs must be positive")
    effective_sefd = math.sqrt(sefd1_jy * sefd2_jy)
    return (snr * effective_sefd / (efficiency * source_flux_jy))**2 / (2.0 * bandwidth_hz)
