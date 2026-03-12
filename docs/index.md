---
layout: default
title: Home
nav_order: 1
---

# InTxGNN - India Drug Repurposing Predictions

Welcome to InTxGNN, a drug repurposing prediction system for India using the TxGNN knowledge graph.

## What is Drug Repurposing?

Drug repurposing (also known as drug repositioning) is the process of finding new therapeutic uses for existing approved drugs. This approach can significantly reduce the time and cost of drug development.

## How It Works

InTxGNN uses the TxGNN knowledge graph to predict potential new indications for drugs approved by India's Central Drugs Standard Control Organisation (CDSCO).

1. **Data Collection**: We collect drug data from CDSCO
2. **Knowledge Graph Mapping**: Drugs are mapped to the TxGNN knowledge graph
3. **Prediction**: Machine learning identifies potential new drug-disease relationships
4. **Evidence Collection**: Supporting evidence is gathered from clinical trials, PubMed, and other sources

## Important Disclaimer

{: .warning }
> This website is for **research purposes only**. The predictions shown here are computational and have not been clinically validated. They do not constitute medical advice. Always consult healthcare professionals for medical decisions.

## Resources

- [Drug Reports](/drugs/) - Browse drug repurposing predictions
- [FHIR API](/fhir/metadata) - Access data via FHIR R4 API
- [About](/about/) - Learn more about this project

## Data Sources

- [CDSCO](https://cdsco.gov.in/) - Central Drugs Standard Control Organisation
- [DrugBank](https://go.drugbank.com/) - Drug database
- [ClinicalTrials.gov](https://clinicaltrials.gov/) - Clinical trial registry
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/) - Biomedical literature
- [TxGNN](https://zitniklab.hms.harvard.edu/projects/TxGNN/) - Knowledge graph

---

*Last updated: {{ "now" | date: "%Y-%m-%d" }}*
