---
layout: default
title: Lindane
parent: Model Prediction Only (L5)
nav_order: 493
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
monitor_inn: "Lindane"
predicted_indications: ["cervical neuroblastoma", "benign neoplasm of tongue", "epiglottis neoplasm", "odontogenic cyst", "pre-malignant neoplasm", "benign neoplasm of hypopharynx", "schwannoma of jugular foramen", "cystic neoplasm", "benign neoplasm of buccal mucosa", "inner ear neoplasm"]
description: "Lindane: predicted new indication Cervical neuroblastoma (evidence level L5). Approved use: Not recorded in the local data"
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
| Number of Listed Products | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Lindane is known as an organochlorine insecticide that acts as a GABA-A receptor antagonist. Its efficacy in scabies and lice is established, but this is a parasiticidal effect on the pest's nervous system.

No mechanistic link has been identified between this action and neuroblastoma. The very high score (0.9991) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Other top-ranked predictions are also tumour or cyst conditions of the head and neck (for example benign neoplasm of tongue, epiglottis neoplasm, odontogenic cyst, inner ear neoplasm). All are L5 with no supporting studies, which suggests a systematic pattern in the model's predictions rather than a drug-specific signal.

Lindane also has well-documented neurotoxicity (seizure risk) and carcinogenicity concerns, which argue against its use in oncology.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 202944 | Scabex S Lotion | Lotion, 100 ml bottle | Not stated in the data |
| 165108 | Olscab C Lotion | Lotion, 100 ml bottle | Not stated in the data |
| 207147 | Scabac Lotion | Lotion, 100 ml bottle | Not stated in the data |
| 131284 | Linscab Lotion | Lotion, 100 ml bottle | Not stated in the data |
| 96831 | Gamascab 1% Cream | Cream, 15 g tube | Not stated in the data |

All 20 registrations are valid single-ingredient products (lotions, creams, solution, liquid and soaps); the table shows the first five.

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

