---
layout: default
title: Drug Repurposing Predictions — India
nav_order: 1
---

# InTxGNN - India Drug Repurposing Predictions

Welcome to InTxGNN, a drug repurposing prediction system for India using the TxGNN graph neural network.

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## India: what this site covers

This site publishes reports for **{{ site.data.drug_stats.total_drugs }}** medicines listed in the registration data of [CDSCO](https://cdsco.gov.in/) (India).

Reports by evidence level: L1 {{ site.data.drug_stats.level_counts.L1 }} · L2 {{ site.data.drug_stats.level_counts.L2 }} · L3 {{ site.data.drug_stats.level_counts.L3 }} · L4 {{ site.data.drug_stats.level_counts.L4 }} · L5 {{ site.data.drug_stats.level_counts.L5 }}

### Highest evidence levels on this site

| Medicine | Evidence level |
|---|---|
| [Bendamustine](/drugs/bendamustine/) | L1 |
| [Bromfenac](/drugs/bromfenac/) | L1 |
| [Bupropion](/drugs/bupropion/) | L1 |
| [Busulfan](/drugs/busulfan/) | L1 |
| [Hyaluronic Acid](/drugs/hyaluronic-acid/) | L1 |
| [Natamycin](/drugs/natamycin/) | L1 |
| [Nepafenac](/drugs/nepafenac/) | L1 |
| [Polidocanol](/drugs/polidocanol/) | L1 |
| [Rifabutin](/drugs/rifabutin/) | L1 |
| [Tegafur](/drugs/tegafur/) | L1 |

### Medicines covered only by this site among the 30 TxGNN sites

| Medicine | Evidence level |
|---|---|
| [Valdecoxib](/drugs/valdecoxib/) | L2 |
| [Oxyphenbutazone](/drugs/oxyphenbutazone/) | L3 |
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

<!-- local-home:end -->

## What is Drug Repurposing?

Drug repurposing (also known as drug repositioning) is the process of finding new therapeutic uses for existing approved drugs. This approach can significantly reduce the time and cost of drug development.

## How It Works

InTxGNN uses the TxGNN graph neural network to predict potential new indications for drugs approved by India's Central Drugs Standard Control Organisation (CDSCO).

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
- [TxGNN](https://zitniklab.hms.harvard.edu/projects/TxGNN/) - Graph neural network trained on a knowledge graph

---

*Last updated: {{ "now" | date: "%Y-%m-%d" }}*

---

## About the Developer

This platform is developed and operated by **藥提醒科技有限公司** (yao.care, company registration
number 83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

InTxGNN is the India site of the company's "TxGNN Drug Repurposing" product line.
The same system is deployed across 30 countries and regions, each named `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN, and so on) at `{cc}txgnn.yao.care`.
Product overview: <https://www.yao.care/medical/txgnn/>.

The TxGNN model itself was developed by the Zitnik Lab at Harvard Medical School and published
in *Nature Medicine*. This platform is the production system 藥提醒科技有限公司 built on top of that
model, covering national drug-registration data integration, deep-learning prediction that excludes uses already recorded in the knowledge graph, PubMed / ClinicalTrials evidence grading, and SMART on FHIR
electronic health record integration.
