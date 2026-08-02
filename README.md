# T-REX Mission Concept

**T-REX (Time-Resolving Explorer)** is a pre-formulation space-VLBI mission concept organized around a reusable Pez spacecraft bus and deployable DiskSat radio telescopes. This repository is the team's digital engineering workspace for science traceability, hardware trades, software prototypes, theory studies, proposal development, and decision control.

> **Status:** Concept maturation / pre-Phase A. The repository intentionally separates source statements, proposed assumptions, and unresolved issues.

## Six-month objective

From August 2026 through January 2027, mature T-REX from a compelling narrative into a reviewable mission concept with:

- a controlled reference architecture;
- a science-to-requirements traceability matrix;
- reproducible calculations for sensitivity, timing, data volume, resolution, cadence, and orbit trades;
- an initial hardware breadboard and software analysis pipeline;
- a defensible SWaP-C and mission-class trade;
- proposal-ready packages for ASTRA engagement, NIAC technology studies, Flight Opportunities/TechLeap demonstrations, and a Pioneers-to-SMEX mission pathway.

## Source baseline

The uploaded ASTRA concept describes a time-domain VLBI observatory in which DiskSats deploy from a central Pez bus, observe independently with an 86 GHz receiver chain, store data locally, rendezvous with the Pez, and transfer data for correlation and downlink. It identifies precision timing, pointing, docking, onboard correlation, and deployable reflectors as major design drivers.

A separate dual-mode note describes **18 hexagonal DiskSats** that can either disperse into a long-baseline array or interlock into one larger collecting aperture. These two source documents contain configuration differences that are tracked as open issues rather than silently reconciled.

## Repository map

```text
.
├── .github/                 # Issue, PR, and review templates
├── assumptions/             # Controlled assumptions and change log
├── calculations/            # Reproducible first-order mission calculations
├── data/                    # Input data (not large binaries)
├── docs/                    # Strategy, architecture, ConOps, and slide plan
├── hardware/                # Subsystem work packages and breadboard plans
├── outputs/                 # Generated tables and figures
├── proposals/               # Funding/program pathway packages
├── references/              # Source documents and official program links
├── requirements/            # Science and system traceability
├── risks/                   # Risk and opportunity register
├── scripts/                 # Executable analyses
├── software/                # Flight/ground software concept documents
├── src/trex_mission/        # Python analysis package
├── team/                    # Roles, onboarding, cadence, and student pathways
├── tests/                   # Unit tests for calculations
├── theory/                  # Science models and observability studies
├── CHANGELOG.md
├── CONTRIBUTING.md
├── pyproject.toml
└── README.md
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest
python scripts/run_baseline_trade.py
```

Generated outputs are written to `outputs/`.

## Team operating rule

Every quantitative claim should point to one of four things:

1. a source document;
2. a controlled assumption ID;
3. a reproducible calculation;
4. an explicitly labeled open issue.

See `docs/06_governance_and_reviews.md` and `CONTRIBUTING.md` before adding work.
