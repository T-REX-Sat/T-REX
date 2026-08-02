# Critical Mission Calculations

## SEFD

\[
\mathrm{SEFD}=\frac{2 k_B T_{sys}}{\eta_A A}
\]

The source dual-mode assumptions are implemented in `trex_mission.sensitivity`.

## Baseline thermal noise

\[
\sigma_S = \frac{\sqrt{\mathrm{SEFD}_1\mathrm{SEFD}_2}}{\eta_q\sqrt{2\Delta\nu\tau}}
\]

Run this calculation for source-specific correlated flux, not only total flux.

## Timing/coherence

A first-order random phase model uses

\[
C=\exp(-\sigma_\phi^2/2),\qquad \sigma_\phi=2\pi\nu\sigma_t.
\]

This is only an allocation. A full model must include oscillator Allan deviation, time transfer, orbit error, atmospheric/propagation calibration, and fringe fitting.

## Data payload

For real Nyquist sampling,

\[
R = N_{pol}N_{bit}(2\Delta\nu).
\]

The model must distinguish raw samples, channelized data, visibilities, calibration data, and housekeeping.

## Angular resolution

\[
\theta \sim \lambda/B.
\]

Report the convention used for the numerical factor and distinguish nominal resolution from practical imaging fidelity.

## Temporal resolution

Temporal resolution is not an independent hardware number. It is the shortest integration/cadence that meets the target SNR and calibration requirement with adequate uv coverage.
