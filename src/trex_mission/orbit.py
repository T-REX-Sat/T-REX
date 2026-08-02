from __future__ import annotations

import math

EARTH_RADIUS_M = 6_378_137.0
EARTH_MU_M3_S2 = 3.986004418e14


def kepler_period_s(perigee_alt_m: float, apogee_alt_m: float) -> float:
    """Two-body period for an Earth orbit defined by perigee and apogee altitude."""
    if perigee_alt_m < 0 or apogee_alt_m < perigee_alt_m:
        raise ValueError("invalid altitudes")
    rp = EARTH_RADIUS_M + perigee_alt_m
    ra = EARTH_RADIUS_M + apogee_alt_m
    a = 0.5 * (rp + ra)
    return 2.0 * math.pi * math.sqrt(a**3 / EARTH_MU_M3_S2)


def ideal_rocket_propellant_fraction(delta_v_m_s: float, isp_s: float, g0: float = 9.80665) -> float:
    """Ideal propellant fraction 1-exp(-dv/(Isp*g0)); excludes tanks and margins."""
    if delta_v_m_s < 0 or isp_s <= 0 or g0 <= 0:
        raise ValueError("invalid inputs")
    return 1.0 - math.exp(-delta_v_m_s / (isp_s * g0))
