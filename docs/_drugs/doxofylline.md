---
layout: default
title: Doxofylline
parent: Model Prediction Only (L5)
nav_order: 288
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Doxofylline: predicted new indication Pierre Robin syndrome associated with a chromosomal anomaly (evidence level L5). Approved use: Not stated in the India licence records. Published literature desc…"
monitor_inn: "Doxofylline"
drugbank_id: DB09273
predicted_indications: ["Pierre Robin syndrome associated with a chromosomal anomaly", "Laubry-Pezzi syndrome", "Jeune syndrome situs inversus", "genetic syndromic Pierre Robin syndrome", "orofacial clefting syndrome", "partial deletion of the long arm of chromosome 7", "disorder of fucoglycosan synthesis", "partial deletion of the long arm of chromosome 22", "heart disease", "pulmonary valve disease"]
---

# Doxofylline
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

## Doxofylline: From Asthma and COPD to Pierre Robin Syndrome Associated with a Chromosomal Anomaly
{: .text-alpha }

## One-Sentence Summary

Doxofylline is a xanthine bronchodilator used for respiratory disease (asthma and chronic obstructive pulmonary disease).
The TxGNN model predicts it may be effective for **Pierre Robin syndrome associated with a chromosomal anomaly**,
but **no clinical trials and no publications** currently support this prediction. It is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India licence records. Published literature describes use in asthma and COPD |
| Predicted New Indication | Pierre Robin syndrome associated with a chromosomal anomaly |
| TxGNN Prediction Score | 0.9954 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From the published literature, doxofylline is a methylxanthine bronchodilator. It is thought to act through phosphodiesterase inhibition, with weaker binding to adenosine A1 and A2 receptors than theophylline. This may explain its better cardiovascular tolerability.

The predicted indication is a craniofacial developmental condition linked to a chromosomal anomaly. It is not a respiratory-smooth-muscle disorder, and no plausible mechanistic link to doxofylline was identified. A bronchodilator would not be expected to alter the developmental or genetic basis of this syndrome. The high score (0.9954, rank 7922) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, so this prediction should be treated with considerable caution.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for this predicted indication.

## India Market Information

Twenty valid registrations are on record. The licence records do not include approved indication text.

<!-- review:begin in-lic-20261124c-doxofylline-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Twenty valid single-ingredient registrations are on record." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-doxofylline-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 4156 | Amril Plus 400mg Tablet | Strip of 10 tablets | Valid |
| 59805 | Doximax Tablet | Strip of 10 tablets | Valid |
| 59990 | Doxoford Tablet | Strip of 10 tablets | Valid |
| 60384 | Doxside AM Tablet | Strip of 10 tablets | Valid |
| 61488 | Doxonil 400 Tablet | Strip of 10 tablets | Valid |
| 62957 | Doxo M 400mg/10mg Tablet | Strip of 10 tablets | Valid |
| 64027 | Doxygrap 400mg Tablet | Strip of 10 tablets | Valid |
| 64246 | Doxorid 400mg Tablet | Strip of 10 tablets | Valid |
| 64772 | Dofyll AM 400mg/30mg Tablet | Strip of 10 tablets | Valid |
| 65576 | Doxomac M 400mg/10mg Tablet | Strip of 10 tablets | Valid |
| 66851 | Doxoent 400mg Tablet | Strip of 10 tablets | Valid |
| 67433 | Dofasma Plus Tablet | Strip of 10 tablets | Valid |
| 68754 | Doxjafy M 400mg/10mg Tablet SR | Strip of 10 tablet sr | Valid |
| 68991 | Doxofit M 400mg/10mg Tablet | Strip of 10 tablets | Valid |
| 70548 | Doxogod Tablet | Strip of 10 tablets | Valid |
| 71644 | Doxopax 400mg/10mg Tablet | Strip of 10 tablets | Valid |
| 79950 | Evomont D 400mg/10mg Tablet | Strip of 10 tablets | Valid |
| 127934 | Lunair 400mg Tablet | Strip of 10 tablets | Valid |
| 180955 | Phydoxin AB 400mg/100mg Tablet | Strip of 10 tablets | Valid |
| 196133 | Roaron M 400mg/10mg Tablet SR | Strip of 10 tablet sr | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

All products are oral tablets. The registered product names suggest that some are fixed-dose combinations, and the Indian Medicine Dataset lists a second active ingredient for several of them.

<!-- review:begin in-lic-20261124b-doxofylline-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The registered product names suggest that some are fixed-dose combinations, although the records classify all of them as single-ingredient." Revised: the sentence said the data classify these products as single-ingredient, but the Indian Medicine Dataset lists a second active ingredient for several of them (they are fixed-dose combinations). Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124b-doxofylline-1 -->

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction data are available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no trials or publications for this indication, and no plausible mechanistic link between a xanthine bronchodilator and a chromosomal craniofacial syndrome. Doxofylline is already widely marketed in India, but only for respiratory use.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA) and a biological rationale linking doxofylline to the pathology of the syndrome
- Package insert warnings and contraindications from the India regulatory source
- Original approved indication text from the licence records
- Any preclinical or clinical evidence specific to this condition

## Other Predictions Reviewed

The other nine top-ranked predictions were also reviewed. None has supporting clinical trials. Only the "heart disease" prediction shows any indirect evidence, and it is graded L4 as a research question rather than a candidate for development.

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Laubry-Pezzi syndrome | 0.9954 | L5 | Structural cardiac defect; no mechanistic link |
| 3 | Jeune syndrome situs inversus | 0.9954 | L5 | Skeletal ciliopathy; at most theoretical symptom relief |
| 4 | Genetic syndromic Pierre Robin syndrome | 0.9953 | L5 | No mechanistic link |
| 5 | Orofacial clefting syndrome | 0.9953 | L5 | Developmental malformation; no mechanistic link |
| 6 | Partial deletion of the long arm of chromosome 7 | 0.9953 | L5 | No pharmacological rationale |
| 7 | Disorder of fucoglycosan synthesis | 0.9952 | L5 | Retrieved literature covers asthma/COPD only |
| 8 | Partial deletion of the long arm of chromosome 22 | 0.9952 | L5 | No pharmacological rationale |
| 9 | Heart disease | 0.9950 | L4 | Indirect evidence only (research question) |
| 10 | Pulmonary valve disease | 0.9950 | L5 | Structural valve disorder; no rationale |

For heart disease, the available evidence concerns cardiovascular safety. Doxofylline shows fewer cardiostimulant effects than theophylline ([PMID 2781149](https://pubmed.ncbi.nlm.nih.gov/2781149/), [PMID 11268710](https://pubmed.ncbi.nlm.nih.gov/11268710/)). A 1993 randomised, double-blind trial in chronic heart failure with hypoxaemia ([PMID 8088931](https://pubmed.ncbi.nlm.nih.gov/8088931/)) compared methylxanthines in 48 patients. Because it does not establish that doxofylline treats heart disease, it does not support this indication.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Revised: the single-ingredient classification | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

