# InTxGNN - India Drug Repurposing Predictions

Drug repurposing prediction system for India using TxGNN knowledge graph.

## Overview

InTxGNN uses the TxGNN knowledge graph to predict potential new therapeutic uses for drugs available in India.

## Installation

```bash
uv sync
```

## Usage

```bash
# Process drug data
uv run python scripts/process_fda_data.py

# Prepare vocabulary data
uv run python scripts/prepare_external_data.py

# Run KG prediction
uv run python scripts/run_kg_prediction.py

# Generate FHIR resources
uv run python scripts/generate_fhir_resources.py
```

## Data Sources

- Indian Medicine Dataset (253,973 drugs)
- TxGNN Knowledge Graph
- DrugBank
- ClinicalTrials.gov
- PubMed

## Disclaimer

This project is for research purposes only. The predictions have not been clinically validated and do not constitute medical advice.
