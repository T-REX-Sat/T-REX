import math
from trex_mission import hex_area, sefd_jy, baseline_thermal_noise_jy, integration_time_s


def test_dual_mode_source_values():
    area = hex_area(0.715)
    assert math.isclose(area, 1.328, rel_tol=0.01)
    single = sefd_jy(150, 0.65, area)
    combined = sefd_jy(150, 0.65, 18 * area)
    assert math.isclose(single, 4.8e5, rel_tol=0.02)
    assert math.isclose(combined, 2.7e4, rel_tol=0.03)
    assert math.isclose(single / combined, 18.0, rel_tol=1e-12)


def test_noise_improves_as_sqrt_time():
    n1 = baseline_thermal_noise_jy(4.8e5, 4.8e5, 8e9, 60)
    n2 = baseline_thermal_noise_jy(4.8e5, 4.8e5, 8e9, 240)
    assert math.isclose(n1 / n2, 2.0, rel_tol=1e-12)


def test_fixed_snr_time_scales_as_sefd_squared():
    t_single = integration_time_s(0.04, 5, 4.8e5, 4.8e5, 8e9)
    t_combined = integration_time_s(0.04, 5, 4.8e5/18, 4.8e5/18, 8e9)
    assert math.isclose(t_single / t_combined, 18**2, rel_tol=1e-12)
