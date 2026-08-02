from __future__ import annotations

import math


def timing_jitter_for_coherence_s(frequency_hz: float, coherence: float = 0.90) -> float:
    """
    RMS time error that produces a coherence factor C = exp(-sigma_phi^2/2),
    using sigma_phi = 2*pi*f*sigma_t. This is a first-order allocation, not a
    complete Allan-deviation or fringe-fitting model.
    """
    if frequency_hz <= 0 or not 0 < coherence < 1:
        raise ValueError("frequency must be positive and coherence in (0,1)")
    sigma_phi = math.sqrt(-2.0 * math.log(coherence))
    return sigma_phi / (2.0 * math.pi * frequency_hz)


def fractional_frequency_stability(frequency_hz: float, integration_s: float, max_phase_rad: float = 1.0) -> float:
    """First-order constant fractional frequency offset causing max_phase_rad drift."""
    if frequency_hz <= 0 or integration_s <= 0 or max_phase_rad <= 0:
        raise ValueError("all inputs must be positive")
    return max_phase_rad / (2.0 * math.pi * frequency_hz * integration_s)
