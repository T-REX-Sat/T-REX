from __future__ import annotations

from .constants import C_LIGHT, RAD_TO_UAS


def angular_resolution_uas(frequency_hz: float, baseline_m: float, factor: float = 1.0) -> float:
    """First-order interferometric resolution factor * lambda / B, in microarcseconds."""
    if frequency_hz <= 0 or baseline_m <= 0 or factor <= 0:
        raise ValueError("frequency, baseline, and factor must be positive")
    wavelength_m = C_LIGHT / frequency_hz
    return factor * wavelength_m / baseline_m * RAD_TO_UAS
