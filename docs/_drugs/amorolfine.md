---
layout: default
title: Amorolfine
parent: Model Prediction Only (L5)
nav_order: 56
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Amorolfine: predicted new indication Drug-induced osteoporosis (evidence level L5). Approved use: Fungal nail infection (onychomycosis)…"
monitor_inn: "Amorolfine"
predicted_indications: ["drug-induced osteoporosis", "disease of retroperitoneum", "disease of uterine broad ligament", "lumbar spinal stenosis", "abdominal cystic lymphangioma", "abdominal ectopic pregnancy", "celiac trunk compression syndrome", "lymph node palisaded myofibroblastoma", "sacrum chordoma", "urethral disease"]
---

# Amorolfine
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

## Amorolfine: From Fungal Nail Infection (Topical Antifungal) to Drug-Induced Osteoporosis
{: .text-alpha }

## One-Sentence Summary

Amorolfine is a topical morpholine antifungal, used mainly for fungal nail infections (onychomycosis).
The TxGNN model predicts it may be relevant to **drug-induced osteoporosis**, but **no clinical trials and no publications** currently support this prediction, so it is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Fungal nail infection (onychomycosis), based on general pharmacological reference information; the Indian licence records compiled for this report contain no indication text |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, amorolfine is a morpholine antifungal that inhibits fungal ergosterol biosynthesis (sterol delta-14 reductase and delta-7,delta-8 isomerase). It is applied topically and has negligible systemic absorption.

No established mechanistic link to bone metabolism or osteoporosis has been identified. The very high TxGNN score (0.99998, rank 96) is a TxGNN model (deep learning) prediction only. Similarity between the original and predicted indications could not be assessed.

The other top predictions show the same pattern: disease of retroperitoneum, disease of uterine broad ligament, lumbar spinal stenosis, abdominal cystic lymphangioma, abdominal ectopic pregnancy, celiac trunk compression syndrome, lymph node palisaded myofibroblastoma, sacrum chordoma and urethral disease. All are Level L5 with no trials or literature, and many are anatomical groupings or mechanical conditions with no plausible antifungal link. Route compatibility with a topical-only product is also unresolved.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Amorolfine is marketed in India with 20 valid single-ingredient licences, all topical creams. Indication text is not recorded in the licences.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 245 | Amrolstar Cream | Tube of 30 gm Cream | Valid |
| 902 | Amrfy 0.25% Cream | Tube of 30 gm Cream | Valid |
| 953 | Amorfine Cream | Tube of 30 gm Cream | Valid |
| 1317 | Amrosys Cream | Tube of 15 gm Cream | Valid |
| 1333 | Amoron Cream | Tube of 30 gm Cream | Valid |
| 1369 | Amrolstar Cream | Tube of 10 gm Cream | Valid |
| 1381 | Amrolstar Cream | Tube of 50 gm Cream | Valid |
| 1450 | Alimnator Cream | Tube of 60 gm Cream | Valid |
| 1493 | Amortive Cream | Tube of 30 gm Cream | Valid |
| 2127 | Amroltop 0.25% Cream | Tube of 30 gm Cream | Valid |
| 2436 | Arolson Cream | Tube of 30 gm Cream | Valid |
| 3966 | Amfocin Cream | Tube of 50 gm Cream | Valid |
| 4648 | Amortive Cream | Tube of 10 gm Cream | Valid |
| 11666 | Amrobest Cream | Tube of 15 gm Cream | Valid |
| 42273 | Candiwel AF 0.25% Cream | Tube of 20 gm Cream | Valid |
| 84441 | Fintop-AF Cream | Tube of 30 gm Cream | Valid |
| 121166 | Loceryl Cream | Tube of 10 gm Cream | Valid |
| 141766 | Mycoban-A Cream | Tube of 15 gm Cream | Valid |
| 174253 | Pamoria Cream | Tube of 30 gm Cream | Valid |
| 186525 | Rolofine Cream | Tube of 30 gm Cream | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: One pharmacology-based entry was found: amorolfine is listed as a ligand of the sodium channel Nav1.7 (SCN9A). No interaction severity level is provided, and this is not a clinical drug-drug interaction.

Please refer to the package insert for other safety information (warnings and contraindications).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a TxGNN model (deep learning) score. There are no clinical trials or publications, no plausible mechanistic link between a topical antifungal and drug-induced osteoporosis, and negligible systemic exposure. Package-insert safety data are also missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India product labels
- Confirmed mechanism of action data (for example from DrugBank)
- Preclinical or mechanistic evidence linking amorolfine to bone metabolism
- Assessment of route and formulation feasibility, since all marketed products are topical creams with minimal systemic absorption
- Systematic literature and trial searches to confirm that no supporting evidence exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

