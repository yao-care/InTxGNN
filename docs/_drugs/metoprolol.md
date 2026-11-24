---
layout: default
title: Metoprolol
parent: Model Prediction Only (L5)
nav_order: 544
evidence_level: L5
indication_count: 6
monitor_inn: "Metoprolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease", "trichotillomania"]
last_modified_at: 2026-11-24
description: "Metoprolol: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension"
---

# Metoprolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Metoprolol: From Hypertension to Malignant Hypertensive Renal Disease
{: .text-alpha }

## One-Sentence Summary

Metoprolol is a beta-1 selective blocker whose recorded uses in the knowledge graph include hypertension, acute coronary syndrome and myocardial infarction.
The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**, but **no clinical trials and no publications** directly study this condition, so the prediction rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (relation recorded in the knowledge graph; no approved-indication text is available in the local licence records) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for metoprolol: "Metoprolol is a beta 1 -selective (cardioselective) adrenergic receptor blocking agent. This preferential effect is not absolute, however, and at higher plasma concentrations, metoprolol also inhibits beta 2 -adrenoreceptors, chiefly located in the bronchial and vascular musculature." ([DailyMed: Toprol Xl (metoprolol succinate) prescribing information, Melinta Therapeutics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=496ddfaa-7c9c-4888-b747-a210249b367a), label version 2026-03-03; accessed 2026-11-19.) Based on known information, metoprolol is a beta-1 selective adrenergic blocker. Its blood-pressure-lowering effect is recorded for hypertension in the knowledge graph, and mechanistically it may be applicable to hypertensive kidney injury.

Beta-1 blockade lowers heart rate, cardiac output and renin release. Lowering blood pressure and renin activity could plausibly limit hypertensive renal damage. The high TxGNN score most likely reflects closeness to the hypertension relation already recorded for the drug, rather than new information.

There is an important caveat. Malignant hypertension is usually managed acutely with titratable intravenous agents, and beta-blockers are at best adjunctive. No trial or publication supplied for this report tests metoprolol in this condition.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for malignant hypertensive renal disease.

---

## Literature Evidence

Currently no related literature available for malignant hypertensive renal disease.

---

## India Market Information

At least 20 licences are on record, and the list may be partial. All are valid registrations. The records contain no approved-indication text.

<!-- review:begin in-lic-20261124-metoprolol-1 -->

> **Review correction (2026-11-24)**: Originally stated: "All are valid single-ingredient registrations." Removed: it described the products as single-ingredient (or as having no combination products), which does not match the Indian medicine data (the Indian Medicine Dataset): some of the recorded products are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124-metoprolol-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 6427 | Angibloc 50 Tablet PR | Strip of 10 Tablet pr | Valid |
| 30652 | Betapress 50mg Tablet XL | Strip of 10 tablet xl | Valid |
| 31346 | BetaMet 12.5mg Tablet XL | Strip of 10 tablet xl | Valid |
| 33480 | Beboxia H Tablet | Strip of 10 tablets | Valid |
| 48318 | Clovet M 50mg/6.25mg Tablet | Strip of 10 tablets | Valid |
| 51064 | Cadprol 50mg Tablet XL | Strip of 10 tablet xl | Valid |
| 73288 | Embeta XR 75mg Tablet | Strip of 15 tablet er | Valid |
| 80930 | Excemet 25mg Tablet XL | Strip of 10 tablet xl | Valid |
| 94901 | Genericart Metoprolol Succinate 12.5mg Tablet ER | Strip of 10 tablet er | Valid |
| 136562 | Metadon 25mg Tablet XL | Strip of 10 tablet xl | Valid |
| 138053 | Mettop 25mg Tablet XL | Strip of 10 tablet xl | Valid |
| 139154 | Metored 50mg Tablet XL | Strip of 10 tablet xl | Valid |
| 139982 | Metadon 50mg Tablet XL | Strip of 10 tablet xl | Valid |
| 140719 | Metosan XR 25 Tablet | Strip of 10 tablet er | Valid |
| 140942 | Mymeta XL 50mg Tablet ER | Strip of 10 tablet er | Valid |
| 144468 | Metoan H 25mg/12.5mg Tablet | Strip of 10 tablets | Valid |
| 144978 | Metoprime 25mg Tablet XL | Strip of 10 tablet xl | Valid |
| 148084 | Metocop 25mg Tablet | Strip of 10 tablets | Valid |
| 212848 | Starbeta 50mg Tablet XL | Strip of 10 tablet xl | Valid |
| 218623 | Topme-XL 50mg Tablet | Strip of 10 tablet er | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

All listed forms are oral tablets.

---

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** The knowledge graph links metoprolol with contraindication relations to several conditions, including:
  - hypotensive disorder
  - diabetes mellitus and diabetic ketoacidosis
  - liver disease and hepatic encephalopathy
  - myasthenia gravis
  - pheochromocytoma
  - psoriasis
  - gout
  - systemic lupus erythematosus
  - anxiety and dysthymic disorders
  - pancreatitis and gallbladder disease
  - anuria
  
  These come from the graph and have not been checked against a product label.
- **Drug Interactions:** 337 interactions are recorded. Most of those listed are Moderate, including epinephrine, bupropion, morphine, cimetidine, the corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), canagliflozin, dapagliflozin and chlorpropamide. Acetylsalicylic acid and magnesium oxide are Minor.

Please refer to the package insert for label warnings, as none were available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5). No trial or publication directly studies metoprolol in malignant hypertensive renal disease, and standard care for this condition relies on intravenous agents. Metoprolol is widely marketed in India, but this does not support the new use.

**To proceed, the following is needed:**
- Clinical or observational data on metoprolol in hypertensive renal disease
- Mechanism of action data and the package insert warnings and contraindications
- A comparison against current acute management of malignant hypertension

**Other predictions reviewed**

| Predicted indication | TxGNN score | Evidence level | Note |
|------|------|------|------|
| Pulmonary hypertension owing to lung disease and/or hypoxia | 0.9991 | L5 | The retrieved articles do not test metoprolol in this condition |
| Pulmonary hypertension with unclear multifactorial mechanism | 0.9991 | L5 | Prediction only |
| Braddock syndrome | 0.9989 | L5 | Prediction only |
| Chronic pulmonary heart disease | 0.9940 | L5 | Trials and studies address heart failure or myocardial infarction with COPD, not this disease itself. Trial NCT02587351 (Phase 3, COPD exacerbation prevention) was terminated and does not support efficacy |
| Trichotillomania | 0.9905 | L5 | Prediction only |

For chronic pulmonary heart disease, the supplied evidence concerns related conditions rather than the disease itself. The level is therefore capped at L5, even though the pack scored it L4.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Toprol Xl (metoprolol succinate) prescribing information, Melinta Therapeutics, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=496ddfaa-7c9c-4888-b747-a210249b367a) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

