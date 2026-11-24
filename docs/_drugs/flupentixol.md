---
layout: default
title: Flupentixol
parent: Model Prediction Only (L5)
nav_order: 368
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Flupentixol: predicted new indication Retinal dystrophy with or without extraocular anomalies (evidence level L5). Approved use: Schizophrenia"
monitor_inn: "flupentixol"
predicted_indications: ["retinal dystrophy with or without extraocular anomalies", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "congenital disorder of glycosylation with defective fucosylation", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "hydranencephaly (disease)", "myopia X-linked", "syndromic myopia", "myopia 26, X-linked, female-limited", "atypical glycine encephalopathy"]
---

# Flupentixol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Flupentixol: From Schizophrenia to Retinal dystrophy with or without extraocular anomalies
{: .text-alpha }

## One-Sentence Summary

Flupentixol is a thioxanthene antipsychotic originally used to treat schizophrenia.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**,
but **no clinical trials and no publications** currently support this prediction. It is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, flupentixol is a thioxanthene-class antipsychotic that acts as an antagonist at dopamine receptors (D1, D2, D3 and D5). Its use in schizophrenia (and depression) is established.

No mechanistic link to inherited retinal degeneration has been identified. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No known pathway connects dopamine receptor antagonism to the disease-modifying biology of inherited retinal dystrophies.

Other predictions for this drug (for example Charcot-Marie-Tooth disease type 1G, congenital disorders of glycosylation, congenital brain malformations, glycine encephalopathy and several myopia subtypes) likewise have no supporting trials or literature. For the myopia subtypes, dopamine antagonism may even act against the generally protective effect of dopamine signalling. The predictions should be treated as hypotheses, not findings.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Flupentixol is marketed in India, with 20 valid registrations and none cancelled. The data compiled for this report does not include approved indication text.

<!-- review:begin in-lic-20261124c-flupentixol-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Flupentixol is marketed in India as single-ingredient products, with 20 valid registrations and none cancelled." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-flupentixol-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 42071 | Calm U 0.5mg/10mg Tablet | Strip of 10 tablets | Valid |
| 66346 | Denzole-E Tablet | Strip of 10 tablets | Valid |
| 68052 | Deaxn 0.5mg/10mg Tablet | Strip of 10 tablets | Valid |
| 85058 | Flupen 0.5mg Tablet | Strip of 10 tablets | Valid |
| 85327 | Flutrameli 0.5mg/10mg Tablet | Strip of 10 tablets | Valid |
| 87142 | Fluteez 0.5mg/10mg Tablet | Strip of 10 tablets | Valid |
| 87406 | Flunaxit Tablet | Strip of 10 tablets | Valid |
| 87935 | Fresh Up 0.5mg/10mg Tablet | Strip of 10 tablets | Valid |
| 90365 | Flucida 20mg Injection | Ampoule of 1 Injection | Valid |
| 151263 | Nuanixt 0.5 mg/10 mg Tablet | Strip of 10 tablets | Valid |
| 151332 | Newanxit 0.5mg/10mg Tablet | Strip of 10 tablets | Valid |
| 158866 | Nishq-S 5 Tablet | Strip of 10 tablets | Valid |
| 164614 | Ornarest 0.5mg/10mg Tablet | Strip of 10 tablets | Valid |
| 173582 | Placida Tablet | Strip of 10 tablets | Valid |
| 180791 | Penflu 40 mg Injection | Vial of 2 ml Injection | Valid |
| 188809 | Rexipra FX 5 Tablet | Strip of 10 tablets | Valid |
| 200364 | Spenzo Depot 20 Injection | Vial of 1 ml Injection | Valid |
| 209210 | Safeol 1mg Tablet | Strip of 10 tablets | Valid |
| 220740 | Tixocen-M 0.5mg/10mg Tablet | Strip of 10 tablets | Valid |
| 230021 | Tilomeg EL 0.5mg/10mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

Both oral (tablet) and injectable forms are available.

## Safety Considerations

Please refer to the package insert for safety information.

Pharmacology data show that flupentixol binds dopamine D1, D2, D3 and D5 receptors. Screening studies have also reported anti-SARS-CoV-2 activity for this class of cationic amphiphilic drugs, probably through phospholipidosis. This is not a clinical finding.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a TxGNN model (deep learning) score alone (Evidence Level L5), which may reflect similarities the model learned between related diseases, not biological evidence. There are no clinical trials, no literature and no plausible mechanistic link between dopamine antagonism and inherited retinal dystrophy.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source, which are currently missing and block safety screening
- Detailed mechanism of action data
- Preclinical or mechanistic evidence connecting flupentixol to retinal dystrophy pathology
- A systematic literature search to confirm that no supporting studies exist
- Assessment of route compatibility and a safety plan for the target population

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

