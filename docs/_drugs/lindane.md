---
layout: default
title: Lindane
parent: Model Prediction Only (L5)
nav_order: 493
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "Lindane"
predicted_indications: ["cervical neuroblastoma", "benign neoplasm of tongue", "epiglottis neoplasm", "odontogenic cyst", "pre-malignant neoplasm", "benign neoplasm of hypopharynx", "schwannoma of jugular foramen", "cystic neoplasm", "benign neoplasm of buccal mucosa", "inner ear neoplasm"]
description: "Lindane: predicted new indication Cervical neuroblastoma (evidence level L5). In India: at least 20 listed products"
---

# Lindane
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Lindane: Cervical neuroblastoma
{: .text-alpha }

## One-Sentence Summary

Lindane is an organochlorine topical antiparasitic, originally used to treat scabies (including Norwegian scabies), head and pubic lice, and mite infestations.
The TxGNN model predicts it may be effective for **cervical neuroblastoma**, but **no clinical trials and no publications** currently support this prediction, so it rests on a computational score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Cervical neuroblastoma |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of lindane as: GABA-A receptor negative allosteric modulator ([ChEMBL CHEMBL15891 (lindane): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL15891), CC BY-SA 3.0; accessed 2026-11-19.) Lindane is known as an organochlorine insecticide that acts as a GABA-A receptor antagonist. Its efficacy in scabies and lice is established, but this is a parasiticidal effect on the pest's nervous system.

No mechanistic link has been identified between this action and neuroblastoma. The very high score (0.9991) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Other top-ranked predictions are also tumour or cyst conditions of the head and neck (for example benign neoplasm of tongue, epiglottis neoplasm, odontogenic cyst, inner ear neoplasm). All are L5 with no supporting studies, which suggests a systematic pattern in the model's predictions rather than a drug-specific signal.

Lindane also has well-documented neurotoxicity (seizure risk) and carcinogenicity concerns, which argue against its use in oncology.

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 60823 | Descab Lotion | Bottle of 450 ml Lotion | Valid |
| 79842 | Eskino Liquid | Bottle of 100 ml Liquid | Valid |
| 95984 | G Scab Lotion | Bottle of 100 ml Lotion | Valid |
| 96831 | Gamascab 1% Cream | Tube of 15 gm Cream | Valid |
| 97468 | Gama Soap | Packet of 75 gm Soap | Valid |
| 99063 | Gamaderm Forte Lotion | Bottle of 100 ml Lotion | Valid |
| 99359 | Gamin Lotion | Bottle of 100 ml Lotion | Valid |
| 99610 | Gamabez Soap | Packet of 75 gm Soap | Valid |
| 104666 | Hexab Lotion | Bottle of 100 ml Lotion | Valid |
| 125165 | Lupiscab Solution | Bottle of 100 ml Solution | Valid |
| 131284 | Linscab Lotion | Bottle of 100 ml Lotion | Valid |
| 155587 | Nit N Mite 1% Cream | Tube of 25 gm Cream | Valid |
| 165108 | Olscab C Lotion | Bottle of 100 ml Lotion | Valid |
| 200260 | Scabiped Lotion | Bottle of 500 ml Lotion | Valid |
| 200828 | Scaboma Soap | Packet of 75 gm Soap | Valid |
| 201014 | Scabinil Lotion | Bottle of 100 ml Lotion | Valid |
| 202944 | Scabex S Lotion | Bottle of 100 ml Lotion | Valid |
| 204447 | Scabcare Lotion | Bottle of 200 ml Lotion | Valid |
| 207147 | Scabac Lotion | Bottle of 100 ml Lotion | Valid |
| 230581 | Ultrasone Cream | Tube of 10 gm Cream | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

All 20 registrations are valid products (lotions, creams, solution, liquid and soaps).

<!-- review:begin in-lic-20261124-lindane-1 -->

> **Review correction (2026-11-24)**: Originally stated: "All 20 registrations are valid single-ingredient products (lotions, creams, solution, liquid and soaps)." Removed: it described the products as single-ingredient (or as having no combination products), which does not match the Indian medicine data (the Indian Medicine Dataset): some of the recorded products are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124-lindane-1 -->

## Safety Considerations

- **Disease associations flagged in the knowledge graph (contraindication edges, not label text)**: epilepsy, cirrhosis of liver, atopic eczema/atopic dermatitis, psoriasis, parapsoriasis, substance abuse/dependence, skin disease, actinic keratosis, seborrheic keratosis.
- **Drug Interactions**: 179 interactions are recorded. Major-level examples include **bupropion**, **iopamidol** and **iohexol**. Moderate-level examples include morphine, levofloxacin, metoclopramide, promethazine, ephedrine, phentermine, fenfluramine and sibutramine.
- **Other concerns noted in the prediction review**: neurotoxicity (seizures), systemic absorption and carcinogenicity classification, which weigh against exploratory use.

Please refer to the package insert for label warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (L5), with no clinical trials, no literature and no plausible mechanism. Lindane's neurotoxicity and carcinogenicity concerns make oncology repurposing unattractive.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (currently blocking safety screening)
- Mechanism of action data from DrugBank
- Preclinical evidence showing a biological link to neuroblastoma
- A safety and route-of-administration assessment, since the available products are topical only

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL15891 (lindane): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL15891) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

