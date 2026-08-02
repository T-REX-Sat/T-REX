# Contributing to T-REX

## Branches

- `main`: reviewed, reproducible concept baseline
- `work/<workstream>-<topic>`: active development
- `proposal/<program>-<cycle>`: proposal-specific packages

## Pull requests

A pull request should contain:

- the decision or question being addressed;
- changed assumptions and requirement IDs;
- evidence (calculation, test, source, or review note);
- affected risks and downstream documents;
- a named reviewer outside the author's workstream.

## Definition of done

A task is not done until its output is reproducible, linked to requirements, and reviewed. Calculations must include units, assumptions, and at least one test. Architecture changes require a decision record in `docs/decisions/`.

## File conventions

- Use SI units internally.
- Put human-readable units in tables and plots.
- Do not commit large raw data or generated caches.
- Do not put confidential export-controlled, proprietary, or unpublished partner material in the public repository.
