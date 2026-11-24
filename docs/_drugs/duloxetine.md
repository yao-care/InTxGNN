---
layout: default
title: Duloxetine
parent: Model Prediction Only (L5)
nav_order: 293
evidence_level: L5
indication_count: 10
monitor_inn: "Duloxetine"
predicted_indications: ["benign paroxysmal torticollis of infancy", "agoraphobia", "obsessive-compulsive disorder", "paranoid personality disorder", "histrionic personality disorder (disease)", "schizoid personality disorder", "schizotypal personality disorder", "Ohdo syndrome and variants", "ligneous conjunctivitis", "blepharophimosis - intellectual disability syndrome, Ohdo type"]
last_modified_at: 2026-11-24
description: "Duloxetine: predicted new indication benign paroxysmal torticollis of infancy (evidence level L5). In India: at least 20 listed products"
---

# Duloxetine
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

## Duloxetine: serotonin-norepinephrine reuptake inhibitor (SNRI) → benign paroxysmal torticollis of infancy
{: .text-alpha }

## One-Sentence Summary

Duloxetine is a serotonin-norepinephrine reuptake inhibitor (SNRI) antidepressant that is currently marketed in India.
The TxGNN model predicts it may be effective for **benign paroxysmal torticollis of infancy**,
but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | benign paroxysmal torticollis of infancy |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for duloxetine: "Although the exact mechanisms of the antidepressant, central pain inhibitory and anxiolytic actions of duloxetine in humans are unknown, these actions are believed to be related to its potentiation of serotonergic and noradrenergic activity in the CNS." ([DailyMed: Duloxetine Delayed-Release (duloxetine hydrochloride) prescribing information, Golden State Medical Supply, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=00628e5e-4c5b-2573-e063-6294a90a0e3b), label version 2026-08-20; accessed 2026-11-19.) Duloxetine belongs to the SNRI class, which blocks reuptake of serotonin and norepinephrine.

Benign paroxysmal torticollis of infancy is a self-limiting paediatric disorder that is associated with CACNA1A channelopathy. No plausible link between serotonin-norepinephrine reuptake inhibition and this condition is evident. The high TxGNN score is a model-based prediction only, and it is not backed by any clinical or literature evidence. The prediction should therefore be treated as a hypothesis with no mechanistic support at present.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

At least 20 valid licences are recorded, and the list may be partial.

<!-- review:begin in-lic-20261124c-duloxetine-1 -->

> **Review correction (2026-11-24)**: Originally stated: "At least 20 valid single-ingredient licences are recorded, and the list may be partial." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-duloxetine-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 58877 | Duvanta NP 20 Tablet | Strip of 10 tablets | Valid |
| 59065 | Duloxin 20 Tablet | Strip of 10 tablets | Valid |
| 59350 | Dt 20mg Tablet | Strip of 10 tablets | Valid |
| 59906 | Dulox 30mg Tablet | Strip of 10 tablets | Valid |
| 62138 | Dtn 20mg Tablet | Strip of 10 tablets | Valid |
| 63444 | Dulet 30mg Tablet DR | Strip of 10 Tablet DR | Valid |
| 63482 | Dulosys 20 Tablet | Strip of 10 tablets | Valid |
| 63981 | DXT 40 Tablet | Strip of 10 tablets | Valid |
| 64218 | Dulotix 20mg Tablet | Strip of 10 tablets | Valid |
| 64416 | Dutexol 20mg Tablet | Strip of 10 tablets | Valid |
| 64661 | Diligo 20 Tablet | Strip of 10 tablets | Valid |
| 65191 | Dulovib 30mg Tablet | Strip of 10 tablets | Valid |
| 65927 | Duloxmine 30mg Tablet | Strip of 10 tablets | Valid |
| 66306 | Duloren 40mg Tablet | Strip of 10 tablets | Valid |
| 67092 | Dulohox 20mg Tablet | Strip of 10 tablets | Valid |
| 68686 | Dulx 20mg Tablet | Strip of 10 tablets | Valid |
| 199855 | Symbal 30 Tablet | Strip of 10 tablets | Valid |
| 202890 | Sogeval M 20mg/750mcg Tablet | Strip of 10 tablets | Valid |
| 206010 | Sylonex 60mg Tablet | Strip of 10 tablets | Valid |
| 251146 | Zidane 40mg Capsule | Strip of 10 capsules | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 329 interactions were found in the interaction screening. Examples rated **Major** include bupropion, lorcaserin, diethylpropion, dolasetron and dexfenfluramine. Examples rated **Moderate** include epinephrine, morphine, acetylsalicylic acid and cimetidine.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score, but there are no clinical trials or publications for this condition, and no plausible mechanism links duloxetine to it. The evidence level is L5.

**To proceed, the following is needed:**
- Mechanistic data showing how duloxetine could act on this condition
- Any preclinical or clinical studies in benign paroxysmal torticollis of infancy
- Package insert warnings and contraindications, plus a paediatric safety assessment, since the condition occurs in infants

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Duloxetine Delayed-Release (duloxetine hydrochloride) prescribing information, Golden State Medical Supply, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=00628e5e-4c5b-2573-e063-6294a90a0e3b) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

