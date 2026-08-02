# T-REX Six-Month Strategy

**Period:** August 2026 - January 2027  
**Version:** 0.1  
**Purpose:** Convert T-REX from a compelling mission narrative into a controlled, quantitatively defensible concept package.

## 1. Strategic outcome

By the end of Month 6, T-REX should have:

- a science traceability matrix linking objectives to observables and system performance;
- a reconciled configuration baseline for the number and role of DiskSats;
- a parametric sensitivity and cadence model that demonstrates what targets are observable;
- an orbit and baseline trade comparing LEO, high-apogee, and cislunar options;
- preliminary SWaP-C allocations for Pez, DiskSat, payload, propulsion, storage, and communications;
- a hardware breadboard plan and at least one bench-level demonstration;
- a tested software analysis package and representative simulated data flow;
- a proposal pathway with one near-term technology opportunity and one mission-class objective;
- student work packages that can produce credit, funding applications, posters, papers, and invention disclosures.

## 2. Workstreams

### Hardware Development

Own the physical architecture: reflector, 86 GHz receiver chain, frequency reference, cryogenic or non-cryogenic thermal approach, ADCS, storage, docking, Pez interfaces, propulsion, power, and communications. Produce mass/power/data budgets and breadboard evidence.

### Software Development

Own the digital thread: requirements database, orbit and uv-coverage simulation, sensitivity calculator, timing/coherence model, onboard recording and correlation concept, ground pipeline, reproducible plots, tests, and documentation.

### Theoretical Development

Own science traceability: source models, correlated flux assumptions, variability timescales, polarization requirements, scattering effects, target catalog, imaging observables, and minimum viable science cases.

### Proposal Development

Own narrative, program fit, stakeholder mapping, schedule, cost-class strategy, external reviews, graphics, proposal boilerplate, student participation plans, and submission readiness.

## 3. Month-by-month plan

### Month 1 - August 2026: Baseline and team formation

- Appoint four workstream leads and a systems-integration lead.
- Import source documents and create a controlled assumption register.
- Resolve or explicitly branch the 5-DiskSat versus 18-DiskSat architecture.
- Freeze a Reference Mission 0.1 and a Pathfinder 0.1.
- Create the science traceability matrix and top-level requirement IDs.
- Run the first sensitivity, timing, data-rate, resolution, and orbit calculations.
- Decide whether the current TechLeap challenge is actionable; its application path is time-sensitive and only relevant if registration prerequisites were satisfied.
- Prepare a concise package for the September Ad ASTRA workshop and stakeholder conversations.

**Gate 1:** Baseline Definition Review.

### Month 2 - September 2026: Requirements and feasibility

- Participate in ASTRA community engagement and record feedback.
- Complete first-order link/data/storage budgets.
- Define receiver bandwidth, polarization, quantization, and observing duty cycle.
- Quantify sensitivity against at least five target/source scenarios.
- Establish timing/coherence allocations for 86 GHz and stretch frequencies.
- Compare LEO, high-apogee, and cislunar baseline evolution and visibility.
- Create an initial risk register and technology-gap map.

**Gate 2:** Science and System Requirements Review.

### Month 3 - October 2026: Integrated architecture trades

- Build a parametric spacecraft and payload budget.
- Model dispersed, phased/clustered, and combined-aperture observing modes.
- Produce uv-coverage and cadence simulations for Sgr A*, M87*, and one transient scenario.
- Define Pez-DiskSat data transfer and correlation architecture.
- Downselect one reflector concept and one timing architecture for breadboarding.
- Define the Pioneers pathfinder and SMEX science mission boundaries.

**Gate 3:** Architecture Trade Review.

### Month 4 - November 2026: Demonstration and external review

- Demonstrate one critical function at bench level: timing distribution, receiver chain element, deployment coupon, interlocking interface, or data ingest/correlation pipeline.
- Run an end-to-end simulated observation from orbit state to visibility data to science metric.
- Conduct an external review with radio astronomy, spacecraft, timing, and proposal experts.
- Draft a NIAC-style technology study around one breakthrough element rather than the complete observatory.
- Draft a Flight Opportunities/TechLeap-style payload concept around a testable, self-contained technology.

**Gate 4:** Technology Demonstration Review.

### Month 5 - December 2026: Convergence and proposal package

- Close high-priority review actions.
- Produce SWaP-C ranges and a cost-class argument.
- Complete ConOps, mission timeline, operational modes, and failure-response logic.
- Prepare the six-slide stakeholder deck and a longer technical appendix.
- Draft one conference abstract, one student poster template, and one paper outline.
- Identify potentially patentable subsystem concepts and follow Brown's invention-disclosure process before public disclosure where appropriate.

**Gate 5:** Proposal Red-Team Review.

### Month 6 - January 2027: Concept maturity review

- Demonstrate reproducibility of all critical calculations.
- Publish Mission Concept Package 1.0.
- Hold a Concept Maturity Review across science, engineering, implementation, cost, story, and strategy.
- Select the next 12-month objective: technology study, flight demonstration, Pioneers pathfinder, SMEX concept study, or a combination.
- Assign student deliverables for Spring and Summer 2027 funding/credit cycles.

**Gate 6:** Concept Maturity and Roadmap Review.

## 4. Quantitative gates

The following must be answered with reproducible evidence:

1. What correlated flux densities can the array detect at SNR 5 in 60 s, 10 min, and 10 h?
2. What baseline and frequency are required for 10, 2, and 1 microarcsecond resolution?
3. What time/frequency stability preserves at least 90% coherence over the chosen integration interval?
4. What raw and reduced data volumes are produced per observation?
5. What mass, power, pointing, thermal, storage, and downlink allocations fit a Pioneers pathfinder and a SMEX mission?
6. How long does a low-thrust transfer take, how much delta-v and propellant does it require, and what radiation exposure is accumulated?

## 5. Team cadence

- Weekly 30-minute workstream standups.
- Weekly 60-minute systems integration meeting.
- Biweekly calculation or design review.
- Monthly gate review with an external advisor when available.
- Decisions recorded in `docs/decisions/`; actions tracked through GitHub issues.

## 6. Program strategy

- **ASTRA:** Use for strategic mission-concept maturation, community alignment, and Concept Maturity Level discipline. Treat T-REX as a scalable architecture and clearly distinguish the strategic end-state from lower-cost precursors.
- **NIAC:** Propose a breakthrough enabling technology such as autonomous assembly/interlocking, reusable deployable reflectors, precision time transfer, or a novel Pez-DiskSat servicing architecture. NIAC is not the primary home for the full science mission.
- **Flight Opportunities / TechLeap:** Demonstrate one flight-ready technology. The 2026 robotically manipulated payload challenge is especially aligned with docking, manipulation, modular assembly, and deployable sensor interfaces, but it is time-sensitive.
- **Pioneers:** Target a reduced pathfinder with compelling standalone astrophysics under the $20M cost cap, not automatically the full 18-element observatory.
- **SMEX:** Treat as the likely upper mission-class target for a more complete initial observatory; the 2026 SMEX cost cap is $190M.

## 7. Student outcomes

Each student should own a bounded work package with a technical output and a communication output. Possible outcomes include independent-study credit subject to faculty/department approval, UTRA/SPRINT funding, a poster, conference abstract, paper contribution, hardware or software artifact, stakeholder presentation, proposal section, and potentially an invention disclosure.
