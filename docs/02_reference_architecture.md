# Reference Architecture 0.1

## Source-derived elements

- Central Pez spacecraft bus.
- Deployable DiskSat radio telescopes.
- 86 GHz baseline receiver chain with feed horn, orthomode transducer, low-noise amplification, frequency conversion, and digital backend.
- Local VLBI recording on DiskSats.
- Rendezvous/docking with Pez for data transfer, correlation, servicing, or reconfiguration.
- Deployable reflector options: sail-derived membrane, CFRP, or mesh.
- Precision timing, pointing, docking, storage, correlation, and downlink as core design drivers.

## Configuration branches requiring decision

### Branch A - Pez plus 5 observing DiskSats

This branch follows the ASTRA ConOps figure and is the more credible near-term architecture for a limited constellation demonstration.

### Branch B - 18 interlocking hexagonal DiskSats

This branch follows the dual-mode note. Dispersed mode maximizes baseline; combined mode pools collecting area. It is a stronger long-term architecture but adds substantial docking, metrology, surface-accuracy, thermal, and control complexity.

## Recommended layered baseline

- **Pathfinder:** Pez plus 2-3 DiskSats or one DiskSat plus ground VLBI, focused on timing, deployment, recording, orbit determination, and correlated detection.
- **Initial science mission:** Pez plus 5-6 DiskSats with controlled distributed baselines and ground participation.
- **Strategic architecture:** Up to 18 reconfigurable segments with distributed and combined modes.

This recommendation is a planning hypothesis, not a source statement. It must be tested against science yield and cost.
