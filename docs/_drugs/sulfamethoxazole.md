---
layout: default
title: Sulfamethoxazole
parent: Model Prediction Only (L5)
nav_order: 797
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "Sulfamethoxazole"
predicted_indications: ["acute contagious conjunctivitis"]
description: "Sulfamethoxazole: predicted new indication Acute contagious conjunctivitis (evidence level L5). In India: at least 20 listed products"
---

# Sulfamethoxazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Sulfamethoxazole: Acute contagious conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Sulfamethoxazole is a sulfonamide antibacterial, originally used for infections such as otitis media, nocardiosis, toxoplasmosis, pneumocystosis, shigellosis and conjunctivitis.
The TxGNN model predicts it may be effective for **acute contagious conjunctivitis**, but conjunctivitis already appears among its original indications, so this is not a true repurposing candidate.
Support is limited to **0 clinical trials** and **1 publication** (a cohort study of bacterial conjunctivitis).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acute contagious conjunctivitis |
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of sulfamethoxazole as: Bacterial dihydropteroate synthase inhibitor ([ChEMBL CHEMBL443 (sulfamethoxazole): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL443), CC BY-SA 3.0; accessed 2026-11-19.) Based on general pharmacology, sulfamethoxazole inhibits bacterial dihydropteroate synthase and blocks folate synthesis. It is usually combined with trimethoprim, which blocks the folate pathway at a second step. This sequential blockade is plausibly relevant to bacterial conjunctivitis, an infection caused by susceptible pathogens.

Importantly, conjunctivitis is already listed among the drug's original indications. The high TxGNN score (0.9963) is therefore likely driven by this existing association rather than by a genuinely new finding. The mechanism link above is inferred from general knowledge, not from the supplied data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31788487](https://pubmed.ncbi.nlm.nih.gov/31788487/) | 2019 | Cohort (retrospective) | Medical Hypothesis, Discovery & Innovation Ophthalmology Journal | Bacteriology and antibiotic susceptibility patterns in childhood acute bacterial conjunctivitis in Western Greece. It describes the pathogens and susceptibility in a paediatric hospital and does not evaluate sulfamethoxazole efficacy directly. |

## India Market Information

Twenty valid single-ingredient registrations are on record, with no cancelled licences. Approved-indication text is not recorded for any of them.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 19886 | Aanprim DS 800mg/160mg Tablet | Strip of 10 tablets | Valid |
| 25959 | Bactrim Syrup | Bottle of 50 ml Syrup | Valid |
| 30976 | Bioprim 800mg/160mg Tablet | Strip of 10 tablets | Valid |
| 31371 | Bentis DS 200mg/400mg Tablet | Strip of 10 tablets | Valid |
| 45319 | Chemotrin Forte 800mg/160mg Tablet | Strip of 10 tablets | Valid |
| 54981 | Cidaprim Forte Oral Suspension | Bottle of 50 ml Oral Suspension | Valid |
| 82674 | Eltiprim Suspension | Bottle of 50 ml Suspension | Valid |
| 113956 | Jolltrim-DS Tablet | Strip of 10 tablets | Valid |
| 117025 | Kombina 400mg/80mg Tablet | Strip of 10 tablets | Valid |
| 127639 | Larprim 200 mg/40 mg Drop | Packet of 15 ml Drop | Valid |
| 142897 | Methoxaprim 800mg/160mg Tablet | Strip of 10 tablets | Valid |
| 159638 | Nolapse Suspension | Bottle of 50 ml Suspension | Valid |
| 173343 | Osotrim DS 800mg/160mg Tablet | Strip of 10 tablets | Valid |
| 199546 | Septran DS 800mg/160mg Tablet | Strip of 10 tablets | Valid |
| 201573 | Synastat 800mg/160mg Tablet | Strip of 10 tablets | Valid |
| 204285 | Sulfatrim Suspension | Bottle of 100 ml Suspension | Valid |
| 205639 | Sumetrol 400mg/80mg Tablet | Strip of 10 tablets | Valid |
| 209382 | Salgatran 400mg/80mg Tablet | Strip of 10 tablets | Valid |
| 213239 | Sepnil DS 800mg/160mg Tablet | Strip of 10 tablets | Valid |
| 243572 | Wypal 200 mg/40 mg Suspension | Bottle of 50 ml Suspension | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

Available forms are oral tablets, suspensions, syrups and paediatric drops. No ophthalmic (eye-drop) formulation is listed.

## Safety Considerations

**Contraindications / risk conditions (from the knowledge graph, not label text):** inherited porphyria and other porphyrin metabolism diseases, kidney disease and kidney failure, uraemia, glomerulonephritis, liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, G6PD deficiency, folic acid deficiency anaemia, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, glycogen storage disease, cystinuria, galactosaemia and pyoureter.

**Drug Interactions:** 151 interactions are recorded. Examples are listed below.
- **Moderate:** sulfonylurea antidiabetics (chlorpropamide, glimepiride, glipizide, glyburide, acetohexamide); insulins (human, aspart, degludec, detemir, glargine, glulisine); balsalazide; picosulfuric acid. These mainly involve hypoglycaemia risk with antidiabetics.
- **Minor:** famotidine, clarithromycin, cisapride, and the setrons dolasetron, granisetron and palonosetron.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for the approved safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Conjunctivitis is already an original indication, so this is not a true repurposing opportunity. The evidence is model prediction plus one descriptive cohort study, with no clinical trials (Evidence Level L4). Package insert safety data are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Obtain the package insert warnings and contraindications from the Indian regulatory source to complete safety screening.
- Obtain mechanism of action data from DrugBank.
- Confirm whether a distinct new indication (for example a specific subtype of contagious conjunctivitis or a topical route) is intended. If so, the route would need to be assessed, since only oral and systemic forms are marketed in India.
- Identify clinical studies of sulfamethoxazole (or trimethoprim-sulfamethoxazole) in conjunctivitis, and weigh them against current topical antibiotic standards of care and local resistance patterns.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL443 (sulfamethoxazole): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL443) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

