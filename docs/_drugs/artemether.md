---
layout: default
title: Artemether
parent: Model Prediction Only (L5)
nav_order: 72
evidence_level: L5
indication_count: 8
monitor_inn: "Artemether"
predicted_indications: ["acquired angioedema", "angioedema", "hereditary angioedema", "nephrogenic syndrome of inappropriate antidiuresis", "acute contagious conjunctivitis", "scleroderma (disease)", "conjunctivitis", "renin-angiotensin-aldosterone system-blocker-induced angioedema"]
last_modified_at: 2026-11-24
description: "Artemether: predicted new indication acquired angioedema (evidence level L5). In India: at least 20 listed products"
---

# Artemether
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Artemether: antimalarial artemisinin derivative → acquired angioedema
{: .text-alpha }

## One-Sentence Summary

Artemether is an artemisinin-class drug marketed in India in many single-ingredient products. The TxGNN model predicts it may be relevant to **acquired angioedema**, with a score of 0.9990. However, **no clinical trials and no publications** were found for this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | acquired angioedema |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of artemether as: Ferriprotoporphyrin IX inhibitor ([ChEMBL CHEMBL566534 (artemether): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL566534), CC BY-SA 3.0; accessed 2026-11-19.) Artemether belongs to the artemisinin class, and its activity in this class is not known to involve the pathways that drive angioedema.

Acquired angioedema is typically linked to C1-inhibitor deficiency or excess bradykinin signalling (the kallikrein-kinin and complement C1-inhibitor pathways). No mechanistic link between artemether and these pathways has been established. The high score of 0.9990 is a model-based prediction only, and it should not be read as evidence of efficacy.

Other angioedema-related predictions (angioedema, hereditary angioedema, and RAAS-blocker-induced angioedema) appear to share the same model signal, which suggests they reflect similar model patterns rather than independent biological support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

At least 20 valid single-ingredient licences are recorded, and the list may be partial. None of the records carry approved-indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 13128 | Aartimet L Dry Syrup | Bottle of 30 ml Dry Syrup | Valid |
| 13423 | Acuther L 80mg/480mg Tablet | Strip of 10 tablets | Valid |
| 13720 | Arsumet L 80mg/480mg Tablet | Strip of 6 tablets | Valid |
| 18533 | Artmon L 80mg/480mg Tablet | Strip of 6 tablets | Valid |
| 20569 | Artson 80mg/480mg Tablet | Strip of 6 tablets | Valid |
| 24902 | Artisafe L 40 mg/240 mg Tablet DT | Strip of 6 tablet dt | Valid |
| 25433 | Arteq LF 80 mg/480 mg Tablet | Strip of 6 tablets | Valid |
| 41355 | Coartrin 20 mg/120 mg Tablet | Strip of 8 tablets | Valid |
| 43001 | Chinther 20 mg/120 mg Tablet | Strip of 8 tablets | Valid |
| 90323 | Falcihit-LF 80mg/480mg Tablet | Strip of 6 tablets | Valid |
| 101327 | Gnate L Syrup | Bottle of 30 ml Syrup | Valid |
| 157460 | Numal Forte Oral Suspension | Bottle of 30 ml Oral Suspension | Valid |
| 169010 | Orther 40 Injection | Ampoule of 1 Injection | Valid |
| 188232 | Rezatrin 80 mg/480 mg Tablet | Strip of 6 tablets | Valid |
| 190805 | Rezart M 80mg Injection | Vial of 1 ml Injection | Valid |
| 194797 | Rmether 40mg Capsule | Strip of 6 capsules | Valid |
| 195682 | Rezart M 40mg Capsule | Strip of 6 capsules | Valid |
| 210591 | Sviz LF 40 mg/240 mg Dry Syrup | Bottle of 30 ml Dry Syrup | Valid |
| 210998 | Santher Kid Dry Syrup | Bottle of 30 ml Dry Syrup | Valid |
| 231992 | Ufither L 80mg/480mg Tablet | Strip of 6 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 95 interactions are recorded. Major-level examples include clarithromycin, cobicistat, amprenavir, apalutamide, atazanavir and boceprevir. Moderate-level examples include dexamethasone, miconazole, deferasirox and bosentan.
- **Contraindication-related conditions flagged in the data**: long QT syndrome, familial long QT syndrome, torsades de pointes and potassium deficiency disease. These come from database relations, not from label text.

Please refer to the package insert for further safety information, as label warnings and contraindications are not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. No trials or publications address acquired angioedema, no mechanistic link is known, and the evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data for artemether
- Preclinical evidence that artemether acts on bradykinin, kallikrein or complement pathways
- Package insert warnings and contraindications, with particular attention to QT-related risk
- Any clinical or literature evidence directly studying artemether in acquired angioedema

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available for artemether in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL566534 (artemether): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL566534) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

