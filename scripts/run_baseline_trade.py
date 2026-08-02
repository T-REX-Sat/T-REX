#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
from pathlib import Path

from trex_mission import (
    angular_resolution_uas,
    baseline_thermal_noise_jy,
    data_volume_bytes,
    hex_area,
    raw_data_rate_bps,
    sefd_jy,
    timing_jitter_for_coherence_s,
)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

R = 0.715
N = 18
TSYS = 150.0
ETA_A = 0.65
BANDWIDTH = 8e9
ETA_Q = 0.88

area1 = hex_area(R)
area18 = N * area1
sefd1 = sefd_jy(TSYS, ETA_A, area1)
sefd18 = sefd_jy(TSYS, ETA_A, area18)
rate = raw_data_rate_bps(BANDWIDTH, polarizations=2, bits_per_sample=2)
volume_10h = data_volume_bytes(rate, 10 * 3600)

summary = {
    "assumptions": {
        "hex_circumradius_m": R,
        "segments": N,
        "system_temperature_k": TSYS,
        "aperture_efficiency": ETA_A,
        "processed_bandwidth_hz": BANDWIDTH,
        "correlation_efficiency": ETA_Q,
    },
    "area_single_m2": area1,
    "area_combined_m2": area18,
    "sefd_single_jy": sefd1,
    "sefd_combined_jy": sefd18,
    "raw_rate_gbps_per_element": rate / 1e9,
    "raw_volume_tb_per_10h_per_element": volume_10h / 1e12,
    "timing_jitter_ps_90pct_coherence_86ghz": timing_jitter_for_coherence_s(86e9, 0.90) * 1e12,
    "timing_jitter_ps_90pct_coherence_690ghz": timing_jitter_for_coherence_s(690e9, 0.90) * 1e12,
}

for seconds in (60, 600, 36000):
    summary[f"single_single_noise_jy_{seconds}s"] = baseline_thermal_noise_jy(
        sefd1, sefd1, BANDWIDTH, seconds, ETA_Q
    )
    summary[f"combined_combined_noise_jy_{seconds}s"] = baseline_thermal_noise_jy(
        sefd18, sefd18, BANDWIDTH, seconds, ETA_Q
    )

(OUT / "baseline_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

rows = []
for freq_ghz in (86, 230, 345, 690):
    for baseline_km in (12_000, 50_000, 100_000, 384_400):
        rows.append({
            "frequency_GHz": freq_ghz,
            "baseline_km": baseline_km,
            "resolution_uas": angular_resolution_uas(freq_ghz * 1e9, baseline_km * 1e3),
        })
with (OUT / "angular_resolution_trade.csv").open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(json.dumps(summary, indent=2))
