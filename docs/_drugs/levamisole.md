---
layout: default
title: Levamisole
parent: Model Prediction Only (L5)
nav_order: 482
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Levamisole: predicted new indication Drug-induced osteoporosis (evidence level L5). Approved use: Ascariasis and ancylostomiasis"
monitor_inn: "Levamisole"
predicted_indications: ["drug-induced osteoporosis", "benign neoplasm of tongue", "cervical neuroblastoma", "benign neoplasm of buccal mucosa", "epiglottis neoplasm", "cystic neoplasm", "benign neoplasm of floor of mouth", "schwannoma of jugular foramen", "benign neoplasm of hypopharynx", "inner ear neoplasm"]
---

# Levamisole
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

## Levamisole: From Ascariasis and Hookworm Infection to Drug-Induced Osteoporosis
{: .text-alpha }

## One-Sentence Summary

Levamisole was originally used as an anthelmintic to treat ascariasis (roundworm infection) and ancylostomiasis (hookworm infection).
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**, but there are currently **no clinical trials and no publications** supporting this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ascariasis and ancylostomiasis (from the knowledge graph; the Indian license records contain no indication text) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, levamisole is an anthelmintic that has also been used as an immunomodulator (affecting T-cells and macrophages). Its efficacy in parasitic worm infections is established, and mechanistically it might plausibly influence bone remodelling through immune pathways.

This link is speculative. The data compiled for this report contain no trial, publication, or mechanistic evidence connecting levamisole to bone loss, and the similarity between the original and new indications has not been assessed. The high TxGNN score (99.999%, rank 46) is a statistical prediction from the knowledge graph, not proof of benefit.

### Other Predicted Indications

Nine other indications were predicted with similarly high scores (99.996% to 99.999%). Most are neoplasms, and none has strong evidence:

| Predicted Indication | Evidence Level | Available Evidence |
|------|------|------|
| Benign neoplasm of tongue | L5 | None |
| Cervical neuroblastoma | L5 | One in vitro paper on nucleotide metabolism in a cell line, likely a tool-compound use rather than therapeutic evidence |
| Benign neoplasm of buccal mucosa | L4 | Two animal studies (1977, 1979) on hamster cheek pouch carcinogenesis; direction of effect unclear |
| Epiglottis neoplasm | L5 | None |
| Cystic neoplasm | L5 | A fixed drug eruption case report and a paediatric colon carcinoma case report; neither supports efficacy |
| Benign neoplasm of floor of mouth | L5 | None |
| Schwannoma of jugular foramen | L5 | None |
| Benign neoplasm of hypopharynx | L4 | A randomized study of levamisole plus UFT in head and neck carcinoma (2001) and a laryngeal carcinoma pilot study (1980); both concern malignant disease, so they are indirect, and outcomes were not available. Flagged as a research question |
| Inner ear neoplasm | L5 | None |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for drug-induced osteoporosis.

---

## India Market Information

Levamisole holds 20 valid single-ingredient registrations in India, with none cancelled. The records contain no approved indication text. Five representative authorizations:

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 123312 | Levomol 150mg Tablet | Strip of 1 tablet | Cipla Ltd |
| 123339 | Levomol 50mg Tablet | Strip of 1 tablet | Cipla Ltd |
| 75722 | Elseal 150mg Tablet | Strip of 4 tablets | Organic Laboratories |
| 59226 | Deworm Syrup | Bottle of 10 ml syrup | Gem Pharmaceuticals Pvt Ltd |
| 58688 | Dicaris Adults Tablet | Strip of 1 tablet | Janssen Pharmaceuticals |

Available forms are oral tablets (including dispersible tablets), syrup, and suspension.

---

## Safety Considerations

- **Drug Interactions**: 73 interactions were recorded. Examples of **Major** interactions include deferiprone, samarium (153Sm) lexidronam, adalimumab, baricitinib, certolizumab pegol, and cladribine. **Moderate** interactions include ethanol, warfarin, zidovudine, azathioprine, alemtuzumab, anakinra, chloramphenicol, and several vaccines (anthrax, tetanus toxoid, live cholera). Many of the listed interactions involve immunosuppressants or myelosuppressive agents.
- **Known toxicity profile**: The assessment notes levamisole is associated with serious toxicity, including agranulocytosis and vasculitis, which weighs heavily against use in a non-life-threatening condition. A fixed drug eruption has also been reported.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for drug-induced osteoporosis rests only on a model score, with no trials, no literature, and no established mechanism. Levamisole's known risks (agranulocytosis, vasculitis) make unsupported use hard to justify.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) and a plausible mechanistic link to bone metabolism
- Preclinical or clinical evidence in drug-induced osteoporosis (for example glucocorticoid-induced bone loss models)
- Package insert warnings and contraindications from the Indian regulator, which currently block safety screening
- A risk-benefit assessment covering haematological monitoring and the interaction burden
- If the research focus shifts, a review of the head and neck randomized study (PMID 11735172) for the malignant setting only, since outcomes were not available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

