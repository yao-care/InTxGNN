---
layout: default
title: Camylofin
parent: Model Prediction Only (L5)
nav_order: 136
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Camylofin: predicted new indication Insomnia (evidence level L5). Approved use: Not stated in the licence data (the drug is generally known as an ant…"
monitor_inn: "Camylofin"
drugbank_id: DB13738
predicted_indications: ["insomnia (disease)"]
---

# Camylofin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Camylofin: From Antispasmodic Use to Insomnia
{: .text-alpha }

## One-Sentence Summary

Camylofin is an antispasmodic that is currently marketed in India in many products, although the data compiled for this report do not include an approved indication text.
The TxGNN model predicts it may be effective for **insomnia**, but there are currently **no clinical trials and no publications** supporting this direction, so the prediction rests on the model alone.

<!-- review:begin in-lic-20261124c-camylofin-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Camylofin is an antispasmodic that is currently marketed in India in many single-ingredient products, although the data compiled for this report do not include an approved indication text." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-camylofin-1 -->

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data (the drug is generally known as an antispasmodic) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 0.9939 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general background knowledge (not part of the data compiled for this report), camylofin is an antispasmodic that combines anticholinergic (antimuscarinic) activity with direct smooth-muscle relaxation. Its use in smooth-muscle spasm is the likely original context, but no approved indication text was recorded in the licence data.

The link to insomnia is speculative. Central anticholinergic effects could in theory cause sedation, but they could equally impair cognition or worsen sleep quality. No mechanistic, clinical, or literature evidence in the compiled data confirms a benefit. The high TxGNN score (0.9939) is a model-based prediction only and should be treated as a hypothesis to test, not as proof of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Camylofin is registered in India under 20 valid licences (no cancelled licences). The licence data contain no approved indication text.

<!-- review:begin in-lic-20261124c-camylofin-2 -->

> **Review correction (2026-11-24)**: Originally stated: "Camylofin is registered in India under 20 valid single-ingredient licences (no cancelled licences)." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-camylofin-2 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 41 | Anafortan 25 mg/300 mg Tablet | Strip of 15 tablets | Valid |
| 486 | Anafortan-MF 50mg/250mg Tablet | Strip of 10 tablets | Valid |
| 498 | Anaspas 25mg Injection | Vial of 2 ml Injection | Valid |
| 1028 | Avapar Tablet | Strip of 10 tablets | Valid |
| 3355 | Avapar 25mg Injection | Vial of 2 ml Injection | Valid |
| 25919 | Bigspas-P Tablet | Strip of 10 tablets | Valid |
| 27172 | Bigspas 50mg Injection | Vial of 1 ml Injection | Valid |
| 36411 | Camyfyl 25mg/300mg Tablet | Strip of 10 tablets | Valid |
| 37778 | Carespas CP 25mg/300mg Tablet | Strip of 10 tablets | Valid |
| 40215 | Camyfyl Plus 50mg/325mg Tablet | Strip of 10 tablets | Valid |
| 40249 | Camyfyl 25mg Injection | Vial of 2 ml Injection | Valid |
| 41361 | Cyclobid CP 25mg/300mg Tablet | Strip of 10 tablets | Valid |
| 42154 | Camifort Suspension | Bottle of 30 ml Suspension | Valid |
| 50660 | Cyclobid CP Oral Suspension | Bottle of 30 ml Oral Suspension | Valid |
| 61205 | Dicloran Spas Tablet | Strip of 10 tablets | Valid |
| 67677 | Dimace M Tablet | Strip of 10 tablets | Valid |
| 125429 | Listaspas 50mg/325mg Tablet | Strip of 10 tablets | Valid |
| 199822 | Spasmonorm Tablet | Strip of 10 tablets | Valid |
| 200121 | Spasmonorm Injection | Ampoule of 2 ml Injection | Valid |
| 200802 | Spasmonorm M Tablet | Strip of 1 Tablet | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

Available dosage forms include injections, tablets, and oral suspensions.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug in the data compiled for this report, and no disease contraindications were identified in the knowledge graph.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for insomnia is a model prediction (L5), with no clinical trials or publications. The mechanism is unconfirmed, and the anticholinergic activity could plausibly worsen rather than improve sleep. Package insert safety information is also missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India Pharma website (a blocking gap for safety screening)
- Mechanism of action data from DrugBank to assess a plausible link to insomnia
- Confirmed original indication from the licence or label
- A targeted literature and trial search for camylofin and sleep outcomes
- Preclinical or early-phase evidence of benefit, with attention to central anticholinergic effects on cognition and sleep quality
- Assessment of route compatibility and similarity to the original indication (currently pending)

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

