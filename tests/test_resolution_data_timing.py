import math
from trex_mission import angular_resolution_uas, raw_data_rate_bps, data_volume_bytes, timing_jitter_for_coherence_s


def test_earth_diameter_resolution_86ghz():
    value = angular_resolution_uas(86e9, 12_000e3)
    assert 59 < value < 61


def test_raw_rate_and_volume():
    rate = raw_data_rate_bps(8e9, 2, 2)
    assert rate == 64e9
    volume = data_volume_bytes(rate, 10*3600)
    assert math.isclose(volume/1e12, 288.0)


def test_timing_tighter_at_higher_frequency():
    t86 = timing_jitter_for_coherence_s(86e9, 0.9)
    t690 = timing_jitter_for_coherence_s(690e9, 0.9)
    assert t690 < t86
