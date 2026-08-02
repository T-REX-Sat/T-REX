from __future__ import annotations


def raw_data_rate_bps(
    bandwidth_hz: float,
    polarizations: int = 2,
    bits_per_sample: int = 2,
    nyquist_factor: float = 2.0,
) -> float:
    """Simple real-sampled baseband rate: bandwidth * Nyquist * bits * polarizations."""
    if bandwidth_hz <= 0 or polarizations <= 0 or bits_per_sample <= 0 or nyquist_factor <= 0:
        raise ValueError("all inputs must be positive")
    return bandwidth_hz * nyquist_factor * bits_per_sample * polarizations


def data_volume_bytes(rate_bps: float, duration_s: float, duty_cycle: float = 1.0) -> float:
    if rate_bps <= 0 or duration_s <= 0 or not 0 < duty_cycle <= 1:
        raise ValueError("invalid rate, duration, or duty_cycle")
    return rate_bps * duration_s * duty_cycle / 8.0
