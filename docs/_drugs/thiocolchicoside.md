---
layout: default
title: Thiocolchicoside
parent: Model Prediction Only (L5)
nav_order: 830
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Thiocolchicoside: predicted new indication Insomnia (evidence level L5). Approved use: Not stated in the registration data compiled for this report (the dru…"
monitor_inn: "Thiocolchicoside"
drugbank_id: DB11582
predicted_indications: ["insomnia (disease)", "alcohol withdrawal delirium"]
---

# Thiocolchicoside
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Thiocolchicoside: From Muscle Relaxant Use to Insomnia
{: .text-alpha }

## One-Sentence Summary

Thiocolchicoside is a muscle relaxant that is currently marketed in India under 20 valid registrations.
The TxGNN model predicts it may be effective for **insomnia**, but **no clinical trials and no publications** currently support this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data compiled for this report (the drug is generally described as a muscle relaxant) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology knowledge, thiocolchicoside is a muscle relaxant that is reported to act on GABA-A receptors (as an antagonist) and glycine receptors. It can also have effects on the central nervous system, and it is known to lower the seizure threshold.

A link to sleep regulation through GABAergic or glycinergic modulation is conceivable, but it is speculative. The direction of effect is unclear: the drug could be sleep-promoting, or it could be arousing or pro-convulsant. No trial or publication supports this link, and the reasoning rests on general pharmacology knowledge only.

A second prediction, **alcohol withdrawal delirium** (score 0.9921, also L5, Hold), was also generated. It is conceptually relevant because alcohol withdrawal involves GABA hypofunction. However, GABA-A antagonism and pro-convulsant potential would be a safety concern in a condition that already carries seizure risk, so the predicted benefit may be mechanistically contradictory. Benzodiazepines are also the established standard of care.

## India Market Information

All 20 registrations are valid entries. Approved indication text is not recorded in the data compiled for this report.

<!-- review:begin in-lic-20261124-thiocolchicoside-1 -->

> **Review correction (2026-11-24)**: Originally stated: "All 20 registrations are valid single-ingredient entries." Removed: it described the products as single-ingredient (or as having no combination products), which does not match the Indian medicine data (the Indian Medicine Dataset): some of the recorded products are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124-thiocolchicoside-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 4328 | Alnase-TP Tablet | Strip of 10 tablets | Valid |
| 21494 | Aclotem T Plus 4mg/100mg/325mg Tablet | Strip of 10 tablets | Valid |
| 45760 | Clobit T 4mg/100mg/325mg Tablet | Strip of 10 tablets | Valid |
| 54302 | Cuflam PTH 4mg/100mg/325mg Tablet | Strip of 10 tablets | Valid |
| 58477 | Dynapar MR Tablet | Strip of 10 tablets | Valid |
| 63754 | Deficam 4mg Tablet | Strip of 10 tablets | Valid |
| 65424 | D Pain TC Capsule | Strip of 10 capsules | Valid |
| 152387 | Nyfol TP 4mg/100mg/325mg Tablet | Strip of 10 tablets | Valid |
| 209609 | Sonaflam TP 4mg/100mg/325mg Tablet | Strip of 10 tablets | Valid |
| 217338 | Thioquest-Twist 4 Fast Acting Capsule | Strip of 10 soft gelatin capsules | Valid |
| 219450 | Thionaid-P Tablet | Strip of 10 tablets | Valid |
| 219795 | Thioquest D 4 Capsule | Strip of 10 capsules | Valid |
| 221116 | Try-AT Tablet | Strip of 10 tablets | Valid |
| 221416 | Thionip AP 4mg/100mg/325mg Tablet | Strip of 10 tablets | Valid |
| 222077 | Thiopen AP 4mg/100mg/325mg Tablet | Strip of 10 tablets | Valid |
| 222549 | T Mr 8mg Capsule | Strip of 10 capsules | Valid |
| 223424 | Thicomus 8 Tablet | Strip of 10 tablets | Valid |
| 246482 | Zerodol TH Max 8 Tablet | Strip of 10 tablets | Valid |
| 250496 | Zacrol TP 4mg/100mg/325mg Tablet | Strip of 10 tablets | Valid |
| 251893 | Zednac TH 4mg/100mg/325mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

All forms are oral (tablets, capsules and soft gelatin capsules).

## Safety Considerations

Please refer to the package insert for safety information.

Based on general pharmacology knowledge (not the compiled data), thiocolchicoside may lower the seizure threshold. This is particularly relevant to the alcohol withdrawal delirium prediction, and it also calls for caution in any CNS-related repurposing.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no supporting clinical trials or literature (L5). The mechanism is unclear, and the possible pro-convulsant effect makes the direction of benefit uncertain.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator (needed before any safety screening)
- Mechanism of action data, for example from DrugBank
- Preclinical or early clinical evidence of a sleep-related effect, including its direction
- A seizure-risk assessment, especially before considering alcohol withdrawal delirium
- Registered indication text for the marketed products, to confirm the original indication

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

