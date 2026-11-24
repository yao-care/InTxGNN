---
layout: default
title: Benzydamine
parent: Model Prediction Only (L5)
nav_order: 101
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Benzydamine: predicted new indication Benign prostatic hyperplasia (evidence level L5). Approved use: Not stated in the registration records compiled for this report"
monitor_inn: "Benzydamine"
predicted_indications: ["benign prostatic hyperplasia (disease)"]
---

# Benzydamine
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

## Benzydamine: From Local Oral and Throat Use to Benign Prostatic Hyperplasia
{: .text-alpha }

## One-Sentence Summary

Benzydamine is marketed in India mainly as a mouthwash, gargle and dental gel product.
The TxGNN model predicts it may be effective for **benign prostatic hyperplasia (BPH)**, but **no clinical trials and no publications** currently support this direction, so the prediction is computational only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records compiled for this report (the approved indication text is blank for all licenses; products are oral rinses, gargles and a dental gel) |
| Predicted New Indication | Benign prostatic hyperplasia |
| TxGNN Prediction Score | 0.9926 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of benzydamine as: Cyclooxygenase inhibitor ([ChEMBL CHEMBL12610 (benzydamine): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL12610), CC BY-SA 3.0; accessed 2026-11-19.) Based on general background knowledge (not from the supplied data), benzydamine is a locally acting NSAID with anti-inflammatory, analgesic and local anaesthetic properties. These are thought to involve reduced pro-inflammatory cytokines such as TNF-alpha and IL-1beta, together with membrane-stabilising effects.

A possible link to the new indication is that inflammation is believed to contribute to prostatic enlargement and lower urinary tract symptoms, so an anti-inflammatory agent could plausibly be relevant. This link is speculative. The very high TxGNN score reflects a model prediction only, and it has not been tested in preclinical or clinical studies.

There is also a practical gap: all Indian products are mouth, throat or dental formulations. No route of administration suitable for prostatic disease has been identified, and route compatibility has not yet been assessed.

## India Market Information

Benzydamine has 20 valid registrations in India, with no cancelled licenses. The approved indication text is not recorded for any of them.

<!-- review:begin in-lic-20261124c-benzydamine-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Benzydamine has 20 valid single-ingredient registrations in India, with no cancelled licenses." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-benzydamine-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 26529 | B Mine Mouth Wash | Bottle of 200 ml Mouth Wash | Valid |
| 26843 | Biqol Mouth Wash Alcohol Free | Bottle of 300 ml Mouth Wash | Valid |
| 28475 | Biqol Mouth Wash | Bottle of 500 ml Mouth Wash | Valid |
| 29344 | Bzynice Mouth Wash | Bottle of 300 ml Mouth Wash | Valid |
| 29594 | Benzyda 0.15% Mouth Wash | Bottle of 200 ml Mouth Wash | Valid |
| 31318 | Bensodyl 7.5mg/6mg Mouth Wash | Bottle of 100 ml Mouth Wash | Valid |
| 59047 | Dresin Mouthwash & Gargle | Bottle of 100 ml Gargle | Valid |
| 80300 | Edel Mouth Wash | Bottle of 500 ml Mouth Wash | Valid |
| 95404 | Gositis Mouth Wash | Bottle of 450 ml Mouth Wash | Valid |
| 133811 | Maxtra Gargle | Bottle of 120 ml Mouth Wash | Valid |
| 133936 | Mucobenz Mouth Wash | Bottle of 500 ml Mouth Wash | Valid |
| 136429 | Mucobenz Mouth Wash | Bottle of 200 ml Mouth Wash | Valid |
| 162452 | Oralixir Mouth Wash | Bottle of 500 ml Mouth Wash | Valid |
| 164404 | Ora-Ace Mouth Wash Alcohol Free | Bottle of 300 ml Mouth Wash | Valid |
| 165112 | Oraeze Mouth Wash Mint | Bottle of 500 ml Mouth Wash | Valid |
| 187793 | Ready Rinse Mouth Wash | Bottle of 150 ml Mouth Wash | Valid |
| 200727 | Steri Mouth Wash | Bottle of 30 ml Mouth Wash | Valid |
| 202210 | Steri Gargle | Bottle of 100 ml Gargle | Valid |
| 215239 | Tantum Oral rinse | Bottle of 120 ml Mouth Wash | Valid |
| 216902 | Tantum Gel | Tube of 20 gm Dental Gel | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction records were available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but it is the only support. There are no clinical trials or publications for BPH, the mechanism data are missing, and all marketed products are oral or topical formulations with no clear route for a prostatic indication.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank) to test the proposed anti-inflammatory link to BPH
- Package insert warnings and contraindications from the India regulator, needed before any safety screening
- Preclinical or early clinical evidence of benefit in BPH or lower urinary tract symptoms
- Assessment of whether a suitable route or formulation exists for prostatic delivery, given that current products are local oral and dental forms

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL12610 (benzydamine): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL12610) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

