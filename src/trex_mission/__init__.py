"""T-REX mission concept calculations."""

from .sensitivity import hex_area, sefd_jy, baseline_thermal_noise_jy, integration_time_s
from .resolution import angular_resolution_uas
from .data_payload import raw_data_rate_bps, data_volume_bytes
from .timing import timing_jitter_for_coherence_s, fractional_frequency_stability

__all__ = [
    "hex_area", "sefd_jy", "baseline_thermal_noise_jy", "integration_time_s",
    "angular_resolution_uas", "raw_data_rate_bps", "data_volume_bytes",
    "timing_jitter_for_coherence_s", "fractional_frequency_stability",
]
