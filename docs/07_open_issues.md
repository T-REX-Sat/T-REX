# Open Issues

## OI-001: Configuration count

The ASTRA source uses a five-DiskSat ConOps, while the dual-mode note uses 18 hexagonal DiskSats. Define pathfinder, initial mission, and strategic architecture explicitly.

## OI-002: Sensitivity versus science threshold

The ASTRA source states sensitivity to flux densities above 40 mJy and sub-minute time resolution. Under the dual-mode note's single-DiskSat assumptions, an identical two-element baseline is not obviously consistent with 40 mJy at high SNR on sub-minute timescales. This is a first-order gating analysis.

## OI-003: Integration-time scaling in dual-mode note

The note states that an 18-fold SEFD improvement gives the same SNR in 1/18 of the integration time. Under the standard radiometer scaling, time to fixed SNR scales as SEFD squared, implying 1/324 if all other assumptions are unchanged. The intended observing comparison must be clarified.

## OI-004: Frequency scope

The source concept illustrates 86-690 GHz while the baseline instrument description is an 86 GHz receiver. Define the baseline band and a technology roadmap for higher frequencies.

## OI-005: Orbit baseline

The ASTRA source is framed around LEO, while the proposed SMART-1-like concept seeks a high-apogee or lunar-distant orbit. Compare science gain, transfer time, radiation, communications, and operations.

## OI-006: Data architecture

Raw VLBI rates can reach tens of gigabits per second per element. Decide what is recorded, channelized, correlated, compressed, crosslinked, and downlinked.

## OI-007: Combined-aperture feasibility

Interlocking 18 elements into a millimeter-wave reflector requires surface accuracy, phase alignment, metrology, thermal stability, and structural control that are not yet budgeted.
