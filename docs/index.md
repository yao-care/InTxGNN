---
layout: default
title: Drug Repurposing Predictions — India
description: "TxGNN drug repurposing reports for 884 medicines in the Indian Medicine Dataset (India), with evidence levels L1–L5 from clinical trials and literature."
last_modified_at: 2026-11-04
nav_order: 1
---

# InTxGNN - India Drug Repurposing Predictions

Welcome to InTxGNN, a drug repurposing prediction system for India using the TxGNN graph neural network.

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## India: what this site covers

This site publishes reports for **{{ site.data.drug_stats.total_drugs }}** medicines listed in the [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset), a public GitHub dataset (India).

Dataset: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset), downloaded and compared automatically every week (Mondays). Details: [Data Sources]({{ '/sources/' | relative_url }}).

Reports by evidence level:

| Evidence level | Reports | Share |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

185 predicted drug–disease pairs on this site appear on no other of the 30 TxGNN sites.

### Highest evidence levels on this site

| Medicine | Evidence level |
|---|---|
| [Bendamustine](/drugs/bendamustine/) | L1 |
| [Bromfenac](/drugs/bromfenac/) | L1 |
| [Bupropion](/drugs/bupropion/) | L1 |
| [Busulfan](/drugs/busulfan/) | L1 |
| [Nepafenac](/drugs/nepafenac/) | L1 |
| [Polidocanol](/drugs/polidocanol/) | L1 |
| [Ribavirin](/drugs/ribavirin/) | L1 |
| [Clofarabine](/drugs/clofarabine/) | L1 |
| [Doxorubicin](/drugs/doxorubicin/) | L1 |
| [Potassium](/drugs/potassium/) | L1 |

### Medicines covered only by this site among the 30 TxGNN sites

| Medicine | Evidence level |
|---|---|
| [Amifostine](/drugs/amifostine/) | L4 |
| [Conivaptan](/drugs/conivaptan/) | L4 |
| [Chlormezanone](/drugs/chlormezanone/) | L4 |
| [Enclomiphene](/drugs/enclomiphene/) | L5 |
| [Glycolic Acid](/drugs/glycolic-acid/) | L5 |
| [Levosalbutamol](/drugs/levosalbutamol/) | L5 |
| [Oxaceprol](/drugs/oxaceprol/) | L5 |
| [Rofecoxib](/drugs/rofecoxib/) | L5 |
| [Seratrodast](/drugs/seratrodast/) | L5 |
| [Sparfloxacin](/drugs/sparfloxacin/) | L5 |
| [Amineptine](/drugs/amineptine/) | L5 |
| [Ripasudil](/drugs/ripasudil/) | L5 |
| [Carbenicillin](/drugs/carbenicillin/) | L5 |
| [Minodronic Acid](/drugs/minodronic-acid/) | L5 |
| [Rimonabant](/drugs/rimonabant/) | L5 |

<!-- local-home:end -->

## What is Drug Repurposing?

Drug repurposing (also known as drug repositioning) is the process of finding new therapeutic uses for existing approved drugs. This approach can significantly reduce the time and cost of drug development.

## How It Works

InTxGNN uses the TxGNN graph neural network to predict potential new indications for drugs listed in the [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset), a public GitHub dataset.

1. **Data Collection**: We collect drug data from the Indian Medicine Dataset (GitHub)
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

- [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) - Public medicine dataset on GitHub (CDSCO approval status is not included)
- [DrugBank](https://go.drugbank.com/) - Drug database
- [ClinicalTrials.gov](https://clinicaltrials.gov/) - Clinical trial registry
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/) - Biomedical literature
- [TxGNN](https://zitniklab.hms.harvard.edu/projects/TxGNN/) - Graph neural network trained on a knowledge graph

---

*Last updated: {{ page.last_modified_at | date: "%Y-%m-%d" }}*

---

## About the Developer

This platform is developed and operated by **藥提醒科技有限公司** (yao.care). See
<a href="{{ '/about/' | relative_url }}">About</a> for company details, the TxGNN model
background, and the full list of sites in this product line.
