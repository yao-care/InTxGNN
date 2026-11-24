---
layout: default
title: Nalidixic Acid
parent: Model Prediction Only (L5)
nav_order: 577
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
description: "Nalidixic Acid: predicted new indication Conjunctivitis (evidence level L5). Approved use: Not stated in the available India licence data (the drug is known as…"
monitor_inn: "Nalidixic acid"
predicted_indications: ["conjunctivitis", "sclerosing cholangitis", "rheumatoid arthritis", "infectious otitis media"]
---

# Nalidixic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Nalidixic Acid: From Bacterial Infections to Conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Nalidixic acid is a first-generation quinolone antibacterial. The data compiled for this report do not list a formal approved indication for it in India.
The TxGNN model predicts it may be effective for **conjunctivitis**, but there are **0 clinical trials** and only **5 publications**, none of which test nalidixic acid in eye disease.
This prediction is supported by model output alone and should be treated as a hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available India licence data (the drug is known as a quinolone antibacterial, mainly for Gram-negative infections) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 0.9983 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of nalidixic acid as: Bacterial DNA gyrase inhibitor ([ChEMBL CHEMBL5 (nalidixic acid): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL5), CC BY-SA 3.0; accessed 2026-11-19.) Based on general knowledge, nalidixic acid is a first-generation quinolone that inhibits bacterial DNA gyrase and topoisomerase IV. This means it could plausibly act against susceptible Gram-negative bacteria, which is the basis for linking it to bacterial conjunctivitis.

The link is weak. The retrieved literature concerns Shigella and Yersinia susceptibility and resistance in diarrhoeal disease, not eye infection. Nalidixic acid is not used topically in the eye, its spectrum is narrow (mainly Enterobacteriaceae), and later fluoroquinolones have largely replaced it. The TxGNN score is a computational prediction only.

Other predicted indications were also reviewed, and all remain at the Hold stage:
- **Sclerosing cholangitis** (score 0.9963, L5): no trials or literature; a gut-liver axis link is speculative.
- **Rheumatoid arthritis** (score 0.9941, L5): one paper on oral Staphylococcus carriage that does not evaluate the drug.
- **Infectious otitis media** (score 0.9904, L4): one paper on ofloxacin, a different drug, and nalidixic acid has poor activity against the usual otitis media pathogens.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of these papers tests nalidixic acid as a treatment for conjunctivitis. They are laboratory or surveillance studies of related bacteria.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16914657](https://pubmed.ncbi.nlm.nih.gov/16914657/) | 2006 | Resistance surveillance | J Med Microbiol | Over 60% of 445 Shigella sonnei isolates in Bangladesh (1999–2003) were resistant to nalidixic acid |
| [17446289](https://pubmed.ncbi.nlm.nih.gov/17446289/) | 2007 | Microbiological characterisation | J Med Microbiol | A novel Shigella dysenteriae serovar identified in patients with diarrhoea in Bangladesh |
| [15824427](https://pubmed.ncbi.nlm.nih.gov/15824427/) | 2005 | Microbiological characterisation | J Med Microbiol | Isolation and characterisation of provisional Shigella boydii serovar E16553 |
| [9442487](https://pubmed.ncbi.nlm.nih.gov/9442487/) | 1997 | Laboratory study | Microb Drug Resist | A 70-kb plasmid of epidemic Shigella dysenteriae type 1 linked to drug resistance and virulence |
| [3206956](https://pubmed.ncbi.nlm.nih.gov/3206956/) | 1988 | Laboratory study | Zh Mikrobiol Epidemiol Immunobiol | Invasiveness and cytotoxicity as criteria for Yersinia attenuation, including nalidixic-acid-resistant mutants |

---

## India Market Information

There are 20 valid single-ingredient registrations. Approved indication text is not available for any of them.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 28171 | Besco Tablet | Strip of 10 tablets | Valid |
| 29855 | Bactomet 150mg/100mg Suspension | Bottle of 30 ml Suspension | Valid |
| 32458 | Betadix Syrup | Bottle of 30 ml Syrup | Valid |
| 66741 | Diarlop Plus Oral Suspension | Bottle of 30 ml Oral Suspension | Valid |
| 67742 | Dix 300mg Syrup | Bottle of 30 ml Syrup | Valid |
| 95627 | Gramoneg M 300 mg/200 mg Tablet | Strip of 8 tablets | Valid |
| 96921 | Gramoneg M 150 mg/100 mg Suspension | Bottle of 30 ml Suspension | Valid |
| 98234 | Genogyl N Syrup | Bottle of 60 ml Syrup | Valid |
| 98806 | Gramonex Injection | Vial of 1 Injection | Valid |
| 99545 | Gramonex Injection | Vial of 1 Injection | Valid |
| 103156 | Genogyl N 150mg/100mg Suspension | Bottle of 30 ml Suspension | Valid |
| 143249 | Metnil 300mg/200mg Tablet | Strip of 10 tablets | Valid |
| 143338 | Matrix MN Suspension | Bottle of 30 ml Suspension | Valid |
| 157118 | Nalmezole 125mg/100mg Suspension | Bottle of 30 ml Suspension | Valid |
| 157679 | Negadix M Tablet | Strip of 10 tablets | Valid |
| 158805 | Nalidys Tablet | Strip of 10 tablets | Valid |
| 159885 | Nalidys Suspension | Bottle of 60 ml Suspension | Valid |
| 183437 | Qugyl N Syrup | Bottle of 60 ml Syrup | Valid |
| 202927 | Sprot N Tablet | Strip of 10 tablets | Valid |
| 208241 | Sprot N 300 mg/200 mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

---

## Safety Considerations

- **Disease-level cautions (from the knowledge graph, not label text):** the model's knowledge graph links nalidixic acid with possible contraindication in epilepsy, porphyria, liver disease, gallbladder disease, tendinitis and other tendon or joint conditions, peripheral neuropathy and other nervous system diseases, *Clostridium difficile* colitis, G6PD deficiency, and several metabolic disorders (for example galactosemia, cystinuria and glycogen storage disease).
- **Drug interactions:** 156 interactions are recorded. Major ones include:
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone
  - Bupropion
  - Chlorpropamide

  Moderate ones include antidiabetic agents (acarbose, alogliptin, canagliflozin, dapagliflozin, saxagliptin, albiglutide), acetylsalicylic acid, alosetron, balsalazide, and several calcium and citrate preparations.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score alone. There are no clinical trials, and no retrieved paper tests nalidixic acid in conjunctivitis. The drug has a narrow spectrum, is not used in the eye, and has been replaced by later fluoroquinolones.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the India products (currently a blocking gap)
- Mechanism of action data confirmed from DrugBank
- Approved indication text for the India licences
- Comparative susceptibility data against common conjunctivitis pathogens
- Evidence of an ocular formulation or a justification for choosing it over existing ophthalmic fluoroquinolones

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL5 (nalidixic acid): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL5) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

